#While Loop is used to repeat a block of code, It executes the code block multiple times until a certain condition is met.
def main():
    x=0
    while(x<4):
        print(x)
        x=x+1
main()
#In Python, "for loops" are called iterators.
#Just like while loop, "For Loop" is also used to repeat the program.
#But unlike while loop which depends on condition true or false. "For Loop" depends on the elements it has to iterate.
for x in range(2,7):
    print(x)

def main1():
    month=["jan","feb","mar","april","may","june"]
    for m in month:
        print(m)
main1()
#if __name__=="__main__":
#    main1()
for x in range(10,20):
    if x==15:
        break
    print(x) #[11,12,13,14]
for x in range(10,20):
    if x%5==0:    #[10,15,20]
        continue
    print(x) #[11,12,13,14,16,17,18,19]

#Enumerate function in "for loop" does two things
  #It returns the index number for the member
  #And the member of the collection that we are looking at
def main2():
    month = {"jan", "feb", "mar", "april", "may", "june"}
    for i,j in enumerate (month):
        print(i,j)
main2()
def main3():
    x=0
    while (x<4):
        print(x)
        x=x+1
main3()
def main():
    x=0
    for x in range(2,7):
        print(x)
main()

def main2():
    month = {"jan", "feb", "mar", "april", "may", "june"}
    for i in month:
        print(i)
main2()

def main():
    for x in range(10,20):
        if (x==15):
            break
        print(x)
main()


a="guru99"
print(a*3)

for i in "1115":
    print ("guru99"),i,




