i=0
ev = 0
od = 0
sum = 0
sum1 = 0


while i<5:
  n= int(input("enter number: "))
  if(n%2==0):
    print(n, "is even number")
    ev+=1
    sum+=n
  else:
    print(n, "is odd number")
    od+=1
    sum1+=n
  i+=1
print("even count: ", ev)
print("odd count: ", od)

print("even sum: ", sum)
print("odd sum: ", sum1)