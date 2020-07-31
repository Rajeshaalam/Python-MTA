Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the first number:25
enter the second number:24
Success
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the first number:26
enter the second number:35
check the number again
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the first number:24
enter the second number:26
check the number again
enter the number:26
Even number
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the age:18
He cannot vote
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the age:18
Just got vote right
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the age:25
He can vote
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the age:10
He cannot vote
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the age:10
You need to wait 8 years to vote
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the age:10
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/day4script.py", line 50, in <module>
    print("You need to wait for another"+18-age+"years to vote")
TypeError: can only concatenate str (not "int") to str
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the age:10
You need to wait for another18-ageyears to vote
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the age:10
You need to wait for another8years to vote
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the number:25
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the number:5
Positive number
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the number:0
Negative number
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
enter the number:0
Zero
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
1
5
10
18
27
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
27
>>> 
================= RESTART: C:/Users/Name/Desktop/day4script.py =================
The sum is 27
>>> a = int(input(""))
25
>>> a
25
>>> a,b=int(input("enter the numbers"))
enter the numbers25
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a,b=int(input("enter the numbers"))
TypeError: cannot unpack non-iterable int object
>>> a,b=[int(x) for x in input("enter the values:")]
enter the values:15,25
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a,b=[int(x) for x in input("enter the values:")]
  File "<pyshell#3>", line 1, in <listcomp>
    a,b=[int(x) for x in input("enter the values:")]
ValueError: invalid literal for int() with base 10: ','
>>> a,b=[int(x) for x in input("enter the values:").split(',')]
enter the values:15,25
>>> a
15
>>> b
25
>>> a,b=(int(x) for x in input("enter the values:").split(','))
enter the values:15,25
>>> a
15
>>> b
25
>>> a=[int(x) for x in input("enter the values:").split(',')]
enter the values:15,25,1,6,7,8,9
>>> print(a)
[15, 25, 1, 6, 7, 8, 9]
>>> a
[15, 25, 1, 6, 7, 8, 9]
>>> a=[float(x) for i in input("enter the values:").split(',')]
enter the values:1.5,2,53,2.3
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a=[float(x) for i in input("enter the values:").split(',')]
  File "<pyshell#13>", line 1, in <listcomp>
    a=[float(x) for i in input("enter the values:").split(',')]
NameError: name 'x' is not defined
>>> a=[float(x) for x in input("enter the values:").split(',')]
enter the values:1.5,2.5,3.6,8
>>> a
[1.5, 2.5, 3.6, 8.0]
>>> type(a)
<class 'list'>
>>> a=(float(x) for i in input("enter the values:").split(','))
enter the values:1,5,2,6
>>> a
<generator object <genexpr> at 0x0000025C7F4F01C8>
>>> for i in a:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    for i in a:
  File "<pyshell#17>", line 1, in <genexpr>
    a=(float(x) for i in input("enter the values:").split(','))
NameError: name 'x' is not defined
>>> a=(float(x) for x in input("enter the values:").split(','))
enter the values:1,5,2,6
>>> a
<generator object <genexpr> at 0x0000025C7F532EC8>
>>> for i in a:
	print(i)

	
1.0
5.0
2.0
6.0
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
enter the values1,2,4,5,6
The sum is 18
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
<built-in method values of dict object at 0x000002F2F41B7728>
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
dict_values(['saketh', 26, 'vjwda'])
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
name
age
place
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
name age place 
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
name	age	place	
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
saketh	26	vjwda	
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
enter the range of value:10
1
3
6
10
15
21
28
36
45
55
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
enter the range of value:10
1 3 6 10 15 21 28 36 45 55 
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
enter the range of value:10
13610152128364555
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
enter the range of value:10
55 
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
enter the range of value:10
1 3 6 10 15 21 28 36 45 55 The sum is 55
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
enter the range of value:10
1
3
6
10
15
21
28
36
45
55
The sum is 55
>>> for i in 'saketh':
	print(i,end= ' ')

	
s a k e t h 
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
C
o
d
e
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
C o d e 
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
C o d e n a n 
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
1
2
3
4
5
6
7
8
9
10
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
6
7
8
9
10
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
6
7
8
9
10
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
1
2
3
4
5
6
7
8
9
10
-2 -5 -8 -9 
>>> 
=================== RESTART: C:/Users/Name/Desktop/day4script.py ==================
1
2
3
4
5
6
7
8
9
10
1 2 7 8 0 -2 -5 -8 -9 
>>> a ={1:'s',2:'p'}
>>> v = input("enter")
enter1
>>> v
'1'
>>> print(12,5)
12 5
>>> 'saketh'+'codegnan'
'sakethcodegnan'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 's'.__add__'a'
SyntaxError: invalid syntax
>>> 's'.__add__('a')
'sa'
>>> 22//7*2
6
.
>>> 1E10
10000000000.0
>>> bool
<class 'bool'>
>>> bool 0
SyntaxError: invalid syntax
>>> bool(0)
False
>>> bool('saketh')
True
>>> a = {}
>>> a.fromkeys(['a', 'b', 'c', 'd'], 98)
{'a': 98, 'b': 98, 'c': 98, 'd': 98}
>>> print(a)
{}
>>> 