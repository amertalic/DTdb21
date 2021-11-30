import os

def open_txt_r(txt):
    lst = []
    with open(txt, 'r', encoding='utf-8') as nc:
        for row in nc:
            row = row.replace('\n', '')
            lst.append(row)
        return lst
# open clean names and surnames, put data into a list to be compared
# Windows & ubuntu
bff = open_txt_r(os.path.join("bff.txt"))
prijave = open_txt_r(os.path.join("prijave.txt"))

bff2 = []
for name in bff:
    name = name.lower()
    name = name.strip()
    name = name.replace(' ','')
    name = name.replace('č','c')
    name = name.replace('š', 's')
    name = name.replace('ć', 'c')
    name = name.replace('ž', 'z')
    name = name.replace('đ', 'dj')
    bff2.append(name)


prijave2 = []
for name in prijave:
    name = name.lower()
    name = name.strip()
    name = name.replace(' ','')
    name = name.replace('č','c')
    name = name.replace('š', 's')
    name = name.replace('ć', 'c')
    name = name.replace('ž', 'z')
    name = name.replace('đ', 'dj')
    prijave2.append(name)

imena_u_bff = []
for name in prijave2:
    if name in bff2:
        imena_u_bff.append(name)

imena_u_bff = sorted(imena_u_bff)

for i in imena_u_bff:
    print(i)
