import datetime
import translators
from data.names import open_txt_r

# date patterns for strings
# combinens separation chaarcters with d,m,y,Y,b,B combinations
date_patterns = []
# list of predicted combinations of d,m,y,Y,b,B patterns
character_connectors = '.,-/ '
dmy = [
    '%d-%m-%Y', '%d-%m-%y',
    '%Y-%m-%d', '%y-%m-%d',
    '%Y-%b-%d', '%y-%b-%d',
    '%d-%b-%Y', '%d-%b-%y',
    '%d-%B-%Y', '%d-%B-%y',
    '%Y-%B-%d', '%y-%B-%d'
]
# loops through the combinations of days, months and years to get different patterns
for date_pat in dmy:
    # loops through '.,-/ ' to combine them as connectors between d m y
    for char in character_connectors:
        date_1 = (date_pat.replace('-', char))
        # if/esle swaps day and month
        if date_1[1].upper() != 'Y':
            date = date_1.split(char)
            date_2 = date[1] + char + date[0] + char + date[2]
        else:
            date = date_1.split(char)
            date_2 = date[0] + char + date[2] + char + date[1]

        # it is a greater possibility that the sequence is y-m-d aor d-m-y, therefore its inserted at the beginning.
        date_patterns.insert(0, date_1)
        # it is a small possibility, but still possible that the date sequence is m-d-y or y-d-m, there for its appended at the end.
        date_patterns.append(date_2)


# print date patterns created above
# print(date_patterns)


# date cleaner function
def date_cleaner(date):
    '''
    Multiple if statements try to predict all possible date formats entered in an excel sheet.
    It returns in the the and a clean date as: datetime.date(), YYYY-MM-DD
    :param date:
    :return:
    '''

    if isinstance(date, datetime.datetime) is True:
        return date.date()
    elif isinstance(date, datetime.date) is True:
        return date
    elif isinstance(date, str) is True:
        for pattern in date_patterns:
            try:
                date = datetime.datetime.strptime(date, pattern)
                return date.date()
            except:
                assert "Date is not in expected format: %s" % (date)
    else:
        assert 'Does not WORK, date is not predicted, go to date_cleaner()'


# TODO create function to compare dates. If stray dog surgery_date and 'release_date' are not the same as for the owned dogs
# TODO create a function that separates owner_address
#  in streat name, pops br. broj etc., and separates streat number and if availbele post code.
#  Maybe create a cpolumn for city/municipilty which is known beceause of the vet clinic.

# function returns capitalized first letter for first word in a string
# for example address
def capitalize_string(string):
    return string.capitalize()


# for example: dog name, owner name, vet name, catcher name
# function returns capitalized first letter for all words in a string
def title_string(string):
    return string.title()


# function that separates surname and name
def name_seprator(surname_name):
    nc_lst = open_txt_r('names_clean.txt')
    sc_lst = open_txt_r('surnames_clean.txt')
    lst = surname_name.split()
    #     nc_lst = open_txt_r('names_clean.txt')
    #     sc_lst = open_txt_r('surnames_clean.txt')

    if len(lst) == 2:
        name = lst[0]
        surname = lst[1]
    elif len(lst) == 3:
        name = lst[0]
        surname = lst[1] + ' ' + lst[2]
        surname_1 = ''
        surname_2 = ''
    else:
        name = surname_name
        surname = ''

    return name, surname


# function returns a 15 digit long string
# microchip number in Eurpe is 15 digit long
def microchip_cleaner(mchip):
    microchip = str(mchip)
    for char in 'abcdefghijklmnopqrstuvwxyzqxšđžćč,.()/*; ':
        if char in microchip.lower():
            microchip = microchip.lower().replace(char, '')
    # usually microchip starts with 0
    while len(microchip) != 15:
        if len(microchip) < 15:
            microchip = str(0) + microchip
        else:
            # this means that the microchip is longer than 15 characters
            # TODO get these examples(into a sheet written appended and saved) and figure out what to do with them
            # long_microchips.append(microchip)
            return microchip
    return str(microchip)


def weight_cleaner(wght):
    weight = str(wght).lower()
    if ',' in weight:
        weight = weight.replace(',', '.')
    for char in 'abcdefghijklmnopqrstuvwxyzqxšđžćč ':
        if char in weight.lower():
            weight = weight.lower().replace(char, '')
    return int(round(float(weight)))


# this function appends excel spreadsheet in debug outputs when an not implemented format appears
# TODO define what fields should this sheet have (vet clinic, name and date of origin excel, key_name and type
def debug_outputs():
    pass


# this function returns 'M' for males and 'F' for females.
def sex_cleaner(s):
    if s.upper() in ['M', 'MALE', 'MUSKO', 'MUZJAK', 'MUZIJAK', 'MUŠKO', 'MUŽJAK', 'MUŽIJAK']:
        return 'M'
    elif s.upper() in ['Ž', 'Z', 'ZENSKO', 'ŽENSKO', 'F', 'FEMALE', 'FEM']:
        return 'F'
    else:
        return s.upper()


# convert age to date (birthdate)
def age_birthdate_convcerter(age, surgery_date):
    '''

    :param age: grown dog, 2 years 6 months etc.
    :param surgery_date: as date object
    :return: birthdate (date object) and age (float)
    '''
    if str(age).lower() in ['odrastao', 'odrasto']:
        return 'unknown', 'grown'
    elif (isinstance(age, float) or isinstance(age, int)) == True:
        return surgery_date - datetime.timedelta(age * 365), str(age)
    else:
        # print('DEBUG: check age input form excel')
        return 'unknown', 'grown'


# google translate tool from Bosnian to english
def translate(text):
    if text.lower() in ['no', 'ne']:
        translation = 'Not pregnant'
    else:
        translation = translators.google(text, from_language='bs', to_language='en')
    return translation

# ear tag cleaner
# in order None make NULL in order to insert into postgreSQL
def eartag_cleaner(ear_tag):
    if ear_tag == None:
        return 'no stray'
    else:
        return str(ear_tag)