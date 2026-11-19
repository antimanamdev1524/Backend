#STRING

"""
String is a data type that stores a sequence of characters.
"""


#Program_1:
"""
str1 = "string can be written as double quote"
str2 = 'string can be written as single quote'
str3 = '''string can be written as triple quote'''

print(str1)
print(str2)
print(str3)
"""

#Program_2:
"""
str= 'Welcome \t This is a Topic. \n learning from apna college'
print(str) 
""" 

####################..............####################


#ESCAPE SEQUENCE:
# \n =  new line
# \t = horizontal space or tab space

"""
BASIC OPERATIONS

1) Concatenation
    "Hello" + "_World" ----->  "Hello_World"

2) Length of str
    len(str)

"""

####################..............####################


#Concatenation

#Program_3:
"""
str1 = "Top" 
str2 = '_Technology'

print("String Concatenation: ", str1 + str2)
"""
#Program_4:

"""
string= str1 + str2
print("String concatenation: ", string)
"""

####################..............####################


#Length of string
#len(str) is generally used to count string length.

#Program_5:

"""
a= 'TOP'
len= len(a)
print(len)
"""

#Program_6:
"""
x= 'Full Stack'

y= ' Developer'

print(len(x + y), x+y)   # 20 Full Stack Developer

print("length of",x+y ,"is", len(x+y))   # length of Full Stack Developer is 20 
"""

####################..............####################


#INDEXING

"""
 Indexing refers to 
 the process of accessing a specific element in a sequence, 
 such as a string or list, 
 using its position or index number. 
 Indexing in Python starts at 0, 
 which means that 
 the first element in a sequence has an index of 0, 
 the second element has an index of 1, and so on.

     A P N A _ C O L L E G E
     0 1 2 3 4 5 6 7 8 9 10 11

     str = "APNA_COLLEGE"

     str[0] = A
     str[5] = C


     Index is used to access the character directly
     Only can be access the character, can't be modify

"""

#Program_6:
"""
str = "top tech"
ch = str[0]
print(ch)               #t
"""

#Program_7:
"""
str= 'top _technology'
print(str[5])           #e

print(str[3])           #_
"""

####################..............####################

#Slicing
"""
=> Slicing refers to Accessing the part of a string
=> Divide a program into small part

There are two types of slicing 
1) Positive slicing  ==> string[start : end : increment]
2) Negative slicing  ==> string[start : end : decrement]

str[starting_idx : ending_idx]    #ending idx is not included

str= "Apna College"

str[1:4]    #pna

str[ :4] is same as str[0:4]        #Apna 
                                    #here starting is not provided means start from zero.... 
                         

str[1: ] is same as str[1: len(str)]    #pna College
                                        #here ending is not provided means end will be highest index number... 

"""

#Slicing ==> str[starting_idx : ending_idx]    #ending idx is not included

#Program_8:
"""
str = "Apna College"
print(str[1:4])                #pna
print(str[ :4])                #Apna
print(str[1: ])                #pna College
print(str[0: len(str)])        #Apna College
"""

#Positive slicing ==> string[start : end : increment]

#Program_9:
"""
s= "Python_Developer"
print(s[0 : 12 : 1])         #Python_Devel
print(s[3 : 8 : 2])          #hnD
print(s[3 : 13 : 2])         #hnDvl
print(s[2: 14: 2])           #to_eeo
print(s[ : : 1])             #Python_Developer
print(s[2 : : 4])            #t_ee
"""

#Negative slicing ==> string[start : end : decrement]
"""
negative index starts from bottom to top
 A  P  P  L  E
-5 -4 -3 -2 -1

str = "Apple"
str[-3 : -1]       #pl
"""

#Program_10:
"""
s= "apple"
print(s[-5: -2])  #app index -2  will be drop here
"""

"""
s= "Python_Programmer"
#   P   y   t   h   o   n   _   P  r  o  g  r  a  m  m  e  r
# -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(s[-13 : -3 : 1])           #on_Program
print(s[-15 : -5 : 3])           #tnrr
print(s[-12 : : 3])              #nrrm
print(s[ : : -1])                #remmargorP_nohtyP
print(s[ : -2 : 4])              #Pora
print(s[-11 : -2 : 2])           #_rgam
"""

####################..............####################

#String Function
"""
str = "I am a coder."

print(str.endswith("er."))           #returns true if string ends with substr
print(str.capitalize())              #capitalizes 1st char         
print(str.replace(old, new))         #replaces all occurrences of old
print(str.find(word))                #returns 1st index of 1st occurrer
print(str.count("am"))               #counts the occurrence of substring
"""

#Program_11:
"""
s = "I am styding Full Stack Course From top Technology"
str= s.capitalize()
print(str)
"""

# PRACTICE TIME

#Program_12:
#...WAP to input user's first name & print its length
"""
s= input("Enter name: ")
print(s)
"""

#Program_13:
#...WAP to find the occurrence of 'S' in a string
"""
s= "String"
print(s.count("S"))     #1
"""

####################..............####################

#Conditional Statements
"""
There are diff. diff. conditions that exits in our life. we can express that conditions through code.

....if-elif-else.... (syntax)

if(condition):
    statement_1

elif(condition):   #elif works as else if works in c & c++
    statement_2

else:
    statement_N

"""

#Program_14:

"""
light = input("Enter color: ")

if(light == "red"):
    print("Stop")

elif(light == "green"):
    print("Go")

elif(light == "yello"):
    print("Look")

else:
    print("light is broken")

print("end of code")
"""

#Program_15:
"""
age= int(input("Enter age: "))

if(age>= 18):
    print("Eligible for vote")    #indentation means proper space
else:
    print("Not eligible")
"""

#Program_16: WAP to grade students based on marks
"""
marks>=90, grade= "A"
90>marks>=80, grade= "B"
80>marks >= 70, grade= "C"
70>marks, grade= "D"
"""

#Program_17:
"""
marks= int(input("Enter marks: "))

if(marks>=90):
    print("Grade A")
elif(marks<90 and marks>=80):
    print("Grade B")
elif(marks<80 and marks>=70):
    print("Grade C")
else:
   print("Grade D")
"""

#nested if elif condition
"""statement into statement"""

#Program_18
"""
age = int(input("enter age: "))
if(age>= 18):
    if(age<=80):
     print("can drive")
else:
     print("cann't drive")
"""

# PRACTICE TIME

#Program_19:
#...WAP to check if a number entered by user is odd or even.
"""
n= int(input("Enter number: "))

if (n%2== 0):
    print("number is even")
else:
    print("number is odd")
"""

#Program_20:
#...WAP to find the greatest of 3 numbers entered by the user.
"""
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

if(n1>n2 or n1>n3):
    if(n1>n2):
        print(n1, "is greater")
    else:
        print(n2, "is greater")
else:
    if(n2>n3):
        print(n2, "is greater")
    else:
        print(n3, "is greater")
"""

#Program_21:
#...WAP to check if a number is a multiple of 7 or not
"""
n= int(input("enter number: "))

if (n%7==0):
    print(n, "is multiple of 7")
else:
    print(n, "is not multiple of 7")
"""


