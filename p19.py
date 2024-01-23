from datetime import datetime
from dateutil.relativedelta import relativedelta


def counting_sundays_native(start_date, end_date):
    count = 0
    while start_date <= end_date:
        day_of_week = start_date.strftime('%A')
        if start_date.month == 12:
            start_date = datetime(start_date.year + 1, 1, 1)
        else:
            start_date = datetime(start_date.year, start_date.month + 1, 1)
        if day_of_week == 'Sunday':
            count += 1

    return count


def counting_sundays_dateutil(start_date, end_date):
    count = 0
    while start_date <= end_date:
        day_of_week = start_date.strftime('%A')
        start_date += relativedelta(months=1)
        if day_of_week == 'Sunday':
            count += 1

    return count


start_date = datetime(1901, 1, 1)
end_date = datetime(2000, 12, 31)
# print(counting_sundays(start_date, end_date)) 171
