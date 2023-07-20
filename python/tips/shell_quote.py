try:
    # Python3
    from shlex import quote as shell_quote
except ImportError:
    # Python2.x
    from pipes import quote as shell_quote


cmd = ["this", "is", 1, "number"]

# Return a shell-escaped version of the string
s = ' '.join(shell_quote(s) for s in cmd)

print(s)

#
#$ python2 shell_quote.py
#Traceback (most recent call last):
#  File "shell_quote.py", line 11, in <module>
#    s = ' '.join(shell_quote(s) for s in cmd)
#  File "shell_quote.py", line 11, in <genexpr>
#    s = ' '.join(shell_quote(s) for s in cmd)
#  File "/usr/lib/python2.7/pipes.py", line 269, in quote
#    for c in file:
#TypeError: 'int' object is not iterable

#$ python3 shell_quote.py
#Traceback (most recent call last):
#  File "shell_quote.py", line 11, in <module>
#    s = ' '.join(shell_quote(s) for s in cmd)
#  File "shell_quote.py", line 11, in <genexpr>
#    s = ' '.join(shell_quote(s) for s in cmd)
#  File "/usr/lib/python3.6/shlex.py", line 314, in quote
#    if _find_unsafe(s) is None:
#TypeError: expected string or bytes-like object


