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
from final_scheduler import final_scheduling

####declaring and initializing arrays
#for test:
#blind_d = [x for x in range(2, 5, 2)]
blind_d = [x for x in range(2, 17, 2)]
deadlines = np.zeros((len(blind_d), len(times)))
perc_deadline_miss = np.zeros((len(blind_d), len(times)))
max_speed = np.zeros((len(blind_d), len(times))) 
utilize_servers = np.zeros((len(blind_d), len(times))) 
avg_res_times = np.zeros((len(blind_d), len(times)))

#calc deadlines
for i in range(0,(len(blind_d))):
    for j in range(0,(len(times))):
        deadlines[i, j] = round(((blind_d[i]/avg_speeds[j])*1000))


c_ap_avg= np.genfromtxt('avg_ap.csv', delimiter=",")
c_ser_avg= np.genfromtxt('avg_server.csv', delimiter=",")

c_ap= np.genfromtxt('config_ap1.csv', delimiter=",")
c_ser= np.genfromtxt('config_server1.csv', delimiter=",")

peak_aps = (c_ap.max(axis=1))
peak_sers = (c_ser.max(axis=1))







   
# exit()   






data_size= 1.8 #megabits
bandwidth = 1000 #in megabit per sec
edge_execution_time = 16

for i in range(0,(len(blind_d))):
    for j in range(0,(len(times))):
        print("blind distance: ", i)
        print("time: ", j)
        transfer_rate = (bandwidth*c_ap_avg[i])/(avg_no_of_vehicles[j])
        transfer_time = np.round(((data_size/transfer_rate)*1000))  # in millisecond
        no_of_ap = c_ap_avg[i]
        no_of_server = c_ser_avg[i]
        pers_d_miss, avg_res, server_util = final_scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicles[j], deadlines[i,j])

        perc_deadline_miss[i,j] = pers_d_miss
        avg_res_times[i,j] = avg_res
        utilize_servers[i,j] = server_util
        max_speed[i,j] = blind_d[i]/avg_res
        max_speed[i,j] = round(max_speed[i,j], 3)


#writing all the results in csv files
dff1= pd.DataFrame(perc_deadline_miss)
dff2= pd.DataFrame(avg_res_times)
dff3= pd.DataFrame(utilize_servers)
dff4= pd.DataFrame(max_speed)


print(dff4)

dff1.to_csv('percentage_deadline_miss_avg.csv')
dff2.to_csv('avg_response_avg.csv')
dff3.to_csv('server_utilization_avg.csv')
dff4.to_csv('max_safe_speed_avg.csv')


print("percentage of deadline_miss:", perc_deadline_miss)
print("avg response time:", avg_res_times)
print("server utilization:", utilize_servers)
print("max_safe_speed:", max_speed)        






