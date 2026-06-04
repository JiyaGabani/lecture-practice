#OOP
#1.class and object
#student class

class Student:
    def __init__(self ,name ,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name : " , self.name)
        print("Age : " , self.age)

#creating object
            
s1 = student("vivek",26)
s2 = student("rahul",20)

print(s1)

s1.display()
s2.display()

#self keyword
#Employee
class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Employee Name:",self.name)
        print("Salary:",self.salary)
    
e1 = Employee("rahul",50000)
e1.show()

#del keyword

x=100
del x
print(x)

#student

class student:
    
    def __init__(self):
        self.name = "jiya"

s1 = student()
del s1
print(s1.name)
del s1.name



#Encapsulation
#Bank Acount

class BankAccount:
    def __init__(self):
        self.__balance = 100000
    def deposite(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        self.__balance -= amount
    def get_balance(self):
        return self.__balance

acc1 = BankAccount()
acc1.deposite(50000)
acc1.withdraw(10000)
print("Account Balance:",acc1.get_balancee())

#Polymophism
#Method overriding

class Animal:
    
    def sound(self):
        print("Animal make sound")
        
class Dog(Animal):
    
    def sound(self):
        print("Dog Bhow Bhow")

class Snack(Animal):
    
    def sound(self):
        print("Snack sheeeeeeee.....")

d = Dog()
s = Snack()

d.sound()
s.sound()

#same function diffrent object

class Car:
    
    def move(self):
        print("car is running")

class Plane:
    
    def move(self):
        print("plan is flying")

def action(vehical):
    vehical.move()
    
c = Car()
p = Plane()

action(c)
action(p)

#Abstraction
#Vehical

class vehical():
    
    def start(self):
        pass

class Car(vehical):
    
    def start(self):
        print("Car started")

class Bike(vehical):
    
    def start(self):
        print("Bike started")

c = Car()
b = Bike()

c.start()
b.start()

#Inheritance
#1.Single inheritance

class parent:
    def show(self):
        print("parent Class")

class child(parent):
    pass

c = child()

c.show()

#Multi-level inheritance

class Grandparent:
    def title(self):
        print("Grand parent")

class parent(Grandparent):
    def title1(self):
        print("parent")

class child(parent):
    def title2(self):
        print("child")

obj = child()
obj.title()
obj.title1()
obj.title2()


#Multipe Inheritance

class Father:
    def father_property(self):
        print("car")

class Mother:
    def mother_property(self):
        print("jwellery")

class child(Father,Mother):
    pass

c = child()
c.father_property()
c.mother_property()

#Hierarchiccal Inheritance

class parent:
    def display(self):
        print("parent class")

class child1(parent):
    pass
class child2(parent):
    pass

c1 = child1()
c2 = child2()

c1.display()
c2.display()

#Hybrid Inheritane

class A:
    
    def showA(self):
        print("A class")

class B(A):
    
    def showB(self):
        print("B class")

class C(A):
    
    def showC(self):
        print("C Class")

class D(B,C):
    
    def showD(self):
        print("D class")

obj = D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()


