"""
Write a Python program to generate and 
print a list of first and last 5 elements 
where the values are square of numbers between 1 and 30. 
"""

list = []    #blank list

for i in range(1, 31):   #loop for 1 to 30 numbers
   square = i*i         #square logic for looping numbers

#adding square result into list 

   list.append(square)    

#to find first alast 5 square list slicing
   
first_five = list[:5]
last_five = list[-5:]

print(first_five)
print(last_five)





