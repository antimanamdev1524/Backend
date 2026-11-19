"""
 #program:_1

  print("apna college")

  print(45)

  print(55+ 45)

  print("Antima is my name", "my course is FSD")
"""
#####################


    #variable: 

"""
     A varable is a name given to a memory location in a program

     name= "Antima"
     age= 45
     Price= 56.67

     where 
     variable= name, age, Price
     value= Antima, 45, 56.67
"""

"""
#program:_2
name= "Antima"
age= 56
price= 56.67

print(name)  #to print value colon will not be used.
print("my name is: ", name)
print("Age: ", age)

age5= age
print("age5: ", age5)

print(type(name))    #datatypes
print(type(age))
print(type(price))
"""

#generally 5 types of data type
# integer: positive int, negative int, zero
# string: name or words that writes into "double quote", 'single quote', '''triple quote'''
# float: decimal values (5.66, 67.67, 8.0)
# boolean: True and False  (T & F should capital)
# None: a= none (it means there is no value in variable a)

"""
Rules for identifiers:
* ideantifier can be combination of uppercase  and lowercase letter, dogots or an underscore(_).
so myVariable, variable_5, variable_for_print all are valid python identifiers.

* An identifier can not start with digit, So while varialbe5 is valid, 5variable is not valid.

* we can't use special symbols like !. #, @, %, ^, *, $ etc. in our identifier.

* identifier can be of any length.
"""
#####################


#Keywords: keywords are reserved words in python

"""
and            else            in            return
as             expect          is            True 
assert         Finally         lambda        try
break          False           noniocal      with
class          for             None          while
continue       from            not           yield
def            global          or
def            if              pass           
elif           import          raise     

*python is case- sensitive language
"""

"""
#program:_3:
#print sum

a= 5000
b= 500
sum= a+b
diff= a-b
print(sum)
print(diff)
"""
###################



#Types of Tokens:

"""
Punctuators are symbols to organize sentences structure in programming.
(), {}, [], @, # etc.
-=, +=, /=, *=, //=, = etc

*python is a implicit type language

type of language: implicit, explicit  
* implicit means variable type is predefined  
     ex. python
* explicit means it requires to defined variable type 
     ex. java, c, c++
"""
####################



#Expression Execution:

#program:_4
"""
#string and Numeric values can operate together with *
A, B= 5, 6
Txt=  "@"
print(2*Txt*3)

#output: @@@@@@
"""

#program:_5
"""
A, B="5", 6   #here 5 will be work as string because it is in double quote
Txt= "@"
print((A + Txt)*B)

#output: 5@5@5@5@5@5@
#when two string added together with the help of + sign. It is known as concatanation
"""

#program:_6
"""
# Numeric values can operate with all arithmetic operators
A, B= 5, 6
c= 4
print(A+B*C)

#output: 100
"""

#program:_7
"""
# Arithmetic expression with integer and float will result in float
A, B= 40, 5.0
c= A*B
print(c)

#output: 20.0
"""

#program:_8
"""
# Result of division with float and int will give int displayed as float
A, B=  1, 2
c= A/B
print(c)

#output: 0.5
"""


#program:_9
"""
# Integer division with float and int will give int displayed as float
A, B= 1.5, 3
c= A//B
print(c, A/B)

#output: 0.0, 0.5
#output should be 0.5 but it round off the number in minimum number and give answer in float so A//B = 0.0 (0.5 round off the real ans)
"""


#program:_10
"""
#floor gives closest integer, which is lesser than or equal to the float value
#Result of (A//B) is same as floor(A/B)
"""

"""
A, B= 54, 5
C= A//B
print(C)
#output: 10

A, B= -54, 5
C= A//B
print(C)
#output: -11

A, B= 54, -5
C= A//B
print(C)
#output: -11
"""

##program:_11
"""
#Reminder is negative when denominator is negative

A, B= -5, 2
C= A%B
print(C)
#output: 1

A, B= 5, 2
C= A%B
print(C)
#output: 1

A, B= 5, -2
C= A%B
print(C)
#output: -1
"""
####################


#comments

# (Hash) is uses to mention single line comment

"""
This is multi
line 
comment (three time double quote)
"""

"""


#input in Python

"""
#input() statement is used to accept values (using keyboard) from user

"""
#1) String Input
name = input("name: ")

#2) int Input
age = int(input("age: "))

#3) float Input
price =  float(input("price: "))

print(name)
print(age)
print(price)

print("My name is: ", name, "and my I am ", age, "years old")
"""

#PRACTICE TIME: (STATE TRUE OR FALSE)

