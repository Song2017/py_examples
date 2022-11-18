# g++ -fpic -shared -o lib_test.so foo.cpp
# https://stackoverflow.com/questions/145270/calling-c-c-from-python
# https://docs.python.org/3/library/ctypes.html#module-ctypes
from ctypes import cdll
import ctypes
lib = cdll.LoadLibrary("./lib_test.so")
lib.Foo_add.restype = ctypes.c_float
lib.Foo_hello.restype = ctypes.c_char_p


class Foo:
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

    def hello(self, name_in):
        _result = lib.Foo_hello(self.obj, ctypes.c_char_p(name_in.encode()))
        return _result


    def adder(self, a_in, b_in):
        ans = lib.Foo_add(self.obj, ctypes.c_float(a_in), ctypes.c_float(b_in))
        return ans


if __name__ == "__main__":
    foo = Foo()
    foo.bar()
    print(foo.adder(22.1, 33.1))
    print(foo.hello('asd'))
