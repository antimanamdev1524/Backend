#7)	Write a Python program to remove duplicates from a list.

l = [5, 6, 7, 8, 9, 6, 7, 5]

"""convert list into set to remove duplicates
because set doesn't allow duplicate values
"""

unique = list(set(l))   

print(unique)