#check if a number is even or odd
num=int(input("enter a number:"))
if num%2==0:
    print(f"{num} is an even number:")
else:
    print(f"{num} is an odd number:")

# find minimum of two number
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
if num<num2:
    print(f"the minimum number is{num1}")
else:
    print(f"the maximum number is{num2}")

#find largest of three number
num1=int(input("enter a first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter a third number:"))
if num1>=num2 and num1>=num3:
    print(f"the largest number is {num1}")
elif num2>=num1 and num2>=num3:
    print(f"the largest number is {num2}")
else:
    print(f"the largest number is {num3}")

#identity opreator
a=[1,2]
b=a
c=[1,2]
print(a is b)
print(b is c)
print(c is not a)

#membership opreator
numbers=[1,2,3,4]
print(2 in numbers)
print(5 in numbers)
print(5 not in numbers)

#bitwise opreator
#bitwise AND
a=5
b=3
print(a&b)
#bitwise XOR
a=5
b=3
print(a^b)

#python control flow
#if condition
age=18
if age>=18:
    print("you are eligible to vote")
#if....else condition
number=7
if number%2==0:
    print("even")
else:
    print("odd")
#if...elif...else statment
marks=70
if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>50:
    print("grade C")
else:
    print("Fail")
