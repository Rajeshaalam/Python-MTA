Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #{} --> dictionary
>>> d = {'name':'saketh','place':"vjwda"}
>>> d
{'name': 'saketh', 'place': 'vjwda'}
>>> d['name']
'saketh'
>>> d.get('name')
'saketh'
>>> d.get('age')
>>> d['age']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d['age']
KeyError: 'age'
>>> d
{'name': 'saketh', 'place': 'vjwda'}
>>> d['name'] = 'codegnan'
>>> #Dictionaries are mutable
>>> d
{'name': 'codegnan', 'place': 'vjwda'}
>>> d['age'] = 2
>>> d
{'name': 'codegnan', 'place': 'vjwda', 'age': 2}
>>> d.update({'sno':1,'location':'moghalrajpuram','state':'ap'})
>>> print(d)
{'name': 'codegnan', 'place': 'vjwda', 'age': 2, 'sno': 1, 'location': 'moghalrajpuram', 'state': 'ap'}
>>> d
{'name': 'codegnan', 'place': 'vjwda', 'age': 2, 'sno': 1, 'location': 'moghalrajpuram', 'state': 'ap'}
>>> d.remove('name')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d.remove('name')
AttributeError: 'dict' object has no attribute 'remove'
>>> d.pop('name')
'codegnan'
>>> d.pop()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d
{'place': 'vjwda', 'age': 2, 'sno': 1, 'location': 'moghalrajpuram', 'state': 'ap'}
>>> d.popitem()
('state', 'ap')
>>> d
{'place': 'vjwda', 'age': 2, 'sno': 1, 'location': 'moghalrajpuram'}
>>> d.popitem()
('location', 'moghalrajpuram')
>>> d.clear()
>>> d
{}
>>> d[1] = 25
>>> d
{1: 25}
>>> del d
>>> d
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> d = {'name':'saketh','age':26,'place':'vjwda'}
>>> d.keys()
dict_keys(['name', 'age', 'place'])
>>> d.values()
dict_values(['saketh', 26, 'vjwda'])
>>> d.items()
dict_items([('name', 'saketh'), ('age', 26), ('place', 'vjwda')])
>>> e = d.copy()
>>> e
{'name': 'saketh', 'age': 26, 'place': 'vjwda'}
>>> d
{'name': 'saketh', 'age': 26, 'place': 'vjwda'}
>>> len(d)
3
>>> min(e)
'age'
>>> max(e)
'place'
>>> type(e)
<class 'dict'>
>>> e[2] = 45
>>> min(e)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    min(e)
TypeError: '<' not supported between instances of 'int' and 'str'
>>> e
{'name': 'saketh', 'age': 26, 'place': 'vjwda', 2: 45}
>>> e.setdefault(2,46)
45
>>> e.setdefault(3,45)
45
>>> e
{'name': 'saketh', 'age': 26, 'place': 'vjwda', 2: 45, 3: 45}
>>> d = [1,2,3,4]
>>> f = dict.fromkeys(d)
>>> f
{1: None, 2: None, 3: None, 4: None}
>>> f[1] = 25
>>> f
{1: 25, 2: None, 3: None, 4: None}
>>> #Data types [],(),{}
>>> 5+3
8
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> 'saketh'+'codegnan'
'sakethcodegnan'
>>> #Operators are the constructs which can manipulate the value of operands
>>> #Arithmetic operators +,-,*,/(float division),//(floor division),%(modulus),**(power)
>>> 5+3
8
>>> 5-3
2
>>> 5*3
15
>>> 5/3
1.6666666666666667
>>> 5 // 3
1
>>> 25 // 3
8
>>> 5 % 3
2
>>> 5 ** 3
125
>>> pow(5,3)
125
>>> pow(12,2)
144
>>> #Comparision operators(Relational operators)
>>> #decide the relation between the values or operands
>>> #==(equal to),!=,>,>=,<,<=
>>> 5 == 25
False
>>> a = 15;b = 25;c=a+b
>>> c == 40
True
>>> c != 45
True
>>> 5 < 25
True
>>> 15 < 0
False
>>> 15> -52
True
>>> [12,5,6] == [12,5,6]
True
>>> #Assignment operators
>>> # = ,+=,-=,*=,/=,**=
>>> a = 15
>>> b = 15
>>> a == b
True
>>> a+=10;print(a)
25
>>> #a+=10 --->a=a+10
>>> a-=10
>>> a
15
>>> a++
SyntaxError: invalid syntax
>>> a*=10
>>> a
150
>>> a/=5
a
>>> 
>>> a
30.0
>>> #Identity operators
>>> #is,is not
>>> 'saketh' is 'saketh'
True
>>> a = 45,b = 25;
SyntaxError: can't assign to literal
>>> a,b=45,25
>>> a=45;b=25
>>> 15 is 25
False
>>> [1,2,3] is [1,2,3]
False
>>> [1,2,3] == [1,2,3]
True
>>> [1,2,3] is not [1,2,3]
True
>>> #Memebership Operators
>>> #in , not in
>>> 1 in [1,2,3]
True
>>> 'dog' in 'dogs'
True
>>> 'saketh' in 'sakethreddycodegnan'
True
>>> 15 not in {1,2,5,6,15}
False
>>> #Bitwise opertors
>>> {1,2,5,6}  | {4,5,6,7}
{1, 2, 4, 5, 6, 7}
>>> 5|3
7
>>> #|-->Bitwise OR
>>> #&-->Bitwsie AND
>>> #^-->Bitwise XOR
>>> 5^3
6
>>> 5&3
1
>>> 5++1
6
>>> 5++
SyntaxError: invalid syntax
>>> 5<3
False
>>> 5 << 1
10
>>> #<< Bitwise left shift
>>> 5--1
6
>>> 5-1
4
>>> #Logicaloperators
>>> #and,or,not
>>> 5+3==8 and 25 < 26
True
>>> not1
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    not1
NameError: name 'not1' is not defined
>>> not 1
False
>>> not 0
True
>>> 5>3 or 25 in [1,2]
True
>>> 5 and 3
3
>>> 5 or 3
5
>>> 5 and []
[]
>>> 5 or []
5
>>> 5 | 3
7
>>> 0 and 5
0
>>> 0 or 25
25
>>> [] or {}
{}
>>> [] and {}
[]
>>> #(),**,+=,-=,/,*,..not,and,or -->operator precedence
>>> a+=25
>>> a
70
>>> not 25
False
>>> #>> Binary Right Shift
>>> 5 >> 1
2
>>> 5 >1
True
>>> print(a)
70
>>> a
70
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 25
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 25
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 26
25,26
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 26
25,26
25:26
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 26
25,26
25:26
25
26
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 26
25,26
25:26
25
26
25	26
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
hello everyone	
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
hello everyone
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
hello everyone
good evening	
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
hello everyone
good evening	
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
hello everyone
good evening	hey how are you
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
hello everyone
good evening hey how are you
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
hello everyone
good evening	hey how are you
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 26
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 26
You have entered 25 26 values
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 26
You have entered 25 26 values
25 26 are the values you have entered
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
25 26
You have entered 25 26 values
25 26 are the values you have entered
a= 25
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
a = 25,b=26.000000
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
a = 25,b=26.0
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
a = 25,b=26.0
a=26,b=25
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
a = 25,b=26.0
a=26,b=25
Hello Codegnan
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
a = 25,b=26.0
a=26,b=25
Hello Codegnan
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/dayy3script.py", line 34, in <module>
    print("Hello %c"%name)
