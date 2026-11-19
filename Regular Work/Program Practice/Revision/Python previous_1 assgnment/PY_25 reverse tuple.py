# WAP to reverse a tuple. 

T = (44, 55, 66, 77, "python", "C", "C++")   #tuple values

l = list(T)        #convert tuple into list

list.reverse(l)    #reverse the list

t = tuple(l)     #convert reverse list into tuple

print("\nTuple Values:", T, "\n\nReverse The Tuple: ", t)


