Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Strings
>>> #Indexing and Slicing part
>>> c = 'codegnan'
>>> c[0] = 2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c[0] = 2
TypeError: 'str' object does not support item assignment
>>> c+'saketh'
'codegnansaketh'
>>> c * 2
'codegnancodegnan'
>>> c ** 2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    c ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> len(c)
8
>>> c - 'saketh'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c - 'saketh'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> c
'codegnan'
>>> #Conversions
>>> c.upper()
'CODEGNAN'
>>> c.lower()
'codegnan'
>>> c.capitalize()
'Codegnan'
>>> c
'codegnan'
>>> c.swapcase()
'CODEGNAN'
>>> c = 'cOdeGnan'
>>> c.swapcase()
'CoDEgNAN'
>>> #Content test functions
>>> c.isalpha()
True
>>> c.isdigit()
False
>>> c.isupper()
False
>>> c.islower()
False
>>> #isupper() -->checks if all the characters are uppercase alphabets
>>> c.isalnum()
True
>>> c.startswith()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c.startswith()
TypeError: startswith() takes at least 1 argument (0 given)
>>> c.startswith('c')
True
>>> c.startswith('C')
False
>>> c.endswith('n')
True
>>> c
'cOdeGnan'
>>> c[2]
'd'
>>> c.index('d')
2
>>> c.index('Z')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c.index('Z')
ValueError: substring not found
>>> c.index('n')
5
>>> c.count('n')
2
>>> c = '  codegnan'
>>> c
'  codegnan'
>>> len(c)
10
>>> c.strip()
'codegnan'
>>> d = c.strip()
>>> c
'  codegnan'
>>> d
'codegnan'
>>> len(c)
10
>>> len(d)
8
>>> c.find('n')
7
>>> c.find('g')
6
>>> d
'codegnan'
>>> d.find('n')
5
>>> d.replace('n','s')
'codegsas'
>>> #Container is an enitity 