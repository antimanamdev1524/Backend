# WAP to check whether an element exists within a tuple. 

try:
        T = (45, 55, 66, 77, "python", "c", "c++", "SQL")   #tuple values

 #to check user input is available in tuple or not

        element = input("Enter element: ")     # user input acceptable for string  if not 
      
        try:
         element = int(element)               # can also be try int input
        
        except:                               #int string al data_types can be pass into element variable
         pass


        if element in T:              
           print("Element exist into tuple")

        else:
           print("Element doesn't exist!!")

except ValueError as e:

 print(e)