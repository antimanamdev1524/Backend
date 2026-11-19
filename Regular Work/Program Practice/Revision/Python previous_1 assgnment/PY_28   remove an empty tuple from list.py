# WAP to remove an empty tuple(s) from a list of tuples.

l = [(), (55, 66), (77, 88), (), (88, 99), ()]


for tup in l:
    if tup:                       
        print(tup)
"""

while () in l:
    l.remove(())

print(l)

"""