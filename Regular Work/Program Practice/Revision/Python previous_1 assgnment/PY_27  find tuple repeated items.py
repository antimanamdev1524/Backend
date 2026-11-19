# WAP to find the repeated items of a tuple. 
             
T = (55, 66, 77, 88, 55, 66, 55)

repeated_items = set() 

for item in T:
    if T.count(item)>1:
        repeated_items.add(item)

print("repeated items: ", repeated_items)