import pandas as pd
from IPython import embed
# data = pd.read_csv("5am.csv")
# last_row = data.iloc[-1:]
# print(last_row)

# print("------")

# df = pd.read_csv("11pm.csv")
# last_row2 = df.iloc[-1:]
# print(last_row2) 

# time_array = df['time'].unique()
# no_of_sec = len(time_array)
# print("no of sec:", no_of_sec)


offset = 0
#no_of_rows =6000000
no_of_rows =60000000000
time = 0
df = pd.read_csv("koln-pruned.tr",
                    skiprows=offset, nrows=no_of_rows, header=None, delimiter=' ',
                    names=['time', "name", 'x', 'y', 'speed'],
                    dtype={"time": "int64", "name": "string", "x": "float64", "y": "float64"})
offset += no_of_rows

start_time = int(df['time'].head(1))
end_time = int(df['time'].tail(1))

print(start_time)  

print(end_time)    

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

  