import unittest
import sys
def append(x):
    x.append("modified")

def clear(x):
    x.clear()

def reset_by_assignment(x):
    x = [] # assign it


class RefcountTestCase(unittest.TestCase):
    """sys.getrefcount(object)
Return the reference count of the object. The count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to getrefcount().
    See https://docs.python.org/3/library/sys.html#sys.getrefcount

    """
    def test_refcnt(self):
        s = "abcd"
        print("{}".format(sys.getrefcount(s)))
        s0 = s
        s1 = s0
        print("s={}, s0={}, s1={}".format(sys.getrefcount(s), sys.getrefcount(s0), sys.getrefcount(s1)))


class PassByReferenceTestCase(unittest.TestCase):
    """Python always uses pass-by-reference values. There isn't any exception. Any variable assignment means copying the reference value. No exception. Any variable is the name bound to the reference value. Always.
    See https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

    You can think about a reference value as the address of the target object. The address is automatically dereferenced when used. This way, working with the reference value, it seems you work directly with the target object. But there always is a reference in between, one step more to jump to the target.

    List - a mutable type
    """


    def test_pass_by_ref(self):
        arr = ["A", 1]

        append(arr)

        self.assertEqual(["A", 1, "modified"], arr)  # add assertion here

    def test_clear_array_by_its_ref(self):
        arr = ["A", 1]

        clear(arr)

        self.assertEqual([], arr)

    def test_reset_array_by_its_ref(self):
        arr = ["A", 1]

        clear(arr)

        self.assertEqual([], arr)


class PassByCopyTestCase(unittest.TestCase):
    """String - an immutable type
It's immutable, so there's nothing we can do to change the contents of the string
    And bool, number are immutable types too.
    """

    def test_immutable_type_string(self):
        def reset_string(s):
            """string is also passed by reference.
            But when it is rewrote in the function, it will create a new space.
            Before the change, the id(s) equals to the id(outer_string).
            After that, the id(s) points a new space.
            """
            before = id(s)
            s = ""
            after = id(s)
            print("befor the change id={}, after={}".format(before, after))
            #self.assertEqual(before, after)

        outer_string = "Can the string be passed as reference too?"
        print(id(outer_string))
        reset_string(outer_string)
        self.assertEqual("", outer_string)

if __name__ == '__main__':
    unittest.main()

