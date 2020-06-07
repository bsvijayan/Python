from datetime import datetime
from matplotlib import pyplot as plt

datetime_mystr = '03/06/2020 00:00:00:2012'
datetime_mystr1 = '03/07/2020 00:00:00:203'
datetime_mystr2 = '04/06/2020 12:00:00:2533'


datetime_object = datetime.strptime(datetime_mystr, '%d/%m/%Y %H:%M:%S:%f')
datetime_object = datetime.strptime(datetime_mystr1, '%d/%m/%Y %H:%M:%S:%f')
datetime_object = datetime.strptime(datetime_mystr2, '%d/%m/%Y %H:%M:%S:%f')
x_values=[datetime_mystr,datetime_mystr1,datetime_mystr2]
y_values=[100,0,2000]
print(datetime_object)  # printed in default format
print(datetime_mystr)
plt.plot(x_values,y_values)f