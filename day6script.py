#To create a function to find total and average

'''a = [int(x) for x in input("enter the values:").split(',')]
def cal(a):
    n = len(a)
    d = 0 #total
    for i in a:
        d=d+i #d+=i
        avg = d/n
    return d,avg
x,y=cal(a)
print("The Sum is:",x)
print("The average is:",y)

#Set Comprehension

a = {x for x in range(1,101) if x%2==0}
print(a)
print(type(a))

#Dictionary Comprehension

odd_squares = {x:x*x for x in range(1,101) if x%2!=0}
print(odd_squares)
print(type(odd_squares))


#Conversion of List Comprehension to tuple

b = tuple([(x,x**2,x**3)for x in range(10)])
print(b)


a = (x*x for x in range(11))
#b = list(a)
#print(b)
#print(type(a))
#for i in list(a):
#    print(i,end= ' ')

for i in a:
    print(i,end = ' ')

def a():
    #return "A","B","C"
    #return "B"
    #return "C"
    yield "A",25,63
    yield "B"
    yield "C"
#print(a())
d = a() #Assigning the function to a variable
for i in d:
    print(i)
print(next(d))
print(next(d))
print(next(d))
print(next(d))


#Properties of function

#Function is assigned to a variable

def add(a,b):
    return a+b
#print(add("Codegnan","Saketh"))
c = add(15,25)
print(c)
print(type(c))

#Function inside another function

def a():
    def b():
        return "Hello People"
    print(b())
    r = b() + "How are you"
    return r
print(a())

#Function as a parameter to another function
def a(d):
    return "Hello Codegnan" + str(d)
def b():
    return 25
print(a(b()))


#Function can return another function

def codegnan():
    def message():
        return "Tomorrow is a holiday"
    return message() + "Success"
s = codegnan()
print(s)

#Function can call itself -->Recursive Function 

#Factorial in a normal way

a = int(input("enter the value:"))
def factorial(a):
    d = 1
    for i in range(1,a+1):
        d = d*i
    return d
print(factorial(a))

x = int(input("enter the value:"))
def fact(x):
    if x == 1:
        return 1
    else:
        return x*fact(x-1)
print(fact(x))
    

#Function to compute the logic 3x+1

def f(x): #Function header
    return 3*x+1
print(f(5))

#Anonymous Function = Lambda expression
c = lambda x:3*x+1 #lambda argument(s) : expression
print(c(5))
print(c)
print(type(c))


#Lambda expression with multiple inputs : Social Media Registration (First name and last name)

#combine my first name and last name into "Full Name"

full_name = lambda fn,ln:fn.strip().title()+" "+ln.strip().title()
print(full_name("    sakethreddy","kallepu"))

#remove the missing data

countries = ["","India","USA","Brazil","UK","","","Chile"]
print(len(countries))
a=list(filter(None,countries))
print(a)

a=[int(x) for x in input("enter:").split(',')]
b = list(filter(lambda x:(x%2==0),a))
print(b)'''

i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2

if 1:

       print("huh?")

else:

        print("0 is falsy !")
