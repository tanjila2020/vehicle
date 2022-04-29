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
from final_scheduler import final_scheduling
import time

blind_d= 14
no_of_ap= 1
no_of_server= 8
extra = 100
avg_no_of_vehicles= 411
avg_speeds= 10.31 #in meter/sec

data_size= 1.8 #megabits
bandwidth = 1000 #in megabit per sec
edge_execution_time = 16

transfer_rate = (bandwidth*no_of_ap)/(avg_no_of_vehicles)
transfer_time = math.ceil((data_size/transfer_rate)*1000)  # in millisecond
deadlines= round(((blind_d/avg_speeds)*1000))

def calc_max_safe_speed ():
    pers_d_miss, avg_res, max_res_time= final_scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicles, deadlines)
    max_safe_speed = blind_d/(max_res_time/1000) # in meter per second
    max_safe_speed = round(max_safe_speed, 3)
    return max_safe_speed
    

start_time = time.time()

# pers_d_miss, avg_res, max_res_time= final_scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicles, deadlines)
# max_safe_speed = blind_d/(max_res_time/1000) # in meter per second
# max_safe_speed = round(max_safe_speed, 3)
max_safe_speed = calc_max_safe_speed()
slowdown = max_safe_speed - avg_speeds #in meter/sec
print("slowdown", slowdown)

offset=2
extra = no_of_server* offset


while(slowdown>=0):
    avg_no_of_vehicles+= extra
    print("avg_no_of_vehicles first while loop", avg_no_of_vehicles)
    # pers_d_miss, avg_res, max_res_time= final_scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicles, deadlines)
    # max_safe_speed = blind_d/(max_res_time/1000) # in meter per second
    # max_safe_speed = round(max_safe_speed, 3)
    max_safe_speed = calc_max_safe_speed()
    slowdown_temp = max_safe_speed - avg_speeds #in meter/sec
    slowdown= slowdown_temp
    print("slowdown 1st while loop:", slowdown)

while(slowdown<0):
    extra-=1
    avg_no_of_vehicles-= 1
    print("avg_no_of_vehicles second while loop", avg_no_of_vehicles)
    # pers_d_miss, avg_res, max_res_time= final_scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicles, deadlines)
    # max_safe_speed = blind_d/(max_res_time/1000) # in meter per second
    # max_safe_speed = round(max_safe_speed, 3)
    max_safe_speed = calc_max_safe_speed()
    slowdown_temp = max_safe_speed - avg_speeds #in meter/sec
    slowdown= slowdown_temp
    print("slowdown second while loop:", slowdown)

print("extra vehicles", avg_no_of_vehicles - 250)  
print("--- %s seconds ---" % (time.time() - start_time))  


    