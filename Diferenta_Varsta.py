import datetime

# datetime(year, month, day, hour, minute, second)
a = datetime.datetime(2021, 12, 19, 12, 38, 30)


print("Varsta Dvs :)")
print("Formatul acceeptat: An Luna Zi Ora Minut: ")
date_time_str1 = input( )
date_time_obj = datetime.datetime.strptime(date_time_str1, '%Y %m %d %H %M')
print(date_time_obj)

# returns a timedelta object
c = a-date_time_obj
print('Difference: ', c)

minutes = c.total_seconds() / 60

# returns the difference of the time of the day
years = minutes / 60 / 24 / 364
print('Difference in years: ', int(years), 'ani')
