# 17) Write a Python program to split a list into different variables. 

l = [5, 6, 7, 8, "c", "CPP", "SQL", "Python"]

for i in l:
  l[i], *others = l

  print(i)
print(others)