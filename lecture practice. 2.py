Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
x = 25
y = 30
print(id(x))
4364137184
print(id(y))
4364137344
# int
x = 10
print("before:",id(x))
before: 4364136704
x = x+2
print("after:",id(x))
after: 4364136768
>>> # muteable list
>>> numbers = [1,2,3,4,5]
>>> print("before:",numbers)
before: [1, 2, 3, 4, 5]
>>> print("before id:",id(numbers))
before id: 4354217792
>>> numbers.append(4)
>>> print("after:",numbers)
after: [1, 2, 3, 4, 5, 4]
>>> print("after id:",id(numbers))
after id: 4354217792
>>> numbers.append(6)
>>> print("after:",numbers)
after: [1, 2, 3, 4, 5, 4, 6]
>>> print("after id:",id(numbers))
after id: 4354217792
>>> # mutable dictionary
>>> student = {
...     "name":"rajesh",
...     "age":20
...     }
>>> student ["age"] = 21
>>> print(student)
{'name': 'rajesh', 'age': 21}
>>> # string
>>> a_str = "hello world"
>>> print(a_str)
hello world
>>> print(a_str[0])
h
>>> print(a_str[0:5])
hello
>>> print(a_str[1:7])
ello w
>>> print(a_str[6:11])
world
>>> # set
>>> basket = {'apple','mango','banana','orange'}
>>> print(basket)
{'banana', 'apple', 'mango', 'orange'}
>>> basket = {'apple','mango','banana','orange','mango'}
>>> print(basket)
{'banana', 'apple', 'mango', 'orange'}
>>> a = set('hellomyname')
>>> print(a)
{'y', 'm', 'n', 'e', 'o', 'l', 'h', 'a'}
>>> b = set('my name is')
>>> print(b)
{'y', 'm', 'n', 'e', 's', 'a', 'i', ' '}
