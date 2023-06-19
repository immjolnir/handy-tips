// https://en.cppreference.com/w/cpp/language/structured_binding
// $ g++ -std=c++20 structed_binding.cpp
#include <array>
#include <iomanip>
#include <iostream>
#include <set>
#include <string>

// Combining this with std::array and template argument deduction we can write a function that assigns a value to an
// arbitrary number of variables without repeating the type or value.
template <int N, typename T>
auto assign(T value) {
    std::array<T, N> out;
    out.fill(value);
    return out;
}

int main() {
    std::set<std::string> myset{"hello"};

    for (int i{2}; i; --i) {
        if (auto [iter, success] = myset.insert("Hello"); success)
            std::cout << "Insert is successful. The value is " << std::quoted(*iter) << ".\n";
        else
            std::cout << "The value " << std::quoted(*iter) << " already exists in the set.\n";
    }

    struct BitFields {
        // C++20: default member initializer for bit-fields
        int b : 4 {1}, d : 4 {2}, p : 4 {3}, q : 4 {4};
    };

    {
        const auto [b, d, p, q] = BitFields{};
        std::cout << b << ' ' << d << ' ' << p << ' ' << q << '\n';
    }

    {
        const auto [b, d, p, q] = [] { return BitFields{4, 3, 2, 1}; }();
        std::cout << b << ' ' << d << ' ' << p << ' ' << q << '\n';
    }

    {
        BitFields s;

        auto& [b, d, p, q] = s;
        std::cout << b << ' ' << d << ' ' << p << ' ' << q << '\n';

        b = 4, d = 3, p = 2, q = 1;
        std::cout << s.b << ' ' << s.d << ' ' << s.p << ' ' << s.q << '\n';
    }

    {
        auto [a, b, c] = assign<3>(1);
        for (const auto& v : {a, b, c}) {
            std::cout << v << std::endl;
        }
    }
}
