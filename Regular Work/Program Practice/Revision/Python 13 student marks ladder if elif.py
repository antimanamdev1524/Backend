n= int(input("enter marks: "))

if n>33:
    if n>60:
        print("Ist rank")
    elif n>40:
        print("II rank")
    else:
        print("III rank")
else:
    print("Fail")