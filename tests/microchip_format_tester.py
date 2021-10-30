from utils import microchip_cleaner

# list of possible and seen microchips extracted from excel
weight_list = ['123456789123456', 123456789123456, '12345678912345', 12345678912345, '12345678912345.', 12345678912345.,
               '12345678912345.1', 12345678912345.1,'77745678912345.155', 77745678912345.1555
               ]


# test all possible microchip formats from above list
def microchip_format_tester():
    for mchip in weight_list:
        output = microchip_cleaner(mchip)
        print('microchip:', output)
        print(len(output))
        print(type(output))
        print('\n')


microchip_format_tester()
