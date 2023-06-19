# Tips for C++


## [How can I declare and define multiple variables in one line using C++?](https://stackoverflow.com/questions/6838408/how-can-i-declare-and-define-multiple-variables-in-one-line-using-c)

With the following declaration, only the last variable (index) is set to 0:
```
int column, row, index = 0;
```

Instead, the following sets all variables to 0:
```
int column, row, index;
column = index = row = 0;
```

But personally, I find the following methods much more readable:
```
int column = 0, row = 0, index = 0;
int column = 0;
int row = 0;
int index = 0;
```

As of C++17, you can use [Structured Bindings](https://en.cppreference.com/w/cpp/language/structured_binding):
```
#include <iostream>
#include <tuple>

int main () 
{
    auto [hello, world] = std::make_tuple("Hello ", "world!");
    std::cout << hello << world << std::endl;
    return 0;
}
```