"""
11)	Write a Python function 
that takes a list 
and returns a new list 
with unique elements of the first list. 
"""
#function without parameter without return

def unique():     #create a function named unique
    l1 = [5, 6, 7, 6, 5, "Python"]    #input a list with different data types

    l2=  set(l1)     #convert list into set to remove duplicates

    unique_list = list(l2)    #again convert set into list to take o/p as list
    print(unique_list)    #print result 

unique()  #function calling

######################################################

#function without parameter with return

def unique():
    l1 = [5, 6, 7, 6, 5, "Python"]

    l2 = set(l1)

    unique_list = list(l2)
    return unique_list

result = unique()
print(result)



#function with parameter without return

