#single inheritance
class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
# Inherited or Sub class (Note Person in bracket)
class Employee(Person):
    def isEmployee(self):
        return True
a=Person("krishna")
print(a.getName(),a.isEmployee())
a=Employee("dhara")
print(a.getName(),a.isEmployee())


#mulrtileval linheritance
class A:
    def eat(self):
        print('Eating...')
class B(A):
    def bark(self):
        print('Barking...')
class C(B):
    def sleep(self):
        print('sleeping...')
obj=C()
obj.eat()
obj.bark()
obj.sleep()

#multipul inheritance

class base1:
    def __init__(self):
        self.str1 = "Base1 init"
        print("Base1")
class base2:
    def __init__(self):
        self.str2 = "Base2 init"
        print("Base2")
class Derived(base1, base2):
    def __init__(self):
        base1.__init__(self)
        base2.__init__(self)
        print("Derived")
    def printStrs(self):
        print(self.str1, self.str2)
ob=Derived()
ob.printStrs()