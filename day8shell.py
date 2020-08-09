Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
1596541622.7987375
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
1596541653.1497033
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
1596541827.2151358
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
1596542037.758703
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 0.543673038482666 seconds for the execution:
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
0
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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
0.8764195442199707 seconds for the execution:
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
0
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
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
1.767181396484375 seconds for the execution:
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
1596542515.1911786
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=4, tm_hour=17, tm_min=33, tm_sec=14, tm_wday=1, tm_yday=217, tm_isdst=0)
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=4, tm_hour=17, tm_min=34, tm_sec=1, tm_wday=1, tm_yday=217, tm_isdst=0)
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=4, tm_hour=17, tm_min=34, tm_sec=29, tm_wday=1, tm_yday=217, tm_isdst=0)
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
4 8 2020
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
Today is 4-8-2020
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
Today is 4-8-2020
Time now is 17:38
>>> 
================= RESTART: C:/Users/Name/Desktop/day8script.py =================
Tue Aug  4 17:41:55 2020
>>> import time
>>> a = time.ctime()
>>> a
'Tue Aug  4 17:42:11 2020'
>>> import datetime
>>> a = datetime.now()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = datetime.now()
AttributeError: module 'datetime' has no attribute 'now'
>>> from datetime import *
>>> a = datetime.now()
>>> a
datetime.datetime(2020, 8, 4, 17, 46, 17, 862400)
>>> print(a)
2020-08-04 17:46:17.862400
>>> a.day
4
>>> a.year
2020
>>> a.month
8
>>> a.hour
17
>>> a.minnute
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.minnute
AttributeError: 'datetime.datetime' object has no attribute 'minnute'
>>> a.minute
46
'
>>> a = datetime.now()
>>> a.day
4
>>> a.month
8
>>> a.year
2020
>>> a.hour
17
>>> a.minute
48
>>> print("Today date is {}-{}-{}".format(a.day,a.month,a.year))
Today date is 4-8-2020
>>> d = datetime.today()
>>> d
datetime.datetime(2020, 8, 4, 17, 52, 28, 162602)
>>> print(d)
2020-08-04 17:52:28.162602
>>> d = date.today()
>>> d
datetime.date(2020, 8, 4)
>>> print(d)
2020-08-04
>>> #combining date and time
>>> d = date(1993,12,26)
>>> d
datetime.date(1993, 12, 26)
>>> print(d)
1993-12-26
>>> t = time(6,45)
>>> t
datetime.time(6, 45)
>>> dt = datetime.combine(d,t)
>>> dt
datetime.datetime(1993, 12, 26, 6, 45)
>>> print(dt)
1993-12-26 06:45:00
>>> #Replacing date and time
>>> d1=datetime(year=2020,month = 12,day = 26,hour = 11,minute = 25,second = 45)
>>> d1
datetime.datetime(2020, 12, 26, 11, 25, 45)
>>> d2=d1.replace(year=2020,month = 07)
SyntaxError: invalid token
>>> d2=d1.replace(year=2020,month = 7)
>>> d2
datetime.datetime(2020, 7, 26, 11, 25, 45)
>>> print(d2)
2020-07-26 11:25:45
>>> #Formatting date and time
>>> #strftime
>>> e = date.today()
>>> e
datetime.date(2020, 8, 4)
>>> s = e.strftime()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s = e.strftime()
TypeError: strftime() missing required argument 'format' (pos 1)
>>> s = e.strftime("%d-%b-%y")
>>> s
'04-Aug-20'
>>> s = e.strftime("%D-%B-%Y")
>>> s
'08/04/20-August-2020'
>>> s = e.strftime("%D/%B/%Y")
>>> s
'08/04/20/August/2020'
>>> t=e.strftime("%a")
>>> t
'Tue'
>>> t=e.strftime("%A")
>>> t
'Tuesday'
>>> #strptime -->input string output datetime
>>> value = "26 December 1993"
>>> s = datetime.strptime(value,"%d %B %Y")
>>> s
datetime.datetime(1993, 12, 26, 0, 0)
>>> print(s)
1993-12-26 00:00:00
>>> #check cases
>>> d,m,y=[int(x) for x in input("enter the date:").split('-')]
enter the date:6-8-2020
>>> #store them in date object
>>> g = date(y,m,d)
>>> print(g)
2020-08-06
>>> print(g.strftime("The day is %A and it is %w day of the week"))
The day is Thursday and it is 4 day of the week
>>> #calendar module
>>> from calendar import *
>>> y = int(input("enter the year:"))
enter the year:2020
>>> if isleap(y):
	print(y,"is a leap year")

	
2020 is a leap year
>>> m = int(input("enter the month:"))
enter the month:8
>>> d = month(y,m)
>>> print(d)
    August 2020
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31

>>> print(calendar(y))
                                  2020

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                         1
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8
13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15
20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22
27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29
                                                    30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
27 28 29 30               25 26 27 28 29 30 31      29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2          1  2  3  4  5  6
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
                          31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1          1  2  3  4  5  6
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
                          30

>>> import random
>>> a = random.random()
>>> a
0.7749723548779691
>>> a = random.random()
>>> 
>>> a
0.9266782719687607
>>> a = random.random()
>>> a
0.00035266692952629075
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
0.8852985927371381
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
0.7848583111735563
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
0.6375864404364577
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
0.45749012374852693
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
0.3597231454306703
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
0.13240794868330752
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
10
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
10
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
12
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
11
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
12
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
10
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
13
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
14
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
12
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
15
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
14
16
13
16
10
11
>>> import random
>>> random.randrange(1,10)
6
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
1912
1301
8357
5591
2871
9088
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
7891
3631
7056
8453
8797
7496
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/day8script.py", line 44, in <module>
    a.write(d)
TypeError: write() argument must be str, not list
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/day8script.py", line 46, in <module>
    a.write(d)
TypeError: write() argument must be str, not list
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/day8script.py", line 46, in <module>
    a.writelines(d)
TypeError: write() argument must be str, not int
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
Traceback (most recent call last):
  File "C:/Users/Name/Desktop/day8script.py", line 49, in <module>
    w= open('there.txt','x')
FileExistsError: [Errno 17] File exists: 'there.txt'
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
>>> 
=================== RESTART: C:/Users/Name/Desktop/day8script.py ==================
hellohello
hello today
>>> 