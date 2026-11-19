#fabonacci series
"""
n= int(input("enter number: "))
n1 = 0 
n2 = 1

for i in range(n):
     
     print(n1, end="" "\n")

     n3 = n1 + n2
     n1 = n2
     n2= n3
"""


def fabonacci_series():

    n= int(input("enter number: "))
    n1= 0
    n2= 1
    for i in range(n):
        print(n1, end=" ")

        n3 = n1+n2
        n1 = n2
        n2 = n3

fabonacci_series()



     