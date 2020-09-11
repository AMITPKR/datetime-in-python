"""
week4 working with dates project date 06-09-2020 with python programming
computing no of days,valid days,difference between dates and person's age in day
"""

import datetime
# the key idea of this program to learn date time module


def days_in_month(year, month):
    """
       Inputs:
         year  - an integer between 1 and 9999
                 representing the year
         month - an integer between 1 and 12 representing the month
       Returns:
         The number of days in the input month.
    """
    if year % 4 == 0:
        year = 'leap year'
    if month in [4, 6, 9, 11]:
        return 30

    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    elif month == 2 and year == "leap year":
        return 29

    elif month == 2 and year != "leap year":
        return 28


value = days_in_month(2000, 2)
print("no of days in the given month  :", value)
print()


def is_valid_date(year, month, day):
    """
       Inputs:
         year  - an integer representing the year
         month - an integer representing the month
         day   - an integer representing the day
       Returns:
         True if year-month-day is a valid date and
         False otherwise
    """
    valid = True

    try:
        datetime.datetime(int(year),
                          int(month), int(day))

    except ValueError:
        valid = False

    if valid:
        return True
    else:
        return False


values = is_valid_date(year=2001, month=2,  day=29)
print("date is valid", values)
print()


def days_between(year1, month1, day1, year2, month2, day2):
    """
      Inputs:
        year1  - an integer representing the year of the first date
        month1 - an integer representing the month of the first date
        day1   - an integer representing the day of the first date
        year2  - an integer representing the year of the second date
        month2 - an integer representing the month of the second date
        day2   - an integer representing the day of the second date

      Returns:
        The number of days from the first date to the second date.
        Returns 0 if either date is invalid or the second date is
        before the first date.
      """
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    differ = (date2-date1).days
    if date2 > date1:
        return differ
    else:
        return 0


print("Days between two dates:", days_between(2006, 5, 31, 2020, 7, 15))
print()


def age_in_days(year, month, day):
    """
       Inputs:
         year  - an integer representing the birthday year
         month - an integer representing the birthday month
         day   - an integer representing the birthday day

       Returns:
         The age of a person with the input birthday as of today.
         Returns 0 if the input date is invalid of if the input
         date is in the future.
    """
    date1 = datetime.date.today()
    date2 = datetime.date(year, month, day)
    diff = (date1-date2).days
    if date1 > date2:
        return diff
    else:
        return 0


print("age in days:", age_in_days(year=2008, month=4, day=8))
print("")