#1) l* is a symbol used in python for single line comment.    (FALSE) #use for comment
#2) 2ndNAme is an invalid identifier in python.               (TRUE) first letter start from capital or small letter or with underscoure_
#3) ** is a valid arithmetic operator in python.              (TRUE) Ex. a**b
#4) in is a logical operator in python.                       (FALSE)  logical operators are: OR, XOR, AND
#5) Variable declaration is implict in python.                (TRUE) explicit and implicit are two types of variable declaration

#6) Consider the given expression: NOT TRUE and FALSE or TRUE
"""
 Which of the following will be correct output if the given expression is evalute?
 TRUE        FALSE         NONE        NULL

Solution: 
 NOT TRUE and FALSE or TRUE   (NOT TRUE = False )
 FALSE and FALSE or TRUE      (F and F = F)
 FALSE or TRUE                (F or T =  T) 
 TRUE

  answer is: TRUE
"""
####################


# CONDITIONAL STATEMENT

# if-elif-else (Syntax)
# if-elif
# if

"""
 Ese statement jinke ander koi condition ho
 ex.
 18+ age for vote
 driving license
 grade A First rank
 grade B Second rank

"""


"""

if(condition):
     statement_1
elif(condition):
     statement_2
else:
     statementN
"""
# after condition colom insertion is compulsory
"""
ex_1:
if(age>=18):
    print("eligible for vote")
elif(Citizenship==indian):
    print("Elitible for vote in india")
else:
     print("not eligible")
"""

#python is an indentation language

"""
(indentation means  how much space we are taking in statement or code or can be defined as proper space)
ex_2:
    if(age>=18):                              ....check first condition....
         print("eligible for vote")
         print("-")
    elif(Citizenship==indian):                ....when first condition doen't true it will be check next elif condition)....
         print("Elitible for vote in india")
    elif(condition):                          ....if elif condition doesn't true can be add more elif condition)....
         print("_")
     else:                                    ....if all condition get false....
     print("not eligible")
"""

#Program_12:

"""
light= input("light color: ")

if(light== "red"):
     print("stop")
elif(light== "yellow"):
     print("look")
elif(light== "green"):
     print("go")
else:
     print("light is broken")
"""

#Program_13:

"""
90 - 100 == A
80 - 90 == B
70 - 80 == C
otherwise D


marks= int(input("Enter Marks: "))

if(marks>=90):
     print("Grade A")
elif(marks>=80 and marks<90):
     print("Grade B")
elif(marks>=70 and marks <80):
     print("Grade C")
else:
     print("Grade D")   

"""

#Program_14:

"""
A= int(input("A: "))
G= input("M/F: ")

if((A==1 or A==2) and G == "M"):
     print("Fee is 100")
elif(A==3 or A==4 or G== "F"):
     print("fee is 200")
elif(A==5 and G== "M"):
     print("fee is 300")
else:
     print("no fee")
"""

"""
Output:
1)....
A= 5
G= M
solution:
first condition (A==1 or A==2) and G == "M")
                (F or F) and T
                 F and T
                  F

second condition (A==3 or A==4 or G== "F"):
                   (F or F or F)
                   (F or F)
                   F

third condition  (A==5 and G== "M")
                   (T and T)
                   T                third condition is true 
ans: fee is 300

2)....
A= 2
G= F
solution:
first condition (A==1 or A==2) and G == "M")
                (F or T) and F
                 T and F
                  F

second condition (A==3 or A==4 or G== "F"):
                   (F or F or T)
                   (F or T)
                   T                second condition is true 
                 
ans: fee is 200
"""

# Conditional statements

"""
#single line if/Ternary Operator
"""

#Program_14:

#<var> = <val1>if<condition>else<val2>
"""
food = input("food: ")
eat = "Yes"
if(food=="apple"):
     print(eat)

else:
     print("No")
"""

#Program_15:
#<stt1>if<condition>else<stt2>
"""
food = input("food: ")

if(food== "cake" or food== "jalebi"):
     print("sweet")
else:
     print("not sweet")
"""

#Program_16:
#var> = (false_val, true_val)[<condition>]
"""
age= int(input("Enter age: "))
if(age>=18):
     print("vote! yes")
else:
     print("vote! No")
"""

#Program_17:
"""
sal= float(input("salary: "))
tax= sal*(0.1)  
tax1 = sal*( 0.2)
if(sal<=50000):
     print(tax)
else:
     print(tax1)
"""

#BEST PRACTICE
#...simple instruction   
#...one instruction per task
#...short  and meaningful variable name
#...use appropriate comments
#...avoid complex expression


#Program_18:
#CALCULATE Simple Interest
"""
P= int(input("P: "))
R= float(input("R: "))
T= int(input("T: "))

SI = (P*R*T)/100

print("SI: ", SI)
"""
####################


#TYPES OF OPERATOR

