# 14) Write a Python program to find the second smallest number in a list.

#function without parameter with return

def smallest():    #create function to find second smallest number

  list = [44, 55, 66, 97, 88, 405]   #input list

  list.sort()     #arrange list into ascending order
  print("\nlist: ", list)  #print ascending ordered list
  
  return list[1:2]    #list slicing to return second smallest int
 
result = smallest()   #function caling

print("second smallest is: ", result)  #print result 

