#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>

#if explicit_forced
// no implicit conversions are allowed whatsoever
#define NO_IMPLICIT_CONVERSION explicit
#else
#define NO_IMPLICIT_CONVERSION
#endif

struct Foo {
    std::string data;
};

struct Bar {
    int data;

    // to Foo
    NO_IMPLICIT_CONVERSION operator Foo() const noexcept;

    // NO_IMPLICIT_CONVERSION operator Foo() const noexcept {
    //     std::stringstream ss;
    //     ss << std::setw(5) << std::setfill('0') << data;
    //     Foo foo;
    //     foo.data = ss.str();
    //     return foo;
    // }

    // to int
    operator int() const noexcept { return data; }

    // to double
    explicit operator double() const noexcept { return data * 1.1; }
};

// ‘explicit’ cannot be used outside class declaration
Bar::operator Foo() const noexcept {
    std::stringstream ss;
    ss << std::setw(5) << std::setfill('0') << data;
    Foo foo;
    foo.data = ss.str();
    return foo;
}

int main() {
    Bar bar{12};

#if explicit_forced
    Foo foo = (Foo)bar;
#else
    // Allow implicit conversion
    Foo foo = bar;
#endif

    std::cout << foo.data << std::endl;

    int i = bar;
    std::cout << i << std::endl;

    double iwantdouble = bar;
    std::cout << "iwantdouble=" << iwantdouble << std::endl;  // 12, 这是受到了 int() 的影响了, 容易引起bug

    double d = (double)bar;
    std::cout << d << std::endl;  // 13.2
}
