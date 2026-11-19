#Write a program to show rank of student through marks

n= int(input("enter number: "))

if n<33:
    print("fail")

elif n<40:
    print("III rank")
elif n<60:
    print("II rank")
else:
    print("I rank")