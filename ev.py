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

# parameter value
# average configuration
no_of_ap = 84  # parameter to calculate data size from sanaz paper
no_of_servers = 57

# peak configuration
# no_of_ap = 177# parameter to calculate data size from sanaz paper
# no_of_servers = 121
#no_of_vehicles= 25
data_height = 200  # inpixel
data_width = 300  # inpixel
bit_depth = 30  # in bit
data_size = (data_height * data_width * bit_depth) / 1000000  # in megabit (Mb)
bandwidth = 1000  # in Mbps (megabit) this is when we consider equal share(simple model to calc transfer rate)
no_of_ins = 3000  # in millions
deadline = 200
# calculating local and edge capacity
v = 7.683
o = -4558.52
freq = 2.5  # cpu frequency in GHz
no_of_cores = 1
# millons of instructions per milisecond
local_cpu_capacity = math.ceil(((v * (freq*1000) + o) * no_of_cores) * 0.001)
#local_cpu_speed = math.floor(local_cpu_speed)
local_execution_time = math.ceil(no_of_ins/local_cpu_capacity)  # in millisecond
edge_speed_factor = 15
edge_execution_time = math.ceil(local_execution_time/edge_speed_factor)  # in millisecond

print("edge execution time:", edge_execution_time)
print("local execution time:", local_execution_time)
#print("local_cpu_capacity:", local_cpu_capacity)

# read vehicle data from csv
# df = pd.read_csv('first_output.csv', index_col='#')
df = pd.read_csv('7am.csv')
csv_length = len(df)

# new column made in csv
df['transfer_time'] = None
# df['avg_response_time'] = None
# df['no_of_jobs_dropped'] = None

# finding unique timestamp to get the total no of vehicles in that time
#thresold = 900
#time_array = df['time'].unique()[:thresold]
time_array = df['time'].unique()
vehicle_name_array = df['name'].unique()
# print(vehicle_name_array)
#print('total no of vehicles', len(vehicle_name_array))
# print(time_array)
max_time = np.amax(time_array)
print('max time', max_time)
min_time = np.amin(time_array)
no_of_vehicles = len(vehicle_name_array)
#no_of_vehicles = len(df[df['time'].isin(time_array)]['name'].unique())
#no_of_vehicles= 231

temp_no_of_vehicles = math.ceil(no_of_vehicles/no_of_servers)
temp_no_of_vehicles = 3
print('no_of_vehicles', no_of_vehicles)
print('temp_no_of_vehicles', temp_no_of_vehicles)

# for a particular time, calculating transfer_time for all vehicles
# for time in time_array:
#     if (time <= min_time) and (time>= max_time):
#         # select the rows with the timestamp of sec
#         matched_loc = df.loc[df['time'] == time]
#         no_of_vehicle = matched_loc['name']

#         for i, row in df.loc[df['time'] == time].iterrows():
#             # d = row['distance']  # in kilometer
#             # # Transmission power of each vehicle in(dBm)
#             # p = random.randint(20, 30)
#             # h = 127+30*(math.log(d, (10)))  # channel gain, d is in km
#             # white_noise = 2*10**-13  # white gaussian noise in watt
#             # # data_size = np.random.uniform(0.4, 0.8) #in megabits
#             # data_size = 1.8*10**6  # in bits
#             # bandwidth = 20*10**6  # in Hz
#             # snr = p*h/white_noise
#             # n_i = (math.log((1+snr), (10)))  # uplink spectral efficiency in (bits/(sec* Hz))

#             # transfer_rate1 = (bandwidth*no_of_ap * n_i) / no_of_vehicles #(in bits per sec)
#             # transfer_rate1 = round(transfer_rate1, 2)
#             #n_i2 = (math.log((1+(p*127/white_noise)), (10)))
#             #transfer_rate2 = (bandwidth*no_of_ap)*n_i2/no_of_vehicles
#             transfer_rate2 = (bandwidth*no_of_ap)/temp_no_of_vehicles
#             #print("transfer rate1", transfer_rate1)
#             #print("transfer rate2", transfer_rate2)

#             transfer_time = math.ceil((data_size/transfer_rate2)*1000)  # in millisecond
#             df.at[i, 'transfer_time'] = transfer_time

#transfer_rate2 = (bandwidth*no_of_ap)/temp_no_of_vehicles
transfer_rate2 = (bandwidth*no_of_ap)/no_of_vehicles
transfer_time = math.ceil((data_size/transfer_rate2)*1000)  # in millisecond
print("transfer time:", transfer_time)

# print(df[1:5])
# print(edge_execution_time)
# print(local_execution_time)
# print(data_size)
# print(transfer_time)

# making vehicle class to store its attributes
vehicle = namedtuple('vehicle', 'name no_of_ins data_size edge_exe_time transfer_time period deadline')
vehicle_list = []

