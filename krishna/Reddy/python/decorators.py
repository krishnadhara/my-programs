def foo(bar):
    return bar+1
def call_foo_wih_arg(foo,arg):
    return foo(arg)
print(call_foo_wih_arg(foo,3))
############################################
def p():
    print("parent")
    def f_c():
        return 'first_child'
    def s_c():
        return 'second_child'
    print(f_c())
    print(s_c())
p()
##################################################
def outer(word):
    def inner():
        print(word)
    return inner()
a=outer("krishna")
###############################################
def decorator(wrapped):
    def inner():
        print("i got decorator")
        wrapped()
    return inner()
def ordinary():
    print("i am ordinary function")
ordinary()

##################################################
####@@@@@@@@@@ function decorators @@@@@@@@######
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner

def divide(a, b):
    return a / b

divide(2, 5)

############################################
def decorator(arg1, arg2):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print("Congratulations. You decorated a function that does something with %s and %s" % (arg1, arg2))
            function(*args, **kwargs)
        return wrapper
    return real_decorator
@decorator("arg1", "arg2") # decorator("arg1", "arg2")(print_args)(1, 2, 3)
def print_args(*args):
    for arg in args:
        print(arg)
print_args(1, 2, 3,56,46)
