

import pandas as pd
from IPython import embed
import math
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

clock = ["12am.csv", "1am.csv", "2am.csv", "3am.csv", "4am.csv", "5am.csv", "6am.csv", "7am.csv", "8am.csv", "9am.csv",
 "10am.csv", "11am.csv", "12pm.csv", "1pm.csv", "2pm.csv", "3pm.csv", "4pm.csv", "5pm.csv", "6pm.csv", "7pm.csv", "8pm.csv", "9pm.csv", "10pm.csv", "11pm.csv"]
avg_no_of_vehicles= []
for clk in clock:
        # read vehicle data from csv
        # df = pd.read_csv('first_output.csv', index_col='#')
        df = pd.read_csv(clk)
        no_of_vehicles = 0
        interval = 180
        total_vehicles= 0
        start = df["time"].iloc[0]
        end = df["time"].iloc[-1]

        start_times= []
        end_times =[]
        


        for start_time in range(start, end, interval):
            start_times.append(start_time)
            end_time= start_time + (interval-1)
            end_times.append(end_time)
        print("end times are:", end_times)  
        print("start times are:", start_times)
        no_of_intervals = len(start_times)

        for i in range(0, no_of_intervals):
            total_vehicle_df = df.loc[(df['time'] >= start_times[i]) & (df['time'] <= end_times[i])]
            total_vehicles += len(total_vehicle_df['name'].unique())
            print(total_vehicles)
        

        no_of_vehicles += total_vehicles/no_of_intervals 
        no_of_vehicles = round(no_of_vehicles)
        
        print ("avg no of vehicles:", no_of_vehicles)
        avg_no_of_vehicles.append(no_of_vehicles)

# avg_no_of_vehicles.append(no_of_vehicles)
print("avg no of vehicle array is", avg_no_of_vehicles)

df2 = pd.DataFrame({'Time of the day':clock,
                   'average numebr of vehicles':avg_no_of_vehicles})

writer = ExcelWriter('avg_number of vehicles.xlsx')
df2.to_excel(writer,'Sheet1',index=False)
writer.save()

