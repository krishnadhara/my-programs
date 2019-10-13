import time
def num(m):
    t1 = time.time()
    for i in range(0, m):
              print(i)
    t2 = time.time()
    print(str(t2 - t1))
num(3)
#################################################

print('ab\ncd\nef'.splitlines())    #['ab', 'cd', 'ef']

############################################################3
a={}

a[2]=1

a[1]=[2,3,4]

print(a[1][1])  #3
##########################################
lst = [1, 2, 3]

print(lst[3])   #IndexError
#####################################
a = ('check',)
n = 2
for i in range(int(n)):
    a = (a,)
    print(a)   # (('check',),) ((('check',),),)
#####################################################################
def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)
a=fact(4)
print(a)    #24
##################################################################