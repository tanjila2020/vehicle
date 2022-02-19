from datetime import time
import math
import numpy as np
from collections import namedtuple
from functools import reduce
from random import shuffle
import random
from IPython import embed
from numpy.lib.function_base import piecewise
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pyrsistent import v
from  csv_read import times, avg_no_of_vehicles, avg_speeds
from scheduler import scheduling

####declaring and initializing arrays
#for test:
#blind_d = [x for x in range(2, 5, 2)]
blind_d = [x for x in range(2, 17, 2)]
deadlines = np.zeros((len(blind_d), len(times)))
c_ap = np.zeros((len(blind_d), len(times)))
c_ser = np.zeros((len(blind_d), len(times)))
res_times = np.zeros((len(blind_d), len(times)))





#calc deadlines
for i in range(0,(len(blind_d))):
    for j in range(0,(len(times))):
        deadlines[i, j] = round(((blind_d[i]/avg_speeds[j])*1000))

peak_vehicle_no = max(avg_no_of_vehicles)
peak_time = avg_no_of_vehicles.index(peak_vehicle_no) #returns the index of the times array having max avg vehicle
# peak_time=2
###numeric input parameter
data_size= 1.8 #megabits
bandwidth = 1000 #in megabit per sec
edge_execution_time = 16
ap_inc = 2 # ap number increment to test
server_inc = 5  # server number increment to test the server count

for i in range(0,(len(blind_d))):
    print("current blind_distance", i)

    for j in range(0,(len(times))):
        print("current time of the day:", j)
        no_of_ap = 1- ap_inc
        deadline_missed = 100
        while (deadline_missed >0):
            no_of_ap += ap_inc
            transfer_rate = (bandwidth*no_of_ap)/(avg_no_of_vehicles[j])
            transfer_time = round(((data_size/transfer_rate)*1000))  # in millisecond
            res_time_var = 100
            no_of_server= 1 - server_inc
            res_time = 0
            print("in 1st while loop")
            
            while (deadline_missed >0 and res_time_var >0.03):
                no_of_server+= server_inc
                deadline_missed, res_time_temp = scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicles[j], deadlines[i,j])
                res_time_var = abs((res_time- res_time_temp )/ res_time_temp)
                res_time= res_time_temp
                print("in 2nd while loop")
        
        # storing configurations
        c_ap[i,j] = no_of_ap
        c_ser[i,j] = no_of_server
        res_times[i,j] = res_time



# #finding peak and avg configuration
peak_aps=[]
peak_sers= []
c_ap_avg= []
c_ser_avg= []

for i in range(0,(len(blind_d))):
    p_ap = c_ap[i,peak_time]
    peak_aps.append(p_ap)
    p_ser = c_ser [i,peak_time]
    peak_sers.append(p_ser)







c_ap_avg = np.round(c_ap.mean(axis=1))
c_ser_avg = np.round(c_ser.mean(axis=1))

print("peak ap:", peak_aps)
print("peak server:", peak_sers)
print("average ap", c_ap_avg)
print("average server", c_ser_avg)



#writing all the results in csv files
df1= pd.DataFrame(c_ap)
df2= pd.DataFrame(c_ser)
df3= pd.DataFrame(res_times)
df4= pd.DataFrame(c_ap_avg)
df5 = pd.DataFrame(c_ser_avg) 
df6 = pd.DataFrame(peak_aps)
df7= pd.DataFrame(peak_sers)

print(df7)

df1.to_csv('config_ap.csv')
df2.to_csv('config_server.csv')
df3.to_csv('response_times.csv')
df4.to_csv('avg_ap.csv')
df5.to_csv('avg_server.csv')
df6.to_csv('peak_ap.csv')
df7.to_csv('peak server.csv')
    
