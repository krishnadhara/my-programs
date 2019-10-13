#map,filter,reduce
#map(function_object,iterable1,iterable2)
def mul(x):
    return x*2
c=mul(4)
print(c)

a=map(lambda x:x*2, [1,2,3,4])
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

print(list(map(lambda x:x*2, [1,2,3,4])))

dict=[{'name':'python','points':10},{'name':'java',"points":8}]
print(list(map(lambda x:x['name'],dict)))
print(list(map(lambda x:x["points"]*10,dict)))
print(list(map(lambda x:x['name']=='python',dict)))
print(list(map(lambda x,y:x+y,[3,4,5],[6,7,8])))
dict=({'name':'python','points':10},{'name':'java',"points":8})
print(tuple(map(lambda x:x['name'],dict)))
print(tuple(map(lambda x,y:x+y,(3,4,5),(6,7,8))))
print(set(map(lambda x,y:x+y,{3,4,5},{6,7,8})))

#filter
f=[0,1,1,2,12,3,4,5,2,3,4,5,6,7,8,21,23,34,4,5,66,44]
odd_num=list(filter(lambda x:x%2!=0,f))
evn_num=tuple(filter(lambda x:x%2==0,f))
evn_num_set=set(filter(lambda x:x%2==0,f))
print(odd_num,evn_num,evn_num_set)

#recursion
def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))
a=fact(5)
print(a)

#closers
def kri(a,b):
    return a+b
def dha(fun):
    print(fun(2,4))
    print(fun(3,5))
dha(kri)

def contains_factory(x):
    def contains(lst):
        return x in lst
    return contains
contains_15 = contains_factory(15)
print(contains_15([1,2,3,4,5]))
print(contains_15([13,14,15,16,17]))


def outerfunc(x):
    def innerfunc():
        print(x)
    innerfunc()
outerfunc(7)

def outerfunc(x):
    def innerfunk():
        print(x)
    return innerfunk
my=outerfunc(7)
my()