# for i, row in df.loc[df['time'] == time_array[0]][0:temp_no_of_vehicles].iterrows():
for name in vehicle_name_array[:temp_no_of_vehicles]:
    transfer_rate2 = (bandwidth*no_of_ap)/no_of_vehicles

    v = vehicle(
        name=name,
        no_of_ins=no_of_ins,
        data_size=data_size,
        edge_exe_time=edge_execution_time,
        transfer_time=math.ceil((data_size/transfer_rate2)*1000),
        period=0,
        deadline=deadline
    )
    vehicle_list.append(v)

print('Total vehicle count', len(vehicle_list))
# print(*vehicle_list, sep='\n')

'''
# Logic of allocation
Say, we have 5 vehicles 1, 2, 3, 4, 5.
At first all vehicles will have period starting from zero. 
Then for any particular vehicle the period for next job will be the end time of earlier job of the same vehicle.
Even if jobs miss deadline, we will keep executing them and just keep a count.

# Logic of period caculation
start time = period + transfer time
end time = start time + execution time

execution = 5
transfer = 2

job 1 
period = 0
start = 0 + 2 = 2
end = 2 + 5 = 7

job 2
period = 7
start = 7 + 2 = 9
end = 9 + 5 = 14

job 3
period = 14
start = 14 + 2 = 16
end = 16 + 5 = 21

job 4
period 21
'''


def create_queue(vehicles, time_span):
    queue = []
    queued_vehicles = namedtuple(
        'vehicle', 'name edge_exe_time start_time transfer_time end_time deadline job_no')

    period = dict()
    end = dict()
    job_no = 1
    current_time = 0

    for vehicle in vehicles:
        period[vehicle.name] = 0
        end[vehicle.name] = vehicle.transfer_time

    while (current_time < time_span):
        for vehicle in vehicles:
            vehicle_deadline = period[vehicle.name] + vehicle.deadline
            # start_time = current_time +  vehicle.transfer_time
            start_time = max(current_time, end[vehicle.name])
            end_time = start_time + vehicle.edge_exe_time
            end[vehicle.name] = vehicle.transfer_time + end_time

            qt = queued_vehicles(
                name=vehicle.name,
                edge_exe_time=vehicle.edge_exe_time,
                # time when requests arrives after transfer
                transfer_time=vehicle.transfer_time,
                start_time=start_time,
                end_time=end_time,
                deadline=vehicle_deadline,
                job_no=job_no
            )
            queue.append(qt)
            period[vehicle.name] = end_time
            current_time = end_time

        job_no += 1

    print(*queue, sep='\n')

    return queue


#span = period*temp_no_of_vehicles
span = 500
#span = sum([vehicle.period for vehicle in vehicle_list])
queue = create_queue(vehicle_list, span)
vehicle_period_map = {vehicle.name: vehicle.period for vehicle in vehicle_list}

deadline_missed_jobs = 0
data = {
    "name": [],
    "job_no": [],
    "response_time": [],
}
response_time_df = pd.DataFrame(data)
ignored_jobs_df = pd.DataFrame({"name": [], "job": []})

for vehicle in queue:
    deadline_missed = vehicle.end_time > vehicle.deadline

    response_time_df = response_time_df.append({
        'name': vehicle.name,
        'job_no': vehicle.job_no,
        'response_time': vehicle.end_time - vehicle.start_time + vehicle.transfer_time,
    }, ignore_index=True)

    if not deadline_missed:
        print(vehicle)
    else:
        deadline_missed_jobs += 1
        print('---------', vehicle)

# print(response_time_df)
average_response_time = response_time_df[['name', 'response_time']].groupby(['name']).mean()
#print('Average response time\n', average_response_time)
total_avg_res_time = response_time_df['response_time'].mean()
# response_time_df.loc[(response_time_df['name'] == 'v5') & (response_time_df['job_no'] == 5.0)]
# print(ignored_jobs_df)
ignored_job_count = ignored_jobs_df.groupby(['name']).size().reset_index(name='jobs_dropped')
#print('No of jobs dropped\n', ignored_job_count)
#avg_job_drop = ignored_jobs_df['jobs_dropped'].mean()
print('total average response time is:  ', total_avg_res_time)
total_jobs = len(queue)
total_jobs_dropped = ignored_job_count['jobs_dropped'].sum()
total_demand = (total_jobs - total_jobs_dropped) * edge_execution_time
total_transfer_time = (total_jobs - total_jobs_dropped) * transfer_time
server_utilization = total_demand/span
ap_utilization = ((((total_transfer_time)/span) * no_of_servers)/no_of_ap)
#print('Total generated jobs:', total_jobs)
print('total no of jobs dropped:', total_jobs_dropped)
#print('Average no of jobs dropped:', ignored_job_count['jobs_dropped'].mean())
print('percentage of jobs dropped:', (total_jobs_dropped/total_jobs))
print('server utilization:', server_utilization)
print('bandwidth utilization:', ap_utilization)

#print('Average no of jobs dropped:  ', avg_job_drop )

# embed()
