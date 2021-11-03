# script for pasting names and sorting them to get unique names and surnames.
# These names and surnames will be useful to separate names and surnames
# from from fields where names and surnames are together.

import csv
# import lists with new pasted names
from data.raw_names import names
from data.raw_surnames import surnames


def open_txt_r(txt):
    lst = []
    with open(txt, 'r', encoding='utf-8') as nc:
        for row in nc:
            row = row.replace('\n', '')
            lst.append(row)
        return lst

# open clean names and surnames, put data into a list to be compared
nc_lst = open_txt_r('data/names_clean.txt')
sc_lst = open_txt_r('data/surnames_clean.txt')

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