TypeError: %c requires int or char
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
a = 25,b=26.0
a=26,b=25
Hello Codegnan
Hello C
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
a = 25,b=26.0
a=26,b=25
Hello Codegnan
Hello C
Hello             Codegnan
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
a = 25,b=26.0
a=26,b=25
Hello Codegnan
Hello C
Hello             Codegnan
15 25 26
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
a = 25,b=26.0
a=26,b=25
Hello Codegnan
Hello C
Hello             Codegnan
15 25 26
a=15,b=25,c=26
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 15
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/dayy3script.py", line 48, in <module>
    print("number1 = {2}".format(b))
IndexError: tuple index out of range
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
15,25,26
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
25,15,26
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
25,15,26
codegnan is in vijayawada
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
25,15,26
vijayawada is in codegnan
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
25,15,26
vijayawada is in codegnan
25
25
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
25,15,26
vijayawada is in codegnan
26
26
<class 'str'>
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
25,15,26
vijayawada is in codegnan
2.5
2.5
<class 'str'>
enter a number25
25
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
25,15,26
vijayawada is in codegnan
25
25
<class 'str'>
enter a number2.5
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/dayy3script.py", line 62, in <module>
    d = int(input("enter a number"))
ValueError: invalid literal for int() with base 10: '2.5'
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
number1 = 25
25,15,26
vijayawada is in codegnan
25
25
<class 'str'>
enter a number25
25
<class 'int'>
enter a number25
25.0
<class 'float'>
>>> 5+3
8
>>> 0.1+0.3
0.4
>>> 0.1+0.2
0.30000000000000004
>>> a= ['ab','cd']
>>> a.upper()
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> for i in a:
	i.upper()
	print(i)

	
'AB'
ab
'CD'
cd
>>> print(a)
['ab', 'cd']
>>> 
================== RESTART: C:/Users/Name/Desktop/dayy3script.py ==================
['ab', 'cd']
>>> type(5)
<class 'int'>
>>> type(int)
<class 'type'>
>>> type(type(int))
<class 'type'>
>>> print('abcdef'.replace('ab'25))
SyntaxError: invalid syntax
>>> print('abcdef'.replace('ab',25))
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    print('abcdef'.replace('ab',25))
TypeError: replace() argument 2 must be str, not int
>>> print('abcdef'.replace('ab','25'))
25cdef
>>> print('abcefd'.replace('cd','12'))
abcefd
>>> bin(10-2)
'0b1000'
>>> 10^2
8
>>> 