''''r','w','a','x' '''
''''r+' --->opens a file for reading and writing,placing the pointer at
the beginning of the line
'w+' --> opens a file for writing and reading,previous content is removed
'a+' --> opens a file for appending and reading

a = open("day2.txt",'r+')
#print(a.read())
a.write("good day")
print(a.read())
a.close()

a = open('day2.txt','w+')
a.write('hello guys hope you are doing good')
#print(a.read())
a.close()

a = open('day2.txt','a+')
a.write("hello good evening")
#print(a.read())
a.close()


#a=open('final.xlsx','w')
#a.write("today")
#a.close()

a=open('final.xlsx')
print(a.read())'''

#print(25+26)

'''Python 3 supports a number of different ways of handling command line arguments
#The built-in way is to use the sys module,the other way is getopt

import sys
#count the arguments
arguments = len(sys.argv) #sys.argv is the simple list structure
#print(arguments)
#print(sys.argv)
if sys.argv[1] == 'halo':
    #write the program here when you want to give halo arg
    print("U have selected halo arg")
elif sys.argv[1] == "--version":
    print("my just 2.0")
elif sys.argv[1] == "train":
    print("Model training...")
elif sys.argv[1] == '--help':
    print("Help required give away your details")
elif sys.argv[1] == 'add':
    print(int(sys.argv[2]) + int(sys.argv[3]))
elif sys.argv[1] == 'boom':
    print(sys.argv[2])
print("The  Script is called with %i arguments"%(arguments))
print(sys.argv)


#getopt module goes a bit further and extends the separation of the input string
#by parameter validation

import getopt,sys
argv = sys.argv[1:]
try:
    opts,args = getopt.getopt(argv,'hm:d',['help','my_file='])
    print(opts)
    print(args)
except getopt.GetoptError:
    #print a message or do something useful
    print("Something went wrong")

#Using formatted string (often called fstring) literals:

r,l,b = 25,26,28
print(r)
print("{}".format(r))
print(f'{r}')
print(f"{r}")'''






