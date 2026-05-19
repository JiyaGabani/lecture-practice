Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #number datatype
>>> int_num=10
>>> float_num=10.2
>>> print(int_num)
10
>>> print(float_num)
10.2
>>> #list datatype
>>> list=[123,"abcd",10.2,"T"]
>>> print(list)
[123, 'abcd', 10.2, 'T']
>>> list1=["hello","world"]
>>> print(list1)
['hello', 'world']
>>> print(list[0:1])
[123]
>>> print(list1*2)
['hello', 'world', 'hello', 'world']
>>> print(list+list1)
[123, 'abcd', 10.2, 'T', 'hello', 'world']
>>> #dictionary datatype
>>> dic={'name':'red','age':17}
>>> print(dic)
{'name': 'red', 'age': 17}
>>> print(dic["name"])
red
>>> print(dic.values())
dict_values(['red', 17])
>>> print(dic.keys())
dict_keys(['name', 'age'])
>>> #tuple datatype
>>> tuple=(123,"hello",true)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    tuple=(123,"hello",true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> tuple=(123,"hello")
>>> print(tuple)
(123, 'hello')
>>> print(tuple[0])
123
>>> tuple1=("world")
>>> print(tuple1)
world
