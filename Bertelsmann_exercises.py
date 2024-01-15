# Write a function named readable_timedelta.
# The function should take one argument, an integer days, and return a string that says how many weeks and days that is.

def readable_timedelta(days):
    weeks = int(days / 7)
    leftover_days = int (days % 7)
    return '{} week(s) and {} day(s).'.format(weeks, leftover_days)

print(readable_timedelta(10))