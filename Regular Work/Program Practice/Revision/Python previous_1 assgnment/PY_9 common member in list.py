"""Python function that takes two lists 
and returns true if they have at least one common member.
"""

def common_list():
    l= [5, 9, 4]
    l1 = [6, 0, 8]

    for i in l:
         if i in l1:
             return True
    return False   

result = common_list() 
 
print(result)    


    