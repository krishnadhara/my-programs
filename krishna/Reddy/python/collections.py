from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple,OrderedDict
from collections import ChainMap
d=Counter('krishnareddydhara')
print(d)
print(dir(d))  #o/p 'clear', 'copy', 'elements', 'fromkeys', 'get', 'items', 'keys', 'most_common', 'pop', 'popitem', 'setdefault', 'subtract', 'update', 'values'
print(d['d'])  #    'clear', 'copy', 'default_factory', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
print(d['a'])
print(Counter('abracadabra').most_common())  # [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
print(Counter('abracadabra').most_common(3)) # [('a', 5), ('b', 2), ('r', 2)]

d=Counter('abracadabra')
print(list(d.elements()))      # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
print(tuple(d.elements()))     # ('a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd')
print(set(d.elements()))       # {'a', 'd', 'c', 'r', 'b'}
print(frozenset(d.elements())) # frozenset({'a', 'd', 'c', 'r', 'b'})
"""
d1=d.copy()             #d1=d   d1={10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
{}.fromkeys('pyt')      #d={}.fromkeys('pyt')  {'p': None, 'y': None, 't': None}
d.get(2)                #d.get(2)---- two
d.items()               #dict_items([(10, 'ten'), (2, 'two'), (3, 'three'), (4, 'four'),(5: 'five')])
d.keys()                #dict_keys([10, 2, 3, 4,5])
d.pop()                 # ten
d.popitem()             #(5, 'five')
d.setdefault(6)         #d.setdefault(6)-- {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five',6:None}
d.setdefault(6,'six')   #d.setdefault(6)-- {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five',6:'six'}
d.update({7:'seven'})   # {10: 'ten', 2: 'two', 3: 'three', 4: 'four', 5: 'five',7:'seven'}
d.values()              #dict_values(['ten', 'two', 'three', 'four', 'five', 'seven'])
d.clear()
d.elements()
d.most_common()
d.values()
"""

#defaultdict     'clear', 'copy', 'default_factory', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
s=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d=defaultdict(list)
for i,j in s:
    d[i].append(j)
print(d)
print(d.items()) #dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])
players = ["sachin cricket", "Federer tennis", "Nadal tennis", "virat cricket", "Messi football"]
d=defaultdict(list)
for i in players:
    j,k=i.split()
    d[k].append(j)
print(d) # defaultdict(<class 'list'>, {'cricket': ['sachin', 'virat'], 'tennis': ['Federer', 'Nadal'], 'football': ['Messi']})

s = "The red for jumped over the fence and ran to the zoo for food"
word=s.split()
dic={}
for i in word:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)  # {'The': 1, 'red': 1, 'for': 2, 'jumped': 1, 'over': 1, 'the': 2, 'fence': 1, 'and': 1, 'ran': 1, 'to': 1, 'zoo': 1, 'food': 1}

s = "The red for jumped over the fence and ran to the zoo for food"
word=s.split()
d=defaultdict(int)
for i in word:
    d[i]+=1
print(d)   #defaultdict(<class 'int'>, {'The': 1, 'red': 1, 'for': 2, 'jumped': 1, 'over': 1, 'the': 2, 'fence': 1, 'and': 1, 'ran': 1, 'to': 1, 'zoo': 1, 'food': 1})


#deque     'append', 'appendleft', 'clear', 'copy', 'count', 'extend', 'extendleft', 'index', 'insert', 'maxlen', 'pop', 'popleft', 'remove', 'reverse', 'rotate'

a=deque()
print(dir(a))
a.appendleft("first")
a.appendleft("second")
a.appendleft("first")
a.appendleft("second")
a.append('fore')
print(a)       # deque(['second', 'first', 'second', 'first', 'fore'])
print(a.pop())

n=[0,1,2,3,5,7,11,13]
a=deque(n)
print(a)    #deque([0, 1, 2, 3, 5, 7, 11, 13])

#namedtuple

a=namedtuple('parts','id_no desc cost amount')
auto_parts = a(id_no='1234',desc='ford',cost=1200,amount=10)
print(auto_parts.id_no)  #1234
print(auto_parts.cost)   #1200


c={'x':30,'y':45}
d=namedtuple('tuple',['x','y'])
e=d(**c)   #You can convert a dictionary to a namedtuple using the double-start-operator.
print(e)    #tuple(x=30, y=45)
print(e.x)   #30

#ordeddict
d=OrderedDict()
d[1]='one'
d[2]='two'
d[10]='ten'
print(d)  # OrderedDict([(1, 'one'), (2, 'two'), (10, 'ten')])

#chainmap

car_parts_a={'hood':500,'engine':5000,'front_door':750}
car_parts_b={'a/c':1000,'turbo':2500,'rollbar':300}
car_parts_c={'cover':100,'hood_hornament':150,'seat_cover':99}

car_price=ChainMap(car_parts_a,car_parts_b,car_parts_c)
print(car_price['hood'],['a/c'])