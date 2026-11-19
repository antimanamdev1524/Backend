# 13) Write a Python program to select an item randomly from a list.
          
import random     #use python built in method to generate randome o/p

l = ["Apple", "Banana", "Orange", "Kiwi", "Lime", "Pineapple"]   #input list

random_items = random.choice(l)      #take list into built-in method to generate choice list randomly
print( "list: ", l,"\n\nrandomly select items from list: ", random_items)   #print result