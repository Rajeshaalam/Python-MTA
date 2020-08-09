'''a = [1,4,5,6,7]
b = [3,5,7,8,25]
c = list(map(lambda x,y:x*y,a,b))
print(c)

a = list(map(float,input("enter the values:").split(',')))
print(a)

a,b = map(int,input("enter the values:").split(','))
print(a,b,sep=',')'''

#Logical errors should be modified by programmer

def increment(sal):
    sal = sal+sal*15/100
    return sal
print(increment(45000))
    
