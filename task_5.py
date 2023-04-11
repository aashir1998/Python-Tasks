import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta


def add_week_hours(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date_obj + relativedelta(weeks=1, hours=12)
    return new_date.strftime("%Y-%m-%d %H:%M:%S")


def add_four_months(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date = date_obj + relativedelta(months=4)
    return new_date.strftime('%Y-%m-%d')


if __name__ == "__main__":
    date_str= sys.argv[1]
    date1 = add_week_hours(date_str)
    date2 = add_four_months(date_str)
    print(f"Date 1 week and 12 hours from {date_str} is {date1}. Date 4 months from {date_str} is {date2}.")