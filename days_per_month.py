# days per month
year = int(input())
month = int(input())
list31 = [1, 3, 5, 7, 8, 10, 12]
list30 = [4, 6, 9, 11]
if month in list31:
    print("31")
elif month in list30:
    print("30")
elif month == 2 and year % 4 == 0 and year % 100 != 0:
    print('29')
else:
    print('28')
