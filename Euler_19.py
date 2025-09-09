# Problem 19
# Counting Sundays
# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def euler_19():
    # Days in each month (non-leap year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = 1  # 1 Jan 1900 was a Monday, so day 1
    count = 0

    for year in range(1900, 2001):
        for month in range(12):
            if year >= 1901 and day % 7 == 0:
                count += 1
            # Add days in current month to the day counter
            if month == 1 and is_leap(year):
                day += 29
            else:
                day += month_days[month]

    return count

print(euler_19())