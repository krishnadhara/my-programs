#open()  write()  read()  close()

#print(open(r"C:\Users\DHARA\Desktop\krishna.txt","r"))
#print(open(r"C:\Users\DHARA\Desktop\krishna.txt","w"))



f = open(r"C:\Users\DHARA\python_venky\krishna\Reddy\welcome",'r')     #krishna reddy loves dhara
#data = f.read() # reads entire content from a file and stores in a string    ( krishna reddy loves dhara)
#print(data)
#data = f.read(5) # reads only first five characters from file.    (kris)
#print(data)
#data = f.read(10) # reads other ten characters from file.
#print(data)
#print(f.read(4)) # 'This' # read the first 4 data   kris
#print(f.read(4)) # ' is ' # read the next 4 data    hna
#print(f.read()) # read in the rest till end of file   reddy loves dhara

#f.read() # ' ' # further reading returns empty sting
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readlines())  #['krishna reddy loves dhara\n', 'my name is krishna i am\n', 'searching for job and\n', 'good salory if  i am eligibul\n', 'plese inform me\n']

#Reading a file using for loop:
# We can read a file line-by-line using a for loop. This is both efficient and fast
for i in f:
    print(i,end='')
print(dir(f.read()))   #'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
                       # 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
                       #'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
                       # 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


