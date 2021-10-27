import datetime
from utils import date_cleaner

# list of possible and seen date formats extracted from excel
date_list = [datetime.datetime(2021, 1, 15), datetime.date(2021, 2, 15), '2021-3-23', '2021-14-01', '22.5.2010',]

# test all possible date formats
for date in date_list:
    output = date_cleaner(date)
    print('Date:', output)
    print(type(output))
    print('\n')
