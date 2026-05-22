#simple calculator
num1=10
num2=5

operator="+"

match operator:
    case "+":
        print("addition",num1+num2)
    case "-":
        print("subtaction",num1-num2)
    case "*":
        print("multiplication",num1*num2)
    case "/":
        print("devision",num1/num2)
    case _:
        print("invaild operator")

#python loop
#while loop
i=1
while i<=5:
    print(i)
    i+=1

#for loop
#print number 1 to 5
for i in range (1,6):
    print(i)

#loop with string
name="python"
for i in name:
    print(i)

#loop with list
fruits=["apple","mango","banana","gavava"]
for i in fruits:
    print(i)

#range function
for i in range(5):
    print(i)
    
for i  in range(1,10):
    print(i)
for i in range(0,10,2):
    print(i)

#neseted loops
for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()
