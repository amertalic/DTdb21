# paste names (str). NOTE must be an even number when split
# paste here!
str = ''' '''

# string becomes a list
lst = str.split()
print(len(lst))

# initialize 2 output lists
ime = []
prezime = []
# loops throu the list and separates names and surnames
# because its names as even numbers and surnames as odd numbers and vise versa
while lst != []:
    i = lst.pop(0)
    ime.append(i)
    p = lst.pop(0)
    prezime.append(p)

print(ime)
print(prezime)