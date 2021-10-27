import datetime

# date patterns for strings
date_patterns = [
    "%d-%m-%Y", "%d-%m-%y", "%Y-%m-%d", "%y-%m-%d", "%Y-%d-%m",
    "%d.%m.%Y", "%d.%m.%y", "%Y.%m.%d", "%y.%m.%d", "%Y-%d-%m"
]


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
        assert 'Does not WORK'
