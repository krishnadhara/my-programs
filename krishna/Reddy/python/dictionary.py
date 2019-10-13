#1. A dictionary is an unordered collection of key-value pairs.
#2. It’s a mutable type. We can add elements and remove elements from dictionary.
#3. It’s a built-in mapping type in Python where keys map to values. These key-value pairs provide an intuitive way to store data.
#4. Only immutable types (numbers, strings, tuples) can be used as dictionary keys. Values can be of any type.
#5. It is also known as Associative arrays or hash tables.
"""d = {'name': 'dreamwin', 'place': 'bangalore', 'started': 'Dec 2017'}
print(d)
print(dir(d))# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
print(d['name'],d['place'],d['started'])

# Adding items into dictionary during run-time:
dt={}
print(type(dt))
dt['lang']='python'
dt['year']=1990
dt['auther']='guido van rossum'
print(dt)

#Add or update items into dictionary:
#We can add new items or change the value of existing items using assignment operator.
#If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.
c={'name':'krishna','place':'nellore','start':2017}
c['love']='dhara'
c['place']='marathahalli'
c['course']=['python','data base']
print(c) #{'name': 'krishna', 'place': 'marathahalli', 'start': 2017, 'love': 'dhara', 'course': ['python', 'data base']}
c['course']='django'
print(c)  #{'name': 'krishna', 'place': 'marathahalli', 'start': 2017, 'love': 'dhara', 'course': 'django'}

#Delete or remove elements from dictionary:
# pop(),popitem(),del(),clear()
s = {1:1, 2:4, 3:9, 4:16, 5:25}
print(s.pop(2))  #0/p 4
print(s)    #o/p {1: 1, 3: 9, 4: 16, 5: 25}
print(s.popitem())  #o/p (5, 25)
print(s.popitem())  #o/p (4, 16)
del s[3]
print(s) #o/p {1: 1}
s[6]=36
s[7]=49
print(s)   #{1: 1, 6: 36, 7: 49}
#del s
#print(s)  # Traceback (most recent call last):

#Dictionary methods:
d={}
print(type(d))   #o/p <class 'dict'>
print(dir(d))   # 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

#clear()--The clear() method removes all items from the dictionary
d = {'started': 'Dec 2017', 'name': 'dreamwin', 10: 'ten', 'place':'bangalore', 'courses': ['Python', 'Datascience', 'Django']}
print(d.clear())   #o/p none
print(d)           # o/p {}

a={10:'ten',2:'two'}
print(a)
a1=a
print(a.clear())    #o/p None
print(a)            #o/p {}
print(a1)           #o/p {}

#copy()--They copy() method returns a shallow copy of the dictionary. It doesn't modify the original dictionary. It creates a new dictionary
d={10:'ten',2:'two',3:'three'}
d1=d.copy()
print(d1)  #o/p  {10: 'ten', 2: 'two', 3: 'three'}

#fromkeys()--The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.
a={}.fromkeys('python')
print(a) #o/p {'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}
b={}.fromkeys('python',10)
print(b) #o/p {'p': 10, 'y': 10, 't': 10, 'h': 10, 'o': 10, 'n': 10}

#get()--The get() method takes maximum of two parameters: key - key to be searched in the dictionary
s={10:'ten',2:'two',3:'three',4:'four'}
print(s.get(10))   #o/p ten the value for the specified key if key is in dictionary
print(s.get(2))    #o/p two
print(s.get(5))    #o/p None  None if the key is not found and value is not specified

#keys()

print(s.keys())    #o/p  dict_keys([10, 2, 3, 4])

#values()
print(s.values())  #o/p dict_values(['ten', 'two', 'three', 'four'])

#items()
print(s.items())    #o/p dict_items([(10, 'ten'), (2, 'two'), (3, 'three'), (4, 'four')])

#pop()
print(s.pop(10))   #o/p ten

#popitem()
print(s.popitem()) #o/p (4, 'four')

#setdefault()
s={10:'ten',2:'two',3:'three',4:'four'}
print(s.setdefault(5))
print(s)  #o/p {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: None}
print(s.setdefault(6,'six')) #o/p {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: None, 6: 'six'}
print(s)

#update()
s={10:'ten',2:'two',3:'three',4:'four'}
s.update({5:'five'})
print(s) #o/p {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
s.update(({'course':'python'}))
print(s) #o/p {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 'course': 'python'}
d={}

d={1:'apple',2:'ball'}
print(d)
d={'name':'john',1:[2,4,3]}
print(d)
e=dict({1:'apple',2:'ball'})
print(e)
f=dict([(1,'apple'),(2,'ball')])
print(f)
a={'name':'krishna','age':26}
print(a['name'],a['age'])
print(a.get('age'))
a['address']='downtown'
print(a)

s={1:1,2:4,3:9,4:16,5:25,6:36,7:49}
print(s.pop(5))
print(s)
print(s.popitem())
print(s)
del s[3]
print(s)
s.clear()
print(s)
"""
d={}
#type(d)  <class 'dict'>
#dir(d)   'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
d={10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

d1=d.copy()             #d1=d   d1={10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
{}.fromkeys('pyt')      #d={}.fromkeys('pyt')  {'p': None, 'y': None, 't': None}
d.get(2)                #d.get(2)---- two
d.items()               #dict_items([(10, 'ten'), (2, 'two'), (3, 'three'), (4, 'four'),(5: 'five')])
d.keys()                #dict_keys([10, 2, 3, 4,5])
d.pop(10)               # ten
d.popitem()             #(5, 'five')
d.setdefault(6)         #d.setdefault(6)-- {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five',6:None}
d.setdefault(6,'six')   #d.setdefault(6)-- {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five',6:'six'}
d.update({7:'seven'})   # {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five',7:'seven'}
d.values()              #dict_values(['ten', 'two', 'three', 'four', 'five', 'seven'])
d.clear()               # None

# Adding items into dictionary during run-time:
dt={}
print(type(dt))
dt['lang']='python'
dt['year']=1990
dt['auther']='guido van rossum'
print(dt)

#Add or update items into dictionary:
#We can add new items or change the value of existing items using assignment operator.
#If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.
c={'name':'krishna','place':'nellore','start':2017}
c['love']='dhara'
c['place']='marathahalli'
c['course']=['python','data base']
print(c) #{'name': 'krishna', 'place': 'marathahalli', 'start': 2017, 'love': 'dhara', 'course': ['python', 'data base']}
c['course']='django'
print(c)  #{'name': 'krishna', 'place': 'marathahalli', 'start': 2017, 'love': 'dhara', 'course': 'django'}

#Delete or remove elements from dictionary:
# pop(),popitem(),del(),clear()