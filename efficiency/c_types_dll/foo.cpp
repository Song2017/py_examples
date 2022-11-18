#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
using namespace std;
class Foo
{
public:
    void bar()
    {
        cout << "hello c++" << endl;
    }

    char *hello(char *name)
    {
        char hello[] = "Hello";
        char *greeting = (char *)malloc(sizeof(char) * (strlen(name) + strlen(hello) + 1));
        if (greeting == NULL)
            exit(1);
        strcpy(greeting, hello);
        strcat(greeting, name);
        return greeting;
    }
    float add_float(float f1, float f2)
    {
        cout << f1 << endl;
        cout << f2 << endl;
        cout << f1 + f2 << endl;
        float return_value = f1 + f2;
        return return_value;
    }
};

extern "C"
{
    Foo *Foo_new() { return new Foo(); }
    void Foo_bar(Foo *foo) { foo->bar(); }
    char *Foo_hello(Foo *foo, char *name) { return foo->hello(name); }
    float Foo_add(Foo *foo, float a, float b) { return foo->add_float(a, b); }
}