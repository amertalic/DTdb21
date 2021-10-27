import datetime
from utils import date_cleaner

# list of possible and seen date formats extracted from excel
date_list = [datetime.datetime(2021, 3, 15), datetime.date(2021, 3, 15), '2021-10-23']

# test all possible date formats
for date in date_list:
    output = date_cleaner(date)
    print('Date:', output)
    print(type(output))
    print('\n')
