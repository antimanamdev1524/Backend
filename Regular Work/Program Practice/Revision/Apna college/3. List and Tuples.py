#Lists in Python

"""

A built - in data type that stores set of values.

It can store elements of different types (integer, float, string, etc.)

Definition: List is a collection data type in python. we can store similar & dissimilar types of data in single variable. The items in the list are separated with the comma(,)

==> list is denoted by []
==> list is orderable
==> list is mutable (can be change)
==> list allows slicing

Ex: 
marks = [87, 64, 44, 95, 76]
student = ["karan", 67, "Delhi"]
student[0] = "Arjun"
len(student)
"""

#Program_1:
"""
marks = [94, 4, 87, 5, 95.4, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[4]  )
print(len(marks))
"""

####################..............####################

#List_Slicing
"""
list slicing is similar to string slicing    #ending idx is not included

ex:_1

marks = [87, 64, 33, 95, 76]
marks[1 : 4] is [64, 33, 95]
marks[ : 4] is same as marks[0 : 4] = [87, 64, 33, 95]
marks[1 : ] is same as marks [1 : len(marks)]
marks[-3: -1] is [33, 95]

ex:_2
this some types of list allows in python

marks = [87, 64, 33, 95, 76]
student = ["Karan", 85, "Delhi"]
student[0] = "Arjun"
len(student)
"""

#Program_2:
"""
marks = [87, 64, 33, 95, 76]
print(marks[1 : 4])
print(marks[0: 4])
print(marks[ : 4])
print(marks[1: ])
print(marks[1: len(marks)])
print(marks[-3: -1])
"""

####################..............####################

#List_Methods

"""
list = [2, 1, 3, 56]
list.append(45)                      #adds one element into end of the list
print(list) 

list.sort()                          #sorts in ascending order                    
print(list)

list.sort(reverse= True)             #sorts in descending order                
print(list)      


list.reverse()                       #It reverse the list
print(list)


list.insert(4, 77)                   #inset value at particular index
print(list)

"""
"""

print(list.clear(0))          
print(list.copy())
print(list.count(1))
print(list.extend("x"))
print(list.index())
print(list.insert())
"""

"""

list.pop(0)                           #remove particular index value
print(list.pop())


list.remove(3)                        #remove paricular value from list
print(list)

"""

"""

print(list.__add__())
print(list.__annotations__)
print(list.__class__)
print(list.__class_getitem__)
print(list.__contains__)
print(list.__delattr__)
print(list.__delitem__)
print(list.__dir__)
print(list.__doc__)
print(list.__eq__)
print(list.__format__)
print(list.__ge__)
print(list.__getattribute__)
print(list.__getstate__)
print(list.__getitem__)
print(list.__gt__)
print(list.__hash__)
print(list.__iadd__)
print(list.__imul__)
print(list.__init__)
print(list.__init_subclass__)
print(list.__iter__)
print(list.__le__)
print(list.__len__)
print(list.__lt__)
print(list.__module__)
print(list.__mul__)
print(list.__ne__)
print(list.__new__)
print(list.__qualname__)
print(list.__reduce__)
print(list.__reduce_ex__)
print(list.__repr__)
print(list.__reversed__)
print(list.__rmul__)
print(list.__setattr__)
print(list.__setitem__)
print(list.__sizeof__)
print(list.__str__)
print(list.__subclasshook___)
"""

####################..............####################

#Tuples

"""
==> Tuples is a built-in data type that lets us create immutable sequence of values.
==> Tuple is a collection data type in python, we can store multiple data in single variable.

.. Tuple is immutable  (list is mutable) 
.. Tuple allows duplicate values (list also allows)
.. () perenthesis brackes used into Tuple.

tup = (87, 64, 33, 95, 76)         #tup[0], tup[1]
tup[0] = 43                  #not allowed in python

tup 1 = ()
tup2 = (1,)
tup3 = (1, 2, 3)
""" 

#Program_3:
"""
T= (45, 56, 67, 78, 89)
print(type(T))
print(T)                       #can be print tuple list

print(T[1:3])                  #print value from index 1 to 2 (3 index value will not be print)

"""

####################..............####################

#Tuple_Method

"""
t = (2, 1, 3, 1)

t.index(2)
print(t)
"""

#Let's Practice
#Program_4:
#WAP to ask the user to enter names of their three favourite movies and store them in a list
"""
#code_1............................
m_1= input("first_movie: ")
m_2= input("second_movie: ")
m_3= input("Third movie: ")

list= [m_1, m_2, m_3]

print(list)

#code_2............................
movies= []
m_1= input("\n\nfirst_movie: ")
m_2= input("second_movie: ")
m_3= input("Third movie: ")

movies.append(m_1)
movies.append(m_2)
movies.append(m_3)

print(movies)

#code_3............................
movies= []
m_1= input("\n\nfirst_movie: ")
movies.append(m_1)

m_2= input("second_movie: ")
movies.append(m_2)

m_3= input("Third movie: ")
movies.append(m_3)

print(movies)


#code_4............................
movies= []

movies.append(input("\n\nfirst_movie: "))
movies.append(input("second_movie: "))
movies.append(input("Third movie: "))

print(movies)
"""

#palindrome list.......................

#Program_5:  
#WAP to check if a list contains a palindrome of element. (Hint: use copy() method)
"""
a= [1, 2, 3, 2, 6]

b= a.copy()
b.reverse()

if (a==b):
    print(a, "=", b, "list is palindrome")
else:
    print(a, "!=", b, "list is not palindrome")    
"""

#Program_6:
"""
x= [1, "abc", "abc", 1]

y= x.copy()
y.reverse()

if (x==y):
    print(x, "=", y, "list is palindrome")
else:
    print(x, "=", y, "list not palindrome")
""" 

#Program_7:
"""
x= [input("val_1: "), input("val_2: "), input("val_3: ")]

print(x)

y= x.copy()
y.reverse()

if (x==y):
    print(x, "=", y, "list is palindrome")
else:
    print(x, "=", y, "list not palindrome")
"""

#Program_8:  
#WAP to count the number of students with the "A" grade in the following tuple.
"""
T= ("C", "D", "A", "A", "B", "B", "A")

print("\nTuple values are: ", T)
print("Grade A students are: ", T.count("A"))


#Store the above values in a list & sort them from "A" to "D".
list= list(T)
print("\n\nconvert tuple() values into list[]: ", list)

list.sort()                     #Sorted into ascending order
print("\nSorted list: ", list)
"""