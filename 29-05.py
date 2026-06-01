#Built-in function
#UDF Function

def prints():
    print("welcom Students!")

prints()

def multi(a , b):
    print("Multiplication: " , a * b)

multi(4 , 5)

#fectorial , fibonacci , tree structure , problem sloving

def factorial(n):

    if (n==1):
        return 1

    return n * factorial(n - 1)

print(factorial(5))

#2. sum of two number

def total(n):

    if n == 0:
        return 0

    return n + total(n-1)

print(total(5))

# Annonymous

square = lambda x : x * x

print(square(5))

add = lambda a , b : a + b

print(add(10 , 20))

# list

numbers = [1 , 2 , 3 , 4 , 5]

result = list(map(lambda x : x* 2 , numbers))

print(result)

# filter

numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

odd = list(filter(lambda x : x % 2 != 0 , numbers))

print(odd)

# Global keyword

x = 10

def show():
    print(x)
    
show()

count = 0

def increment():
    global count
    count += 1

increment()
increment()
increment()

print(count)

#single value
#multiple value

def calculation(a,b):

    return a+b,a-b

result = calculation(20 , 5)

print(result)

def student():

    name="Alica"
    marks=90

    return name,marks

n , m = student()

print(m)
print(n)

#built-in function

numbers=[1,2,3,4,5]

print("Length:" , len(numbers))
print("Maximum:", max(numbers))
print("Minimum:" , min(numbers))

#User define function

def greet(name):
    return "hello" + name

print(greet("student"))

#Arbitray Argument

def add_number(*args):
    total = 0

    for num in args:
        total += num
    return total

print(add_number(1 , 2 , 3 , 4 , 5))

#doc (Documentation String)

def multiply(a ,b):
    return a * b
print(multiply(4 , 5))
print(multiply.__doc__)

#1. TNRN

def greet():
    print("hello, python student")

greet()

#2. TSRN

def add(a,b):
    print("Addition :" , a+ b)

add(10 , 20)

#3. TNRS

def message():
    return "hello student"

print(message())

# TSRS function

def multiply(a , b):
    return a * b

result = multiply(4 , 7)

print(result)
