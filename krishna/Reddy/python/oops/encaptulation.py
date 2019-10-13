class Dreamwin:
    def __init__(self):
        self.a = 10 # public variable
        self._b = 20 # protected variable
        self.__c = 30 # private variable
obj = Dreamwin()
print(obj.a)
print(obj._b)
print(obj._Dreamwin__c)
