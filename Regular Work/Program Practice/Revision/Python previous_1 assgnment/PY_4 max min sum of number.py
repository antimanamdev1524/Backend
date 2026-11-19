# 4)	Write a Python function to get the largest number, smallest num and sum of all from a list. 

def max_min_sum():              #function without parameter
    l = [4, 5, 6, 7, 8, 9, 10]   #list 

#using  built-in method to find max, min and calculate total of list
    largest = max(l)    
    smallest = min(l)
    T_sum = sum(l)

    return largest, smallest, T_sum   #function with return

largest, smallest, T_sum = max_min_sum()   #function calling

#print results
print(largest, "is largest")

print(smallest, "is smallest")
print("sum is: ", T_sum)

