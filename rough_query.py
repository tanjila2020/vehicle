import pandas as pd
from IPython import embed
data = pd.read_csv("8am.csv")
last_row = data.iloc[-1:]
print(last_row)

# filtered = data.query('time >=28874 and time<= 29104+180')
# vehicle_name_array = filtered['name'].unique()
# print('total no of vehicles', len(vehicle_name_array))
######## to calc avg no of vehicles in that excel file#####
# avg = 0
# for t in range(28874, 28893):
#     tb1 = data.query('time==@t')
#     tb2 = data.query('time==@t+180')
#     a = set(tb1['name'])
#     b = set(tb2['name'])
#     c = a-b
#     avg = avg+(len(c)/len(a))*100
# print (avg)

  