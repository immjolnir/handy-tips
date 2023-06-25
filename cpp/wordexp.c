/*Tilde Expansions

- The tilde is part of the shell expansion, it's not something handled by the underlying operating system. You need to resolve it yourself.
https://stackoverflow.com/questions/57852502/open-an-ofstream-with-tilde-in-path-name
     

The Bash shell provides some variables that are prefixed with ‘~’ (named tilde) which is called Tilde Expansions.

- Tilde expansion applies to the ‘~’ plus all following characters up to whitespace or a slash. It takes place only at the
beginning of a word, and only if none of the characters to be transformed is quoted in any way.

Plain ‘~’ uses the value of the environment variable HOME as the proper home directory name. ‘~’ followed by a user name
uses getpwname to look up that user in the user database, and uses whatever directory is recorded there. Thus, ‘~’
followed by your own name can give different results from plain ‘~’, if the value of HOME is not really your home
directory.


- https://man7.org/linux/man-pages/man3/wordexp.3.html

The expansion
       The expansion done consists of the following stages: tilde
       expansion (replacing ~user by user's home directory), variable
       substitution (replacing $FOO by the value of the environment
       variable FOO), command substitution (replacing $(command) or
       `command` by the output of command), arithmetic expansion, field
       splitting, wildcard expansion, quote removal.

       The result of expansion of special parameters ($@, $*, $#, $?,
       $-, $$, $!, $0) is unspecified.

       Field splitting is done using the environment variable $IFS.  If
       it is not set, the field separators are space, tab, and newline.
*/
#include <stdio.h>
#include <stdlib.h>
#include <wordexp.h>

int main(void) {
    wordexp_t p;
    char** w;

    // wordexp("[a-c]*.c", &p, 0);
    // wordexp("~/tmp~.log~", &p, 0); // the expansions to the first tilde.
    // ~user
    wordexp("~root", &p, 0); // /root
    w = p.we_wordv;
    for (size_t i = 0; i < p.we_wordc; i++) printf("%s\n", w[i]);
    wordfree(&p);
    exit(EXIT_SUCCESS);
}
