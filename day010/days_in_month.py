def is_leap(year):
    if year % 4 == 0:
        return year % 100 == 0 and year % 400 == 0 or year % 100 != 0
    else:
        return False


def days_in_month(year, month):
    if month > 12 and month < 1:
        return "Please enter a valid month."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return 29 if month == 2 and is_leap(year) else month_days[month - 1]


# 🚨 Do NOT change any of the code belo 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
