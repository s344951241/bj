#!/user/bin/python3

class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'

#实力化类
x = MyClass()


print("myclass i:",x.i)
print("myclass f:",x.f())


class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t=Test()
t.prt()

class people:
    name = ''
    age = 0

    __weight = 0#私有
    def __init__(self,n,a,w):
        self.name = n
        self.age= a
        self.__wight = w

    def speak(self):
        print("%s说：我%d岁" %(self.name,self.age))

p = people('runoob',10,30)
p.speak()

    
