
# From /usr/lib/python3.6/shlex.py
import re

# see https://regex101.com/
# Match a single character not present in the list below [^\w@%+=:,./-]
#   \w matches any word character (equivalent to [a-zA-Z0-9_])
#   @%+=:,./- matches a single character in the list @%+=:,./- (case sensitive)
_find_unsafe = re.compile(r'[^\w@%+=:,./-]', re.ASCII).search

def quote(s):
    """Return a shell-escaped version of the string *s*."""
    if not s:
        return "''"
    # when s is an integer, it raised "TypeError: expected string or bytes-like object"
    if _find_unsafe(s) is None:
        return s

    # use single quotes, and put single quotes into double quotes
    # the string $'b is then quoted as '$'"'"'b'
    return "'" + s.replace("'", "'\"'\"'") + "'"

def static_type_quote(s: str):
    """Return a shell-escaped version of the string *s*."""
    if not s:
        return "''"
    # The `s` cannot be an integer now.
    if _find_unsafe(s) is None:
        return s

    # use single quotes, and put single quotes into double quotes
    # the string $'b is then quoted as '$'"'"'b'
    return "'" + s.replace("'", "'\"'\"'") + "'"

print("use string as parameter: ", quote('1'))
print("use string as parameter: ", quote('.'))
print("use string as parameter: ", quote('+'))
# because of `search` expected string as the parameter type.
#print("use interger as parameter: ", quote(1))

# It still can be run. But we have to check it before running
# $ mypy numeric_regex.py
# numeric_regex.py:41: error: Argument 1 to "static_type_quote" has incompatible type "int"; expected "str"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)
# see https://realpython.com/python-type-checking/
print("use interger as parameter: ", static_type_quote(1))

