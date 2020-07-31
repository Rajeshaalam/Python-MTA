'''Programming flow can be controlled using:
-->Decision Control Instruction
-->Repetition Control Instruction

--->if,else,elif

if(test_expression):
    statements...
    ......

a = 25;b = 36
if a>b:
    print("Success")

else:
    statements ...
    ....
a=int(input("enter the first number:"))
b = int(input("enter the second number:"))
if a>b:
    print("Success")
else:
    print("check the number again")


#To check whether the given number is even or odd by taking user input

a = int(input("enter the number:"))
if a%2==0:
    print("Even number")
else:
    print("Odd number")


#Another check case
elif (test condition):
    statements....
    ....

#To check whether the person is eligible to vote or not in India

age = int(input("enter the age:"))
if age>18:
    print("He can vote")
elif age==18:
    print("Just got vote right")
else:
    #print("He cannot vote")
    #print("You need to wait for another",18-age,"years to vote")
    print("You need to wait for another"+str(18-age)+"years to vote")


#Nested conditions
a = int(input("enter the number:"))
if a>=0:
    if a==0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")'''

#Repetition Control Instruction(Loops)
#for,while

'''Syntax:
for val in sequene:
    body of for...
    .....

#a = [1,4,5,8,9]
a = [int(x) for x in input("enter the values").split(',')]
#variable to store the sum
d = 0
#start iterating over the list
for j in a:
    d = j+d #d+=j
#print(d)
print("The sum is %d"%d)

a = {'name':'saketh','age':26,'place':'vjwda'}
#print(a.values())
for i in a.values():
    print(i,end='\t')'''

#while loop as long as the condition is true

'''Syntax
while test_expression:
     Body of while

#To find the sum of natural numbers 1+2+3+...n

n = int(input("enter the range of value:"))
#to initialize the variable storing the sum and counter
s = 0
i =1 #counter
while i<=n:
    s = s+i
    i+=1
    print(s,end= '\n')
print("The sum is {}".format(s))'''

#break and continue

#alter the flow of loop (for,while)

'''for i in 'Codegnan':
    if i == 'g':
        #break
        continue
    print(i,end=' ')'''

#pass statement is used syntactically

a = 0
while a<10:
    a+=1
    if a>5:
        pass
    print(a)

    
a = [1,2,7,8,0,-2,-5,-8,-9]
for i in a:
    if i>=0:
        #print(i,end=' ')
        pass 
    else:
        print(i,end=' ')






    
    
    



