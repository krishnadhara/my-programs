import re
print(dir(re)) #'compile', 'copyreg', 'enum', 'error', 'escape', 'findall',
# 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split',
 #'sre_compile', 'sre_parse', 'sub', 'subn', 'template'
#'A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE',
# 'M', 'MULTILINE', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X',
nameage='''
Krishna is 24 and Dhara is 20
Sushmi is 17 ans Anu is 30'''

ages=re.findall(r'\d{1,3}',nameage)
names=re.findall(r'[A-Z][a-z]*',nameage)
agedict={}
x=0
for i in names:
    agedict[i] = ages[x]
    x+=1
print(agedict)
#####################search#################
import re
a="cookie"
b="cake and cookie"
d=re.search(a,b)
print(d.group())   # cookie
####################match################
import re
l="C"
m="IceCream"
re.match(l,m)
n="Cake"
print(re.match(l,n).group())    # C
############################ COMPILE ################
import re
s=re.compile(r'cookie')
f='Cake and cookie'
print(s.search(f).group())    #cookie
print(re.search(s,f).group()) #cookie
################ group ################

str="purple alice-b@google.com mokey diswasher"
match=re.search('([\w-]+)@([\w.-]+)',str)
if match:
    print(match.group())     #  alice-b@google.com
    print(match.groups())    # ('alice-b', 'google.com')
    print(match.group(1))    # alice-b
    print(match.group(2))    # google.com
##################### findall #####################
import re
email="please contact us at : kvenkatakrishna98@gmail.com," \
      "dharakvr19@yahoo.co.in," \
      "dharakrishna218@google.com"
address=re.findall(r'[\w.-]+@[\w.-]+',email)
p=re.compile('\d')     # ['1', '1', '4', '1', '8', '8', '6']
print(p.findall("i went to him at 11 a.m on 4th july 1886"))
p=re.compile('\d+')    # ['11', '4', '1886']
print(p.findall('i want to him at 11 a.m on 4th july 1886'))
##################### split ##########################3
text='''John Doe
        Jane Doe
        Jin Du
        Chin Doe'''
import re
result=re.split(r'\n+',text)
print(result) #['John Doe', '     Jane Doe', '    Jin Du', '        Chin Doe']


a="hello, welcome to! python"
print(re.split(", |!",a)) #['hello', 'welcome to', ' python']
print(re.split('[a-f]+','0a3B9',flags=re.IGNORECASE))#['0', '3', '9']
################################### SUB ###########
import re
p=re.compile(r'[0-9]+')
r=p.sub('_',"there is only 1 thing 2 do")
print(r) #there is only _ thing _ do

email='plese contact us at :kvenkatakrishna98@gmail.com'
n_email=re.sub(r'([\w\.-]+)@([\w\.-]+)',r'support@google.com',
               email)
print(n_email) #support@google.com

############## subn   ###################
import re
print(re.subn('ub','ab','subject has Uber booked already'))
#('sabject has Uber booked already', 1)
t = re.subn('ub', 'ab' , 'Subject has Uber booked already', flags = re.IGNORECASE)
print(t)#('Sabject has aber booked already', 2)
print(len(t))  #2
print(t[0])  #Sabject has aber booked already
####################Escape##################
import re
print(re.escape("This is Awseome even 1 A.M"))
#This\ is\ Awseome\ even\ 1\ A\.M
print(re.escape("I Asked what is this [a-9],he said \t ^WoW"))
#I\ Asked\ what\ is\ this\ \[a\-9\]\,he\ said\ \	\ \^WoW
######################### multiline#################
import re
ss = """abc
        def
        ghi"""
r1 = re.findall(r"^\w", ss)  #  ['a']
r2 = re.findall(r"^\w", ss, flags = re.MULTILINE)
print(r1)
print(r2)
##################### DOTALL #################
import re
ss = """once upon a time, there lived a king"""
r1 = re.findall(r".+", ss) # ['once upon a time,', 'there lived a king']
r2 = re.findall(r".+", ss, re.DOTALL)
print(r1)
print(r2)
################ unicode #################
import re
x1 = re.search(r"\w+", u"♥αβγ!", re.U)
x2 = re.search(r"\w+", u"♥αβγ!")
if x1:
    print(x1.group().encode("utf8"))  # αβγ
else:
    print("no match")
print(x2)