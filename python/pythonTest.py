#!/user/bin/python
# -*- coding:UTF-8 -*-
import os
import nester

print("你好")


print(isinstance(10,int))

a =1
b= a
a =2
print(b)

A = [1,2,3]
B = [1,2,A]
A[2] = 2
print(B)


def func(name):
    print(name)

fun = func

fun("vv")

f = lambda name:"lambda:"+name
result = f("vv")

li = [1,2,3,[4,5,6,7]]
nester.print_lol(li,2)


try:
    f = open('file.txt')
    s = f.readline()
except:
    print("error")


class MyClass:
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()

print(x.i)
print(x.f())

class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0,-4.5)
print(x.r,x.i)

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()


class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age =a
        self.__weight = w
    def speak(self):
        print("%s 说:我%d岁"%(self.name,self.age))

p = people('runoob',10,30)
p.speak()

class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print("%s 说：我%d岁了，我在读%d年纪"%(self.name,self.age,self.grade))

s = student("ken",10,60,3)
s.speak()

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫%s，我是一个演说家，我演说%s"%(self.name,self.topic))

speak = speaker('vv','dsfdf')
speak.speak()
