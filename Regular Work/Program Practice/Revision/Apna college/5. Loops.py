#Conditional statement in Python
"""
Conditional Statement in python perform different computations or actions depending on whether a specific Boolean constraint evalutes to true or false. 
Conditional Statements are handle by if statements in python

types of Conditional statement

==> if 
==> if-else 
==> if-else ladder (can be write multiple conditions)
==> nested if (if into if condition)
note: indentation(:) is compulsory
"""


#if
#Program_1:
"""
a =10

if (a == 10):
    print("value is 10")

print("Thanks")

"""

#Program_2:
"""
a = int(input("Enter number: "))
if(a>=25):
    print("value of variable is 25")
print("Thanks")

"""

#if-else
#Program_3:
"""
a= int(input("A: "))
b= int(input("B: "))

if a<b:
    print("B is greater")
else:
    print("A is greater")

"""

#Program_4:
"""
x= 56
y= 78

if x<y:
    print(y, "is greater")
else:
    print(x, "is greater")

"""

#if- else ladder
#Program_5:
"""
 percentage >==70   = Dist
 percentage >= 65 and percentage <= 70   = first class
 percentage >= 60 and percentage <= 65   = second class
 percentage >= 55 and percentage <= 60   = third class
"""

"""
percent = int(input("enter percentage: "))

if percent>= 70:
    print("Dist")
elif percent >= 65 and percent<= 70:
    print("First class")
elif percent >= 60 and percent <= 65:
    print("Second class")
elif percent>= 55 and percent <= 60:
    print("Third class")
else:
    print("fail")
"""

#Nested if
#Program_6:
"""
age>= 18 
weight>= 50
if age and weight match with criteria then the user can donate the blood
if age is less than 18 than show msg is under age
if weight is less than 50 9one msg under weight
if age doesn't match then it ask for weight
"""

"""
age = int(input("Age: "))

if age >= 18:
    weight = int(input("Weight: "))
    if weight>= 50:
        print("Donate blood")
    else:
        print("under weight")
else:
    print("under age")
"""

####################..............####################

#Loops in Python

"""
Loops are used to repeat instructions.
there are two types of loop
==> while loop 
                 while condition:
==> for loop
"""

#Program_7:
#code_1
"""
while True:           #loop will be run infinity
    print("hello")   
"""

#-----------------0--------------0--------------0--------------0--------------

#code_2
"""
count = 1
while count <= 5:     
    print("hello")
    count+=1          
"""
"""
 if count = 1
 count will always be <= 5    
 but count+=1 it means after an execution count value will be increase one by one.
"""

#Program_8:
#print number 1 to 50
"""
i= 1
while i<= 10:
    print(i)
    i+=1

print("\n")

i= 10
while i>= 1:
    print(i)
    i-=1
"""

#Program_9:
#print numbers from 1 to 100
"""
i= 1
while i<= 100:
    print(i)
    i+=1
"""

#Program_10:
#WAP to print reverse numbers from 100 to 1.
"""
i= 100
while i>= 1:
    print(i)
    i-=1
"""

#Program_11:
# WAP to print the multiplication table of a number n.
"""
n= int(input("Multiplication table of: "))
i= 1
while i<= 10:
    print(n*i)
    i+=1
"""

#Program_12:
"""
 Print the elements of the following list using a loop:
 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
#code_1
"""
i= 1
while i<= 10:
    print(i*i)
    i+=1
"""
#-----------------0--------------0--------------0--------------0--------------

#code_2
"""
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx+=1
"""
"""
....treverse....
kisi bhi list ya dictionary pr one ny one jana travers kehlata h
"""
#Program_13:
"""
 WAP to search index for a number x in this tuple using loop:
  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
"""

"""
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x= int(input("enter square between 1 to 10: "))

i= 0

while i< len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
    i+= 1
"""

####################..............####################

# Break & Continue
"""
Break: used to terminate the loop when encountered

Continue: terminates execution in the current iteration & continues execution of the loop with the next iteration.
"""
#Break
#Program_14:
"""
i = 1
while i <= 5:
    print(i)

    if (i==3):
        break
    i+= 1

print("loop end")
"""

#Program_15:
"""
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
i=0

while i<len(nums):
    if(nums[i] == x):
        print("found at idx: ", i)
        break
    else:
        print("finding...")
    i+= 1

print("end of loop")
"""

#Continue
#Program_16:

i = 0
while i<= 5:
    if (i == 3):
        continue
    print(i)
    i+= 1
