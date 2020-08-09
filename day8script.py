import time
'''start = time.time()#initiate
#print(start)
for i in range(100):
    print(i,end='\n')
time.sleep(1)
end = time.time()
print("{} seconds for the execution:".format(end-start))

epoch = time.time()
#print(epoch)
t= time.localtime(epoch)
#print(t)
d= t.tm_mday
m = t.tm_mon
y = t.tm_year
print("Today is %d-%d-%d"%(d,m,y))
h = t.tm_hour
m = t.tm_min
print("Time now is %d:%d"%(h,m))

t = time.ctime()
print(t)

import random
#a = random.random()
#v = random.randint(10,15)
#print(v)
from random import randint,randrange
for i in range(6):
    #print(randint(10,16))
    print(randrange(1000,9999))'''

'''All program files are text files
All images,music,video,executable files are binary files

File I/O Operations
--Open a file
--read/write data into it
--close

a = open("sund.txt",'w')
d = ["Saketh\n","Codegnan"]
e = "I work in Codegnan"
#a.write(str(d))  #Type conversion
a.writelines(d)
a.close()

w= open('there.txt','x')
w.write("hello")
w.close()

w= open('there.txt','a')
w.write("\nhello today")
w.close()'''

d = open("there.txt")
print(d.read())






