import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,highs,lows = [],[],[]
    for row in reader:

        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


 



fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.2)

plt.plot(dates,lows,c='blue',alpha=0.2)
plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.5)

plt.title("Daily high and low temperatures-2014\nDath Valley,CA",fontsize = 20)
plt.xlabel('',fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize = 16)
plt.savefig('Daily high temperatures6.png',bbox_inches='tight')
plt.show()