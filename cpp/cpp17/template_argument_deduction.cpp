/*
Template argument deduction is also performed when the name of a class template is used as the type of an object being constructed:

Template argument deduction for class templates takes place in declarations and in explicit cast expressions; see class template argument deduction for details.
*/

int main() {
    std::pair p(2, 4.5);
    std::tuple t(4, 3, 2.5);
    std::copy_n(vi1, 3, std::back_insert_iterator(vi2));
    std::for_each(vi.begin(), vi.end(), Foo([&](int i) { ... }));
    auto lck = std::lock_guard(foo.mtx);
    std::lock_guard lck2(foo.mtx, ul);
}
