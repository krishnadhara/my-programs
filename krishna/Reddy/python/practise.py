def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
f(2)
f(3,[3,2,1])


s=set()
s.add(10)
print(s)

l=[]
l.append(10)
l.append('hello')
l.append([1,2,3])
print(l)
l.extend('hello')
print(l)

a=[5,4,6,7,3,2,1]
a.sort()
print(a)
a=[5,4,6,7,3,2,1]
sorted(a)
print(a)


a="krishna loves with dhara"
a.split()
print(a)
''.join(a)
print(a)

# define a list
list = [4, 7, 0, 3]
iter_list=iter(list)
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))