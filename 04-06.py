#Abstraction in oop
#1.abc
from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Bow Bow")

d = Dog()
d.sound()

#Abstract class and method

from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

def sleep(self):
    print("Animal is sleeping")

#child class

class Dog(Animal):
    def sound(self):
        print("Dog Bow Bow")

class cat(Animal):
    def sound(self):
        print("Cat meow meow")

d = Dog()
d.sound()

#Abstract class and Methods

from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("animal is sleeping")

#child class

class Dog(Animal):

    def sound(self):
        print("Dog bow bow")

class Cat(Animal):
    def sound(self):
        print("Cat Meow")

d = Dog()
d.sound()
d.sleep()

c = Cat()
c.sound()
c.sleep()

#Abstract class shape with area()

from abc import ABC , abstractmethod
     @abstractmethod

     def area(self):
         pass

class Rectangle(shape):

    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

    class circle(shape):
        def __init__(self,radius)
        self.radius = radius

        def area(self):
            return 3.14*self.radius*self.radius

r = rectangle(10,5)
c = circle(10)

print("Rectangle area:" ,  r.area())
print("Circle area:" ,  c.area())

#Add perimeter() Method
#ML Module Abstract class

from abc import ABC , abstractmethod

class MLModule(ABC):
      @abstractmethod
      def train(self):
          pass

        @abstractmethod
        def predict(self):
            pass

#linear recreation model

class LinearRegressionModel(ML model):

    def train(self):
        print("predicting Linear Regression Model")

    def predict(self):
        print("Predicting using Linear Regression")

class DecisionTreeModel(ML Model):

    def train(self):
        print("Training Decision Tree Model")

    def predict(self):
        print("predicting using Decision Tree")

l = LinearRegression()
d = DecisionTreeModel()

l.train()
l.predict()

d.train()
d.predict()
