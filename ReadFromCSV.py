from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
data = pd.read_csv(r'C:\Users\Public\samp.csv')
df = pd.DataFrame(data, columns= ['Response','Duration'])

data['time'] = pd.to_datetime(df['Response'], format="%d/%m/%Y %H:%M:%S:%f")
#x_values = [datetime.datetime.strptime(d,"%d/%m/%Y %H:%M:%S:%f").date() for d in data['time']]
print(data['time'])

duration = data['Duration']
#plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m/%Y %H:%M:%S:%f"))

plt.plot(data['time'], duration, linestyle='solid')
ax = plt.gca()

formatter = mdates.DateFormatter("%d/%m %H")

ax.xaxis.set_major_formatter(formatter)


plt.title('Timeout Summary')
plt.xlabel('TIme Stamp')
plt.ylabel('Timeouts')

plt.tight_layout()

plt.show()

#x_values=datetime.strptime(years,'%d/%m/%Y %H:%M:%S:%f')
#x_values=datetime.strptime(data.columns.str.strip('response'), '%d/%m/%Y %H:%M:%S:%f'))f