s="krishnareddy"
it=iter(s)
print(it.__next__()) #k
print(it.__next__()) #r
print(it.__next__()) #i
print(it.__next__()) #s
print(it.__next__()) #h
print(it.__next__()) #n
print(list(it))   # ['a', 'r', 'e', 'd', 'd', 'y']
# print(it.__next__())   StopIteration

# COSTOM ITERATER
class powtow():
    def __init__(self,max=0):
        self.max=max
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
a=powtow(4)
i=iter(a)
print(i.__next__()) #1
print(i.__next__()) #2
print(i.__next__()) #4
print(i.__next__()) #8
print(i.__next__()) #16
print(list(i))      #[1, 2, 4, 8, 16]
#We can also use a for loop to iterate over our iterator class
for i in powtow(4):
    print(i) #o/p 1 2 4 8 16

#GENETATOR
"""def my_gen():
    yield "hello"
    yield "krishna"
    yield 5
    yield 10
a=my_gen()
print(a)
print(a.__next__()) #hello
print(a.__next__()) # krishna
print(a.__next__()) # 5
print(a.__next__()) #10
print(a.__next__())
print(a.__next__())"""


#generater exprection or generater comprehenction
"""l=[1,3,6,10]
m=(x**2 for x in l)
print(m)
print(m.__next__()) #1
print(m.__next__()) #9
print(m.__next__()) #36
print(m.__next__()) #100
print(m.__next__()) # StopIteration
"""

"""def powtow(max=0):
    n=0
    while n<max:
        yield 2**n
        n+=1
a=powtow(5)
print(a)
print(a.__next__()) #1
print(a.__next__()) #2
print(a.__next__()) #4
print(a.__next__()) #6
print(a.__next__()) #8
print(a.__next__()) #16 
"""
#Represent Infinite Stream

def eve():
    a=0
    while True:
        yield a
        a+=2
a=eve()
print(a.__next__()) #0
print(a.__next__()) #2
print(a.__next__()) #4
print(a.__next__()) #6