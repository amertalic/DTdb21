import datetime
from utils import weight_cleaner

# list of possible and seen date wight extracted from excel
weight_list = ['10', 10, '10,', '10,0','10,21354654', '10,546 kg', '10.654646 kg', '10.54564', 10.54654, '45,Akg', '3.454sd45kg'
]

# test all possible date formats from above list
def weight_format_tester():
    for weight in weight_list:
        output = weight_cleaner(weight)
        print('weight:', output)
        print(type(output))
        print('\n')

weight_format_tester()

