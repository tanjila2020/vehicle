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
#from  csv_read import times, avg_no_of_vehicles, avg_speeds
from scheduler import scheduling
times= [20]
blind_d = [8]
deadlines = 641
c_ap = np.zeros((len(blind_d), len(times)))
c_ser = np.zeros((len(blind_d), len(times)))
res_times = np.zeros((len(blind_d), len(times)))


avg_no_of_vehicles = 637
data_size= 1.8 #megabits
bandwidth = 1000 #in megabit per sec
edge_execution_time = 16
ap_inc = 2 # ap number increment to test
server_inc = 2 

for i in range(0,(len(blind_d))):

    for j in range(0,(len(times))):
        no_of_ap = 1- ap_inc
        deadline_missed = 100
        while (deadline_missed >0):
            no_of_ap += ap_inc
            transfer_rate = (bandwidth*no_of_ap)/(avg_no_of_vehicles)
            transfer_time = round(((data_size/transfer_rate)*1000))  # in millisecond
            res_time_var = 100
            no_of_server= 1 - server_inc
            res_time = 0
            print("in 1st while loop")
            
            while (deadline_missed >0 and res_time_var >0.05):
                no_of_server+= server_inc
                deadline_missed, res_time_temp = scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicles, deadlines)
                print("current response_time from scheduler:", res_time_temp)
                print("--------")
                print("previous response_time from scheduler :", res_time)
                res_time_var = abs((res_time- res_time_temp )/ res_time_temp)
                print("current res time variation:", res_time_var)
                res_time= res_time_temp
                print("in 2nd while loop")
        
            print("out of second while loop")
        print("out of 1st while loop")    
        # storing configurations
        c_ap[i,j] = no_of_ap
        c_ser[i,j] = no_of_server
        res_times[i,j] = res_time

print("config server", c_ser)
print("config ap", c_ap)
