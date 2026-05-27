# String Formating

name = "Jiya"
age = 18

# using f-string

print(f"My name is {name} and i am {age} years old.")

#using .format()

print("My name is {} and i am {} years old." .format(name , age))

#using %formatting

print("My name is %s and i am %d years old." %(name, age))

price = 199.456

print(f'"Price:{price: .2f}")

# List and Tuple (Mutability)
# list

my_list = [10 , 20 , 30]

print("original list:" , my_list)

my_list[1] = 200

print("Modified list:" , my_list)

#append()

my_list.append(50)
my_list.append(60)

print("After remove list :" , my_list)

#tuple - immutable

my_tuple = (10 , 20 ,30 ,40)

print("Tuple : " , my_tuple)

# Access Element

print("Frist Tuple Element :" , my_tuple[1])

# Indexing and slicing

text = "python"

# indexing

print("First letter:" , text[0])
print("Last letter:" , text[len(text) - 1])
print("last letter:" , text[-1])

#slicing

print("First 3 letters:" , text[0:3])
print("Last 3 letters:" , text[3:1])
print("Last 3 letters:" , text[-3:])

#reverse string

print("Reverse String:" , text[::-1])

#Using List with slicing and formating

students = ["Dixit" , "Jinal" , "Raj" , "Janvi" , "Jiya" ,"Rutva"]

print("\noriginal List:" , students)

print("\nFrist three students:" , students[:3])

#loop

for student in students:
      print("welcome , {student}")

#length

print("Length of List:" , len(students))

#checking element

print("Is Jiya Present?:" , "Jiya" in students)

#Nested list

matrix = [
             [1 , 2 , 3],
             [4 , 5 , 6],
             [7 , 8 , 9]
             ]
print("Matrix :" , matrix)

#Accessing element

print("Middle element:" , matrix[1][1])

#string method

message = "python programming"

print("Uppercase:" , message.upper())
print("Capitalized:" , message.capitalize())
print("Replace:" , message.replace("python" , "AI/ML"))
print("Split:" , message.split())

# list method

numbers = [5 , 8 , 2 , 7 , 1]

numbers.sort()

print("Sorted List:" , numbers)

numbers.reverse()

print("Reverse List:" , numbers)

numbers.insert(1 , 100)

print("After insesrt:" , numbers)
