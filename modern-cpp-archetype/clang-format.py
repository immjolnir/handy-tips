#!/usr/bin/env python3

#                     The LLVM Compiler Infrastructure
#
# This file is distributed under the University of Illinois Open Source
# License. See LICENSE.TXT for details.

import argparse
import collections
import shutil
import difflib
import os
import re
import subprocess
import sys

# Python3 and python2 stuffs.
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import configparser

def get_conf_bool(conf, section_name, opt_name, default_val=False):
    try:
        return conf.getboolean(section_name, opt_name)
    except NoOptionError:
        return default_val


def find_config():
    # Try to find the formatter config at these places.
    curr_dir = os.path.abspath(os.getcwd())
    search_paths = []
    while True:
        search_paths.append(os.path.join(curr_dir, ".formatter"))
        if os.path.exists(os.path.join(curr_dir, ".git")) or curr_dir == "/":
            # Stop at the root of the repo, or the root of the filesystem.
            break
        else:
            curr_dir = os.path.abspath(os.path.join(curr_dir, os.pardir))
    conf_found = False
    conf = configparser.ConfigParser()
    for p in search_paths:
        if not os.path.isfile(p):
            continue
        with open(p, 'r') as fh:
            conf.read_file(fh)
            conf_found = True
            break
    return conf, conf_found, search_paths


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', "--config-path",
                        help=('configuration file path (if not provided'
                              ' it will be searched for)'))
    parser.add_argument('-f', "--path", help='path to format', required=True)
    parser.add_argument('-s', "--read-stdin", help='read stdin for lines to format',
                        action='store_true', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    args = parser.parse_args()
    conf, conf_found, search_paths = find_config()
    if not conf_found:
        print("Could not find formatter configuration,"
              " searched in: %s" % (", ".join(search_paths)))
        sys.exit(1)

    excludes = set()
    try:
        for path in conf.get("formatter", 'exclude').split(","):
            path = path.strip()
            if path:
                excludes.add(path)
    except NoOptionError:
        pass
    filename = args.path
    if filename in excludes:
        if args.verbose:
            print("File %s is excluded, nothing to format." % filename)
        sys.exit(0)
    with open(filename, 'rb') as fh:
        lines = fh.readlines()
        am_lines = len(lines)
    if am_lines == 0:
        if args.verbose:
            print("Nothing in %s to format (empty file?)" % filename)
        sys.exit(0)
    # See if stdin provided certain chunks to format (vs the whole file).
    lines_by_file = collections.defaultdict(list)
    stdin_lines = 0
    if args.read_stdin:
        for line in sys.stdin:
            stdin_lines += 1
            match = re.search('^@@.*\+(\d+)(,(\d+))?', line)
            if match:
                start_line = int(match.group(1))
                line_count = 1
                if match.group(3):
                    line_count = int(match.group(3))
                if line_count == 0:
                    continue
                end_line = start_line + line_count - 1
                lines_by_file[filename].append((start_line, end_line))
    if not lines_by_file and stdin_lines > 0:
        print("Stdin provided %s input lines but none of"
              " them matched (bad format?)" % stdin_lines)
        sys.exit(1)
    if not lines_by_file:
        # Format the whole file.
        lines_by_file[filename] = [(1, am_lines)]
    binary = conf.get("formatter", "binary")
    if not binary.startswith("/"):
        binary_cmd = shutil.which(binary)
        if not binary_cmd:
            print("Could not find %s binary" % binary)
            sys.exit(1)
    else:
        if not os.path.exists(binary):
            print("Could not find %s binary at its specified path" % binary)
            sys.exit(1)
        binary_cmd = binary
    apply_edits = get_conf_bool(conf, "formatter", "apply_edits")
    sort_includes = get_conf_bool(conf, "formatter", "sort_includes", default_val=True)
    style = conf.get("formatter", "style")
    # Reformat files containing changes in place.
    for filename, format_lines in lines_by_file.items():
        tmp_lines = []
        for (start_line, end_line) in format_lines:
            tmp_lines.append(str(start_line) + ':' + str(end_line))
        if apply_edits and args.verbose:
            print('Formatting %s (between lines %s)' % (filename,
                                                        ", ".join(tmp_lines)))
        command = [binary_cmd, filename]
        if apply_edits:
            command.append('-i')
        if sort_includes:
            command.append('-sort-includes')
        for start_end_line in tmp_lines:
            command.extend([
                "-lines",
                start_end_line,
            ])
        command.append('-style=%s' % style)
        command_str = " ".join(command)
        if args.verbose:
            print("Running: %s" % command_str)
        p = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=None,
            stdin=subprocess.PIPE,
            universal_newlines=True)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            command_str = " ".join(command)
            print("Failed running `%s` (exit_code=%s)" % (command_str,
                                                          p.returncode))
            sys.exit(p.returncode)
        if not apply_edits:
            formatted_code = StringIO(stdout).readlines()
            diff = difflib.unified_diff(lines, formatted_code, filename,
                                        filename, '(before formatting)',
                                        '(after formatting)')
            diff_string = ''.join(diff)
            if len(diff_string) > 0:
                sys.stdout.write(diff_string)


if __name__ == '__main__':
    main()
