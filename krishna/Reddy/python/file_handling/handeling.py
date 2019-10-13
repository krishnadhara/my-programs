#b.open("abc",'r')
#b.read()
#open
#a=open("kvr",'w')
#a.write("vhkfdhkdjhfkjdhfjkhfkjhfid\n")
#a.write("vhkfdhkdjhfkjdhfjkhfkjhfid\n")
#apend

#c=open("abc","a")
#c.write("\n krishnareddysir")

f=open("abc","r")
a=open("kvr","w")

for i in f:
    a.write(i)

# readbinary(rb)

c=open("Capture1.PNG","rb")
f1=open("mypick.JPG","wb")
for i in c:
    f1.write(i)


#file=open("wordfile","w")
#file.write("krishnareddy")
#delating
import os
#os.remove() function

#os.remove("wordfile")


import os
if os.path.exists("wordfile"):
    os.remove("wordfile")
else:
    print("file does not exist")



file_names = ['file1.txt','file2.txt']
with open('venky_file.txt','w') as venky_file:
    for i in file_names:
        with open(i) as new_file:
            venky_file.write(new_file.read())
print("file opened successfully and add the data successfully!!!!")

