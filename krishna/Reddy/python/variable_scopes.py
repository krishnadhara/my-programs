#global variable
def f():
    print(s)
s="krishna reddy"
f()


def f():
    s="me too"
    print(s)
s="reddy"
f()
print(s)


def f():
    global s
    print(s)
    s="local"
    print(s)
s="global2"
f()
print(s)

a=1
def f():
    print(a)
def g():
    a=2
    print(a)
def h():
    global a
    a=3
    print(a)
print(a)
f()
print(a)
g()
print(a)
h()
print(a)

