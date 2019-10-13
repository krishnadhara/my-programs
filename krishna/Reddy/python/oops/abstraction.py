from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def say_something(self):
        pass
class Cat(Animal):
    def say_something(self):
        return "Miauuu!"
a = Cat()
print(a.say_something())


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass
class Concrete(Base):
    def foo(self):
        pass
    def bar(self):
        print("bar")
c = Concrete()
c.bar()