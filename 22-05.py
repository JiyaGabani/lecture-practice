#break statement
for i in range(1,7):
    if i==4:
        break
    print(i)

#continue statement
for i in range(1,7):
    if i==4:
        continue
    print(i)

#pass statment
for i in range(1,7):
    if i==4:
        pass
    print(i)

#pattern in pythonh
#right angled tringle
    
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

#number tringle

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

#inverted tringle

for i in range(6,0,-1):
    for j in range(i):
        print(*,end=" ")
    print()

#pyramid pattern

row=5
for i in range(1,row+1):
    for j in raange(row-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

#else with loops

for i in range(5):
    print(i)
else:
    print("loop finished")

#break

for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("loop finished.")

#list and tuple

my_list=[10,20,30,40]
print("original list:",my_list)
my_list[0]=50
print("modified list:",my_list)

#tuple in python

"""
my_tuple=(10,20,30)
print("tuple:",my_tuple)
my_tuple[0]=50
"""
        


    
