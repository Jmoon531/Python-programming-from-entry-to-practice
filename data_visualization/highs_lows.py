#!usr/bin/env python

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'

with open(filename, 'r') as f:
	reader = csv.reader(f)
	next(reader)
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(date, 'missing data')
		else:
			dates.append(date)
			highs.append(high)
			lows.append(low)

fig = plt.figure(figsize=(16, 9))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily high temperatures, 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

'''
for index, head in enumerate(row):
	print(index, head)
'''

