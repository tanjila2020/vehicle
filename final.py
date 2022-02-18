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

c_ap_avg =
c_ser_avg =

peak_aps = 
peak_sers =

data_size= 1.8 #megabits
bandwidth = 1000 #in megabit per sec
edge_execution_time = 16

for i in range(0,(len(blind_d))):
    for j in range(0,(len(times))):
        transfer_rate = (bandwidth*c_ap_avg[i])/(avg_no_of_vehicles[j])
        transfer_time = round(((data_size/transfer_rate)*1000))  # in millisecond
        no_of_ap = c_ap_avg[i]
        no_of_server = c_ser_avg[i]
        pers_d_miss, avg_res, server_util = final_scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicles[j], deadlines[i,j])

        perc_deadline_miss[i,j] = pers_d_miss
        avg_res_times[i,j] = avg_res
        utilize_servers[i,j] = server_util
        max_speed[i,j] = blind_d[i]/avg_res
        max_speed[i,j] = round(max_speed[i,j], 2)

print("percentage of deadline_miss:", perc_deadline_miss)
print("avg response time:", avg_res_times)
print("server utilization:", utilize_servers)
print("max_safe_speed:", max_speed)        






