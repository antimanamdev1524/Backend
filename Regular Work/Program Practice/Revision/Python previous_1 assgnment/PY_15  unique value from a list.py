# 15) Write a Python program to get unique values from a list

l = ["C", "C++", "SQL", "Python", "Python", "C", 45, 56, 67]  #input list

s_1 = set(l)   #convert list into set because set doesn't allow duplicates, it returns unique values
print("unique values are: \n", s_1)