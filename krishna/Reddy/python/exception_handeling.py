try:
    a=10/0
except:
    print ("arthmetic exception")
else:
    print("successfully done")

try:
    a=10/5
    print(a)
except:
    print("arithmetic exception")
else:
    print("sucessfully down")
finally:
    print("finally")
#rise exception
try:
    a=int(input("enter a positive integer: "))
    if a<=0:
        raise ValueError("this is not a positive number")
except ValueError as ve:
    print(ve)
#custom exception
class UnderAge(Exception):
    pass
def vage(age):
    if int(age)<18:
        raise UnderAge
    else:
        print("age: ",age)
vage(17)