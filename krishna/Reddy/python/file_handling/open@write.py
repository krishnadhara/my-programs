#open() write() close()
# 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name',
# 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
#write :
f = open(r"C:\Users\DHARA\python_venky\krishna\Reddy\welcome",'w')
f.write("my first file\n")
f.write("this file having in thres position becose you pout back slace n that represent newline\n")
f.write("contains three lineshfdhgkfhgkhgfd gfdkghkfdhgkfdhgfdhg fgkfdfgklhfkghkgh klhkghdfkfhgkdhg khkhgo gljgklhgkf g gkhkgh\n")
f.write("my first file\n")
f.write("this file having in thres position becose you pout back slace n that represent newline\n")
f.write("contains three lineshfdhgkfhgkhgfd gfdkghkfdhgkfdhgfdhg fgkfdfgklhfkghkgh klhkghdfkfhgkdhg khkhgo gljgklhgkf g gkhkgh\n")
f.close()

#writelines
# Using writelines we can write multiple lines into file through list of lines
l = open(r"C:\Users\DHARA\python_venky\krishna\Reddy\aelcome",'w')
l.writelines(['one\n','two\n','three\n'])
l.writelines("this is krishna reddy i am good at python developing")
l.close()
#append  :

k=open(r"C:\Users\DHARA\python_venky\krishna\Reddy\aelcome",'a')
k.write("\nmy first file\n")
k.write("thisfile\n\n")
k.write("contains three lines\n")
k.close()



try:
    f=open(r"C:\Users\DHARA\python_venky\krishna\Reddy\aelcome")
finally:
    f.close()



#j=open(r"C:\Users\DHARA\python_venky\krishna\Reddy\welcome")
#k=10
#data=""
#while True:
#   data=j.read(k)
#   #print(data,end="")
#   if data == "":
#       break
#f.close()


#with open(r"C:\Users\DHARA\python_venky\krishna\Reddy\welcome") as z:
   #for i in z:
        #print(i,end="")


with open(r"C:\Users\DHARA\python_venky\krishna\Reddy\celcome",'w') as k:
    k.write("one D\n")
    k.write("TWO D\n")
    k.write("THREE D\n")
    k.write("FOUR D\n")
