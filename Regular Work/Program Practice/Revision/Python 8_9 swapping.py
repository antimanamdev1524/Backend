#Swapping

a= int(input("A: "))
b= int(input("B: "))

temp= a
a=b
b= temp

print("A: ", a)
print("B: ", b)

##############################


a= int(input("a: "))
b= int(input("b: "))

a= a+b
b= a-b
a= a-b

print("a= ", a)
print("b= ", b)