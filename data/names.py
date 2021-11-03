# script for pasting names and sorting them to get unique names and surnames.
# These names and surnames will be useful to separate names and surnames
# from from fields where names and surnames are together.


# import lists with new pasted names
from raw_names import names
from raw_surnames import surnames

# paste names (str). NOTE must be an even number when split
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

nc_lst = []
# open clean names and surnames, put data into a list to be compared
with open('names_clean.txt', 'r', encoding='utf-8') as nc:
    for row in nc:
        row = row.replace('\n', '')
        nc_lst.append(row)

sc_lst = []
# open clean names and surnames, put data into a list to be compared
with open('surnames_clean.txt', 'r', encoding='utf-8') as sc:
    for row in sc:
        row = row.replace('\n', '')
        sc_lst.append(row)

# cleans the top lists above of names and surnames
for ns in [names, surnames]:
    clean = []

    for word in ns:
        # remove surnames that end with ic and ić
        if word[-2:].lower() == ('ić' or 'ic'):
            continue
        else:
            # capitalize first letter
            clean.append(word.title())

    # insert the list to the set
    clean = set(clean)
    # convert the set to the list
    clean = (list(clean))
    # sort ABC
    clean = sorted(clean)
    # get the print
    if ns == names:
        # open a (new) file to append
        outF = open("names_clean.txt", "a")
        for n in clean:
            if n in nc_lst:
                continue
            else:
                outF.write(n)
                outF.write('\n')
        outF.close()
    else:
        # open a (new) file to append
        outF = open("surnames_clean.txt", "a")
        for n in clean:
            if n in sc_lst:
                continue
            else:
                outF.write(n)
                outF.write('\n')
        outF.close()

# TODO create a script to take out all names and surnames and return them in alphabetical order