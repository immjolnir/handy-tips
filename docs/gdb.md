# GDB

## [How to pass google command line flags as an argument to GDB](https://stackoverflow.com/questions/60444364/how-to-pass-google-command-line-flags-as-an-argument-to-gdb)

2 ways for it.
- `gdb --args /path/to/binary --flag1=foo --flag2=bar --flag3="hi there"`

- `(gdb) run --flag1=foo --flag2=bar --flag3="hi there"`

### example: [Check.sh @ carla](https://github.com/carla-simulator/carla/blob/master/Util/BuildTools/Check.sh)
- example-carla-Util-BuildTools-Check.sh
