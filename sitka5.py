'''

import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open('sitka_weather_2018_simple.csv', 'r')

csv_file = csv.reader(open_file, delimiter = ',')

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)


mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(type(mydate))

dates = []
highs = []
lows = []


for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)
print(highs)
print(dates)


'''
'''
plt.title("Daily high temperatures, July 2018", fontsize = 16)
plt.xlabel('', fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis = "both", which = 'major', labelsize = 12)

plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)

plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

fig.autofmt_xdate()

plt.show()
'''
'''




#plt.plot(highs, c='red')
#plt.plot(lows, c = 'blue')
#plt.fill_between(dates, highs, lows, facecolor = 'blue')
#plt.title('SITKA AIRPORT, AK US')

'''
import matplotlib.pyplot as plt
import csv
from datetime import datetime


open_file = open('sitka_weather_2018_simple.csv', 'r')
filename = open('death_valley_2018_simple.csv', 'r')

csv_file = csv.reader(open_file, delimiter = ',')
file = csv.reader(filename, delimiter = ',')

header_row = next(csv_file)
header = next(file)
'''
print(type(header_row))
print(type(header))

for index, column_header in enumerate(header_row):
    print(index, column_header)
for index, column_header in enumerate(header):
    print(index, column_header)


mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(type(mydate))
'''
dates = []
highs = []
lows = []


dates2 = []
highs2 = []
lows2 = []

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)

for row in file:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f'Missing data for {the_date}')
    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(the_date)


fig = plt.figure()

plt.subplot(2,1,1)
plt.tick_params(axis = "both", which = 'major', labelsize = 12)
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
plt.title('SITKA AIRPORT, AK US')

plt.subplot(2,1,2)
plt.tick_params(axis = "both", which = 'major', labelsize = 12)
plt.plot(dates2, highs2, c = 'red', alpha = 0.5)
plt.plot(dates2, lows2, c = 'blue', alpha = 0.5)
plt.fill_between(dates2, highs2, lows2, facecolor = 'blue', alpha = 0.1)
plt.title('DEATH VALLEY, CA US')

plt.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")

plt.show()