"""

An operator is a symbol that performs a certain operation between Operands.

Arithmetic Operators (+, -, *, /, %, **)

Relational/Comparison Operators (==, !=, >, <, >=, <=)

Assignment Operators (=, +=, -=, *=, /=, %=. **=)

Logical Operators (not, and, or)

"""

#Program_19:
#aritjhmetc operators
"""
a= 45
b= 6

print( a+b)
print(a-b)
print(a*b)  #multiply or asterisk
print(a/b)  #gives division ans as a float value   / forward slash
print(a%b)  #reminder  % modulo is use to find reminder between two operand
print(a**b)  means a^b to find power

#ans always comes as a floating value, when we divide two values.
"""

#Program_20:
#Relational Operator

"""
a= 50
b= 20

print(a == b)  #False  == equal to
print(a!=b) #True    ! exclamation mark mean not != not equal to
print(a>=b) #True
print(a>b)  #True
print(a<=b) #False
print(a<b)  #False

#output will be show here as a boolean value like True or False
"""

#Program_21:
#Assignment Operator

"""
Assignment operator is used to assign any value
"""
"""
num= 10

num+=10      #num = num + 10     10+10 = 20
print("num: ", num)

num-=5       #num = num - 5      20 - 5 = 15
print("num: ", num)

num*=5       #num = num * 5      15 * 5 = 75
print("num: ", num)

num/=5       #num = num/5        75 / 5 = 15
print("num: ", num)

num**=2       #num means  15^2 = 15 * 15 = 225
print("num: ", num)
"""

#Program_22:
#Logical Operator

"""
print(not False)  #True
print(not True)   #False
"""
#Program_23:
"""
a= 50
b= 40

print(not False)  #True
print(not (a>b))  # not (50>40)     not True = False

"""

#Program_24:
#AND Operator

"""
val1 = True
val2 = True


print("T and T= ", val1 and val2 )  #True

print("F and F= ", False and False)   #False

print("F and T= ", False and True)  #False

print("T and F= ", True and False)   #False



 #OR Operator means OR

print("T or T= ", True or True )  #True

print("F or F= ", False or False)  #False

print("F or T= ", False or True)  #True

print("T or F= ", True or False)   #True
"""
####################


# TYPE CONVERSION

#Difference between TYPE CASTING and TYPE CONVERSION

#TYPE CONVERSION: python interpreter convert type automatically
#TYPE CASTING: interpreter doesn't convert type automatically, programmer codes manually to convert type


#TYPE CONVERSION
"""
#Program_25:
a = 2        #int
b = 4.56     #float
sum= a+b     #2.0 +4.56 = 6.56   it converts automatically int into supirior value
print(sum)


#TYPE CASTING
#Program_26:
a = int("2")       #int
b = 4.56     #float
sum= a+b     #2.0 +4.56 = 6.56   it converts automatically
print(sum)   
"""

"""
#Program_27:
a= 3.14
a= str(a)      #generally a ki value float h but str type dene pr yeh str type show krega
print(type(a))  #str  

b= 5.67
b= str(b)
print(type(a))  #str

b= 567
print(type(b))   # type int

b= "567"
print(type(b))   #type  str

b= "567"
print(b)         # 567
"""
####################


# INPUT in Python

"""
input() #statement is used to accept values (using keyboard) from user

input() #result for input() is always a str

int(input()) #int

float(input())  #float
"""

#Program_28:

"""
#use of input statement
input("Enter Your Name: ")   

name= input("Enmter Your Name: ")
print("Welcome", name)

val= input("enter some value: ")
print(type(val), val)   #type(val) = it will be show val type


val= int(input("enter value: "))
print(type(val), val)

val= float(input("enter value: "))
print(type(val), val)
"""

#Program_29:

"""
name= input("Name: ")
age= int(input("Age: "))
marks= int(input("Marks: "))

print("Welcome ", name)
print("Age: ", age)
print("Marks: ", marks)
"""


# PRACTICE TIME

#Program_30
#...Write a proogram to input two numbers and print their sum.
"""
a= int(input("A: "))
b= int(input("B: "))
print("Sum is", a+b)
"""

#Program_31
#...WAP to input side of a square and print its area.
"""
side= float(input("Enter side of a square: "))
area= side**2
print("area: ", area)
"""

#Program_32
#...WAP to input two floating point number and print their average.
"""
a= float(input("A: "))
b= float(input("B: "))

sum= a+b
avg= sum/2
print("Average: ", (a+b)/2)
print("Average: ", avg)
"""

#Program_33
#...WAP to input two numbers, a and b. Print True if a is greater that or equal to b. if not print False
"""
a= int(input("A: "))
b= int(input("B: "))

print(a>b)
"""

"""
output: 
A: 56
B: 78
False

A: 78
B: 65
True
"""