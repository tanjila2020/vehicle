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
from  csv_read import times, avg_no_of_vehicles, avg_speeds
from scheduler import scheduling

####declaring and initializing arrays
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

###numeric input parameter
data_size= 1.8 #megabits
bandwidth = 1000 #in megabit per sec
edge_execution_time = 16
ap_inc = 2 # ap number increment to test
server_inc = 5  # server number increment to test the server count

for i in range(0,(len(blind_d))):

    for j in range(0,(len(times))):
        no_of_ap = 1- ap_inc
        deadline_missed = 100
        while (deadline_missed >0):
            no_of_ap += ap_inc
            transfer_rate = (bandwidth*no_of_ap)/(avg_no_of_vehicles[j])
            transfer_time = round(((data_size/transfer_rate)*1000))  # in millisecond
            res_time_var = 100
            no_of_server= 1 - server_inc
            res_time = 0
            
            while (deadline_missed >0 or res_time_var >0.05):
                no_of_server+= server_inc
                deadline_missed, res_time_temp = scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicles[j], deadlines[i,j])
                res_time_var = abs((res_time- res_time_temp )/ res_time_temp)
                res_time= res_time_temp
        
        # storing configurations
        c_ap[i,j] = no_of_ap
        c_ser[i,j] = no_of_server
        res_times[i,j] = res_time

for i in range(0,(len(blind_d))):
             