class myclass():
    def method1(self):
        print("krishna")
    def method2(self,name):
        print("dhara"+name)
c=myclass()
c.method1()
c.method2("krishna")

def main():
    c=myclass()
    c.method1()
    c.method2("breath krishna")
main()

class childclass(myclass):
    def method1(self):
        print("chaild class method1")
    def mehod2(self):
        print("chaild class method2")
def main():
    c2=childclass()
    c2.method1()
    c2.mehod2()
    c.method1()
main()


# constructors
#A constructor is a class function that instantiates an object to predefined values.

#It begins with a double underscore (_). It __init__() method

class user():
    def __init__(self,name):
        self.name=name
    def sayhello(self):
        print("welcome to  "+self.name)
user1=user("krishna")
user1.sayhello()

#"Class" is a logical grouping of functions and data. Python class provides all the standard features of Object Oriented Programming.

#Class inheritance mechanism
#A derived class that override any method of its base class
#A method can call the method of a base class with the same name
#Python Classes are defined by keyword "class" itself
#Inside classes, you can define functions or methods that are part of the class
#Everything in a class is indented, just like the code in the function, loop, if statement, etc.
#The self argument in Python refers to the object itself. Self is the name preferred by convention by Pythons to indicate the first parameter of instance methods in Python
#Python runtime will pass "self" value automatically when you call an instance method on in instance, whether you provide it deliberately or not
#In Python, a class can inherit attributes and behavior methods from another class called subclass or heir class.
