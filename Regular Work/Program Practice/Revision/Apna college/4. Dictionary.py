#Dictionary
"""
==> Dictionary are used to store data values in key.value pairs
==> Dictionary are known as the collection data type in python. We can store multiple data in  key value pair.
     
     key + value = item

     * Items are mutable (changable)      (list mutable, tuple immutable)
     * Items are ordered                  (lisrt is orderable)
     * Items don't allow duplicate keys   (List & tuples allows duplicate values)

==> Dictionary are shown as {} curley braces
==> In python Dictionary cann't be repeated      
==> same type of data can be stored as into differet types of data.
==> list can be stored into dictionary.  {[--]}
==> or dictionary can be stored into list. [{--}]

"""

#program_1:
#list into dictionary
"""
dict = {
    "Name": ["Antima", "Disha", "Ronak"], 
    "Course": ["Full Stack", "Backend", "Frontend"], 
    "Language": ["Python", "PHP", "React"],
    "Experience": (4, 5, 4)
    }

print(type(dict))
print(dict)     #access the dictionary

print("\n\n")
"""
#-----------------0--------------0--------------0--------------0--------------

#program_2:
"""
dict = {
    "Name": ["Antima", "Disha", "Ronak"], 
    "Course": ["Full Stack", "Backend", "Frontend"], 
    "Language": ["Python", "PHP", "React"],
    "Experience": (4, 5, 4)
    }

print(dict["Name"])    #Access the values into dictionary by using key
print(dict["Course"])
print(dict["Language"])
print(dict["Experience"])

print("\n\n")
"""
"""
where
   key     :    values
 name           "Antima"
 courses        "Backend"
 language       "Python"
 experience     "4 year"
"""

#-----------------0--------------0--------------0--------------0--------------

#program_3:
"""
dict = {
    "Name": ["Antima", "Disha", "Ronak"], 
    "Course": ["Full Stack", "Backend", "Frontend"], 
    "Language": ["Python", "PHP", "React"],
    "Experience": (4, 5, 4)
    }

dict["Name"] = "Annu"   #overwrite
print(dict)

print("\n\n")
"""
#-----------------0--------------0--------------0--------------0--------------

#program_4:

"""
dict = {
    "Name": ["Antima", "Disha", "Ronak"], 
    "Course": ["Full Stack", "Backend", "Frontend"], 
    "Language": ["Python", "PHP", "React"],
    "Experience": (4, 5, 4)
    }

null_dict = {}
print(null_dict)

null_dict["name"] = "apnacollege"     #we can add something into null dictionary
print(null_dict)   

print("\n\n")
"""
#######################################

#Nested Dictionaries
"""
A dictionary can contain dictionaries, this is called nested dictionaries.   {{--}}

ex.

student = {
    "Name": "Antima",
    "score": { 
        "chem": 98, 
        "phy": 97, 
        "math": 95
        }
     }

student["score"]["math"]
"""

#program_5:
"""
student= {"Name": "Antima Namdev", "Subject": {"Phy": 97, "chem": 98, "math": 95}}

print(student)
print("\n\n Nested Dictionary is:\n")

print(student["Subject"])

print(student["Subject"]["chem"])
"""

#######################################

#Nested Dictionaries
"""
Dictionary methods:

myDict.keys()      #returns all keys
myDict.values()    #returns all values
myDict.items()     #returns all(key, val) pairs as tuples
myDict.get("key")  #returns the key according to value
myDict.update(newDict)      #inserts the specified items to the dictionary 
"""


#program_6:

student = {
    "Name": "Antima",
    "score": { 
        "chem": 98, 
        "phy": 97, 
        "math": 95
        }
     }

# keys method 
"""

print(student.keys())   #access the keys
     
print(list(student.keys()))  #access the value through list   means typecast into list

print(len(student.keys()))   #total keys length

#-----------------0--------------0--------------0--------------0--------------

#values method

print(student.values())    #access complete dictionary data

#-----------------0--------------0--------------0--------------0--------------

#  .items method

print(student.items())

"""
"""
output: 
dict_items([('Name', 'Antima'), ('score', {'chem': 98, 'phy': 97, 'math': 95})])

list[]
tuple()
dictionary{}

list can be into tuple and dictionary
dictionary can be into list
"""
#-----------------0--------------0--------------0--------------0--------------

