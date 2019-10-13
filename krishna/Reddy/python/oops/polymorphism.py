#method over loading
class A:
    def product(self,a,b):
        v=a*b
        print(v)
    def product(self,a,b,c):
        p=a*b*c
        print(p)
obj=A()
obj.product(1,2,3)
obj.product(1,2,4)

#or

class A:
    def product(self,*args):
        print("hello")
obj=A()
obj.product(1,2,3)
obj.product(1,2)
obj.product(1)

def add(datatype, *args):
    if datatype =='int':
        answer = 0
    if datatype =='str':
        answer = ''
    for x in args:
        answer = answer + x
    print(answer)
add('int',1,2,3)
add('str','hi','geeks')

# operater overloading
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
p1=Point(2,3)
print(p1)
str(p1)
format(p1)
#################################
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x #2
        self.y = y #3
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,other):
        x = self.x + other.x #-1
        y = self.y + other.y #2
        return Point(x, y)
p1 = Point(2, 3)
p2 = Point(-1, 2)
print(p1 + p2) #(1,5)


#method over riding

class A:
    def sayhi(self):
        print("I'm in A")
class B(A):
    def sayhi(self):
        print("I'm in B")
obj = B()
obj.sayhi()
###############################
class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs.')
        #super().__init__('Dog')
        super(Dog,self).__init__('Dog')
d1 = Dog()

####################################
####################################
class Animal:
    def __init__(self, animalName):
        print(animalName, 'is an animal.')
class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)
class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammalName):
        print(NonWingedMammalName, "can't fly.")
        super().__init__(NonWingedMammalName)
class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammalName):
        print(NonMarineMammalName, "can't swim.")
        super().__init__(NonMarineMammalName)
class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.');
        super().__init__('Dog')
d = Dog()
print('')
bat = NonMarineMammal('Bat')


