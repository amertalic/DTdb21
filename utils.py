import datetime


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
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()
