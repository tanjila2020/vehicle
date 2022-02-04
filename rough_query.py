import pandas as pd
from IPython import embed
data = pd.read_csv("7am.csv")
# filtered = data.query('time >=28874 and time<= 29104+180')
# vehicle_name_array = filtered['name'].unique()
# print('total no of vehicles', len(vehicle_name_array))
avg = 0
for t in range(28874, 29104):
    tb1 = data.query('time==@t')
    tb2 = data.query('time==@t+180')
    a = set(tb1['name'])
    b = set(tb2['name'])
    c = a-b
    #avg = avg+(len(c)/len(a))*100
print (tb1)
  