#  .get method         RETURN THE KEY ACCORDING TO VALUE

"""
#print(student["name2"])        #returns error
print(student.get("name2"))     #returns null value  (show "None")

#-----------------0--------------0--------------0--------------0--------------

#  .update method

student.update({"city": "delhi"})

print(student)

#also can be update as

new_dict = {"city" : "lucknow", "age": 55}
student.update(new_dict)

print(student)

#dictionary doesn't allow duplicate value it overwrites.

"""

#######################################

#Set in Python
"""
Set is the collection of the unordered items.
Each element in the set must be unique & immutable.
set ignore duplicate values
set are mutable but elements of set are immutable, so that we can pas tuples into set.
set are denoted with {}

nums = { 1, 2, 3, 4}

set2 = { 1, 2, 2, 2}
Note: repeated elements stored only once, so it resolved to { 1, 2}

null_set = set()     #empty set syntax

list and dictionary never stored into set because it doesn't allow duplicate values
tuple can be stored into set because it is immutable
"""

#program_7:
"""
collection = {1, 2, 3, 4, "set", 4, 4}

print(collection)
print(type(collection))   #duplicates values stores only at a time 
print(len(collection))   #total len but it also ignore duplicate values 
"""

#program_8:
"""
collection= set()   #to create empty set
print(type(collection))
print(collection)
"""
#######################################

#Set methods:
"""
set.add(el)                #adds an element
set.remove(el)             # removes the element
set.clear()                #empties the set
set.pop                    #removes a random value
set.union(set2)            #combines both set values & returns new
set.intersection(set2)     #combines common values & returns new
"""

#program_09:
"""
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(3)             #it has ignored duplicate value
collection.add("Backend developer")
collection.add((1, 2, 3))     #can be pass tuples but list cann't be pass because it is mutable

print(collection)

collection.remove(2)     #removes value
print(collection)      

print(len((collection)))    #print lengt  

collection.clear()    #set will be empty
print(collection)
"""

#program_10:
"""
collection = {"hello", "python", "PHP", "Java", "C"}

print(collection.pop())    #it removes element randome
"""

#program_11
"""
set_1= {1, 2, 3}
set_2= {2, 3, 4}

print(set_1)
print(set_2)

#union: combines both set values & returns new but not duplicates

print(set_1.union(set_2))               #   {1, 2, 3, 4}   
print(set_1.intersection(set_2))        #   {2, 3}
"""

#######################################

#let's practice
#Program_12:

"""
Store following word meaning in a python dictionary:
table: "a piece of furniture", "list of facts & figure"
cat: "a small animal"
"""

"""
dict= {"table": ["a piece of furniture", "list of facts & figure"], "cat": "a small animal"}

print(dict)
"""

#Program_13:

"""
You are given a list of subjects for students. 
Assume one classroom is required for 1 subject. 
How many classroom are needed by all students.
"""

"""
subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "C++", "C"}


print(subjects)

print(len(subect))
"""

#Program_14:
"""
WAP to enter marks of 3 subjects from the user 
and store them in a dictionary.
start with an empty dictionary & add one  by one. 
Use subject name as key & marks as value.
"""

#code_1
"""
Marks = {}

Physics =  int(input("Physics: "))
Marks.update({"Physics" : Physics})

Chemistry = int(input("Chemistry: "))
Marks.update({"Chemistry" : Chemistry})

Maths = int(input("Maths: "))
Marks.update({"Maths" : Maths})

print(Marks)
"""

#-----------------0--------------0--------------0--------------0--------------

#code_2
"""
Marks = {}

x =  int(input("Physics: "))
y = int(input("Chemistry: "))
z = int(input("Maths: "))

Marks.update({"Physics" : x, "Chemistry" : y, "Maths" : z})

print(Marks)
"""


#Program_15:

"""
Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data type)
"""
#code_1
"""
set = {9, "9.0"}

print(set)
"""
#-----------------0--------------0--------------0--------------0--------------

"""
#code_2

set_tuple = {("float", 9.0), ("int", 9)}

print(set_tuple)
"""