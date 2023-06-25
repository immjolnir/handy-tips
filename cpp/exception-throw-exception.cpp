/* Throwing Exceptions in C++

The following example shows the syntax for throwing and catching exceptions in C++:

In this C++ throw exception example, the AddPositiveIntegers() function is called from inside the try block in the
main() function. The AddPositiveIntegers() expects two integers a and b as arguments, and throws an invalid_argument
exception in case any of them are negative.

The std::invalid_argument class is defined in the standard library in the <stdexcept> header file. This class defines
types of objects to be thrown as exceptions and reports errors in C++ that occur because of illegal argument values.

The catch block in the main() function catches the invalid_argument exception and handles it.
*/

#include <iostream>
#include <stdexcept>

using namespace std;

int AddPositiveIntegers(int a, int b) {
    if (a < 0 || b < 0) throw std::invalid_argument("AddPositiveIntegers arguments must be positive");

    return (a + b);
}

int main() {
    try {
        cout << AddPositiveIntegers(-1, 2);  // exception
    } catch (std::invalid_argument& e) {
        cerr << e.what() << endl;
        return -1;
    }
    return 0;
}
