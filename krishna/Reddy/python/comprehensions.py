#list comprehensions
nums=[1,2,3,4]
squares=[]
for i in nums:
    squares.append(i*i)
print(squares)


#list_comprehension
squares=[n*n for n in nums]
print(squares)

a=[1,2,3,4,5,6]
b=[e*2 for e in a]
print(b)

y="welcome to world of python"
z=[len(x) for x in y.split()]
print(z)

#list_comprehension with if condition
n=[x**2 for x in range(11) if x%2==0]
print(n)

z=[1,2,3]
x=['a','b','c']
c=[str(i)+j for i in z for j in x]
d=[i+str(j) for i in x for j in z]
print(c)
print(d)

a=[1,2,3,4,7]
b=[2,6,5,4,3]
num=[i for i in a for j in b if i==j]
print(num)

m=[[1,2],[3,4],[5,6],[7,8]]
t=[]
for i in range(2):
    t_raw=[]
    for raw in m:
        t_raw.append(raw[i])
        t.append((t_raw))
print(t)

d=[[j[i] for j in m] for i in range(2)]
print(d)

#dictionary comprehensions
l=[2,4,3,5]
s={i:i*i for i in l}
print(s) #o/p {2: 4, 4: 16, 3: 9, 5: 25}

d={'a':10,'b':34,'A':7,'z':3}
out={k.lower():d.get(k.lower(),0)+d.get(k.upper(),0)  for k in d}
print(out)

dict={'a':1,'b':2,'c':3}
cdict={value:key for key,value in dict.items()}
print(cdict)