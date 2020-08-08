#assert statement is used to specify or check whether the given condition
#is fulfilled or not

#syntax for assert

#assert expression,message

#try block : Enclose in it the code that you anticipate will cause an exception

#except:catch the raised exception 

'''a = int(input("enter the number greater than 0:"))
try:
    assert a>0,"Number should be greater than zero"
    print(a)
except AssertionError:
    print("Check the input number you have passed")
finally:
    print("Happy Ending")
    print(25+26)


try:
    a = int(input("enter an integer"))
    b = int(input("enter an integer"))
    c = a/b #floating division
    print("The value of c=",c)
except ZeroDivisionError:
    print("Denominator is 0")
except ValueError:
    print("Unable to convert string(float) to int")
finally:
    print("Its done")

#A Function is similar to a program that consists group of statements that are
#intended to solve a specific task

#syntax
def name(parameters):
    #doc string (description of the function)
    statement(s)

def saketh(a,b):
    #add function or combining
    c=a+b
    #return c;
    print(c)
print(saketh(15,25))
print(saketh([1,5,2,3],[4,5,6,7]))
print('saketh','codegnan')
  

#positional arguments or required arguments
def it(a,b='gnan'):#default arguments
    return a+b
print(25+29+369)
print(it('saketh','police'))#positional arguments

#keyword arguments
def codegnan(course,price):
    print("Course is %s"%course)
    print("Price is %.1f"%price)
codegnan("Data Science",29500)
#codegnan(29500,"Data Science")
codegnan(price=29500,course = "DS")


#variable length arguments

def addition(a,*b):
    d = 0
    for i in b:
        d=d+i
    #print(d+a)
    return d+a
print("Addition result is",addition(1,2,3,4,5,6))


a =int(input("enter the number:"))
b =[int(x) for x in input("enter the values:").split(',')]
print(b)
print(type(b))
def add(a,*b):
    d=0
    for i in b:
        d+=i
    return d+a
print(add(a,*b))

#Unpacking arguments
def code(a,b,c,d,e):
    print(a,b,c,d,e)
#code(1,23.6,5,8,9)
d = [1,4.5,2,'saketh',25]
code(*d)
for i in d:
    print(i,end= ' ')

#keyword variable length arguments : '**'

def gnan(name = 'Saketh',marks = 95):
    print(name,marks)
#gnan('Code',25)
d = {'name':'Saikiran','marks':55}
gnan(*d) #*args
gnan(**d) #**kwargs

def vjwda(a,**b):
    print(type(b))
    for c,d in b.items():
        print("key = {},value={}".format(c,d))
vjwda(1,name='Saketh',work='Codegnan')
vjwda(2,name='Codegnan',place='Vijayawada')

#global variables are the one that are defined and declared above a function

a = "Python" #global variable
def myfunction(): #function header
    b=25 #local variable
    b+=35
    print(b)
    global a
    #a = "Saketh"
    print(a)
    a=25
    print(a+b)
myfunction()
#print(b)
print(a)'''
    

#List Comprehension

#lst = [expression for item in sequence[optional for and/or if]]

a = [x*x for x in range(1,11)]
print(a)


for i in range(0,11):
    print(i*i,end= ' ')

a = [1,4,5,25,26,28,35,45,50,52,89]
a = [num for num in a if num>20 and num<50]
print(a)





