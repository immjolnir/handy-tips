# [Dry-run a potentially dangerous script?](https://stackoverflow.com/questions/22952959/dry-run-a-potentially-dangerous-script)

bash does not offer dry-run functionality (and neither do ksh, zsh, or any other shell I know).

It seems to me that offering such a feature in a shell would be next to impossible: state changes would have to be simulated and any command invoked - whether built in or external - would have to be aware of these simulations.

The closest thing that bash, ksh, and zsh offer is the ability to syntax-check a script without executing it, via option -n:

bash -n someScript  # syntax-check a script, without executing it.
If there are no syntax errors, there will be no output, and the exit code will be 0.
If there are syntax errors, analysis will stop at the first error, an error message including the line number is written to stderr, and the exit code will be:
2 in bash
3 in ksh
1 in zsh
Separately, bash, ksh, and zsh offer debugging options:

-v to print each raw source code line[1] to stderr before it is executed.

-x to print each expanded simple command to stderr before it is executed (env. var. PS4 allows tweaking the output format).





## [Add some dry run option to script](https://unix.stackexchange.com/questions/433801/add-some-dry-run-option-to-script)

Do proper command line parsing and then choose how to do the actual dry running.

The command line parsing:
```
#!/bin/sh

dry_run=false

while getopts 'n' opt; do
    case "$opt" in
        n) dry_run=true ;;
        *) echo 'error in command line parsing' >&2
           exit 1
    esac
done
```
Now, `$dry_run` will be true if the user invoked the script with the `-n` command line option.

Then, choose how to do the dry running. A simple way would be to use `set -v `(display the commands as they are read by the shell) followed by `set -n` (don't actually run anything):
```
if "$dry_run"; then
    set -v
    set -n
fi
```
This may not be what you want though as it would just display the script.

Instead you may choose to do
```
if "$dry_run"; then
    cmd=echo
else
    cmd=''
fi
```
and then prefix the specific commands that you'd like to dry run with $cmd:
```
$cmd ls -l
$cmd echo "hello world"
```