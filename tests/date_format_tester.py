import datetime
from utils import date_cleaner

# list of possible and seen date formats extracted from excel
date_list = [
    datetime.datetime(2021, 1, 15), datetime.date(2021, 2, 15), '2021-3-23', '2021-14-01',
    '22.5.2010', '2033/10/01', '21-Feb-03', '21-April-03', '2021-April-03', '31.May.21','31.December.21','December 01 21'
]

# test all possible date formats from above list
def date_fromat_tester():
    for date in date_list:
        output = date_cleaner(date)
        print('Date:', output)
        print(type(output))
        print('\n')

# date_fromat_tester()

# TODO compare previously extracted dates to compare
# for example: '10-11-09', all three number could be a y,m and d.