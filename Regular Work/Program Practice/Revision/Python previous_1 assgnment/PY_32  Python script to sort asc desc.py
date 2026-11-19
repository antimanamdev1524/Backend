# Write a Python script to sort (ascending and descending) a dictionary by value

d = { 1: 77, 2: 44, 3: 66, 4: 55}

#logic to arrange dictionary values into ascending order
asc = dict(sorted(d.items(), key = lambda item: item[1]))

#logic to arrange dictionary values into descending order
desc = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))


print("ASC: ", asc, "\nDesc: ", desc)