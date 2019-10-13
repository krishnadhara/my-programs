#list
l=[1,2,3,4,5,1.2,1.3,1.5,'sun','mon','tus','wed']
for i in l:
    print(i)
#string
s="krishnareddy"
for i in s:
    print(i)
#tuple
t=('a','b','c',1,2,3,'krishna','reddy')
for i in t:
    print(i)
#dictionary
d={1:'one',2:'two',3:'three',10:'ten'}
for i in d:
    print(i)
#set
s={'one','two','three',1,2,3,4}
for i in s:
    print(i)

for i in "python":
    if i=="o":
        break
    else:
        print(i)
print("out side loop")

for i in "krishna":
    if i=="s":
        continue
    else:
        print(i)
print("the end")
for i in range(10):
    pass
def hello():
    pass
hello()
s="krishna"
for i in s:
    print(i)
else:
    print("iterated over everything")
s="krishna"
for i in s:
    if i=="z":
        break
    print(i)
else:
    print("iterated over everything")

count=0
while count<=5:
    print(count)
    count+=1
else:
    print("inside else block of while loop")

x=5
while x<=10:
    print(x)
    x+=1
    if x==7:
        break
else:
    print("inside else")

#while True:
#    print("this is an infinet loop")
