def hello():
    print("hello world")
hello()

def hello():
    print("hello world")
    return("hello krishna")
def hello_noreturn():
    print("helloworld")
    return("asdfghg")
a=hello()
print(a)
b=hello_noreturn()
print(b)
def addition(a,b):
    c=a+b
    return a,b,c
val=addition(3,4)
print(val)

def hello(a,b=2):
    return a+b
c=hello(a=1)
print(c)
def hello(a,b=2):
    return a+b
c=hello(a=1,b=3)
print(c)

def hello(*args):
    return args
c=hello(1,4,5)
print(c)
c=hello()
print(c)


def hello(**kwargs):
    return kwargs
a=hello(name="krishna",year=1993)
print(a)

def hello(a,b=2,*args,**kwargs):
    print(a,b)
    print("args:",args)
    print("kwargs:",kwargs)
a=hello(10,50,[1,2,3],"hello",10.5,{1:2},name="krishna",year=1993)
# lambda

lamb=lambda x:x**3
print(lamb(5))
val=lambda x,y:x+y
c=val(2,4)
print(c)
