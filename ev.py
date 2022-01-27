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
no_of_ap = 2  # parameter to calculate data size from sanaz paper
no_of_servers = 4

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
# deadline = 200 #deadline is calculated later at line 52
blind_distance = 2  # in meters

# calculating local and edge capacity
v = 7.683
o = -4558.52
freq = 2.5  # cpu frequency in GHz
no_of_cores = 1
# millons of instructions per milisecond
local_cpu_capacity = math.ceil(((v * (freq*1000) + o) * no_of_cores) * 0.001)
#local_cpu_speed = math.floor(local_cpu_speed)
local_execution_time = math.ceil(no_of_ins/local_cpu_capacity)  # in millisecond
edge_speed_factor = 13
edge_execution_time = math.ceil(local_execution_time/edge_speed_factor)  # in millisecond
edge_execution_time = [16, 32]#, 48]
clock = ["1am.csv", "5am.csv"]#, "3am.csv", "4am.csv", "5am.csv", "6am.csv"]

result_csv = pd.DataFrame({
    "time_of_the_day": [],
    "edge_exe_time": [],
    "avg_response_time": [],
    "percentage_of_d_miss_jobs": [],
    "server_utilization": [],
})


for eet in edge_execution_time:
    print("edge execution time:", eet)
    print("local execution time:", local_execution_time)
    #print("local_cpu_capacity:", local_cpu_capacity)

    for clk in clock:
        # read vehicle data from csv
        # df = pd.read_csv('first_output.csv', index_col='#')
        df = pd.read_csv(clk)
        csv_length = len(df)
        avg_speed = df['speed'].mean()
        #avg_speed = 9
        print('average speed: ' + str(avg_speed))
        deadline = math.ceil((blind_distance/avg_speed) * 1000)  # in millisecond
        print('deadline:', deadline)
        print('data size:', data_size)

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
        temp_no_of_vehicles = round(no_of_vehicles/no_of_servers)
        if temp_no_of_vehicles == 0:
            temp_no_of_vehicles = 1
        #temp_no_of_vehicles = 2
        print('no_of_vehicles', no_of_vehicles)
        print('temp_no_of_vehicles', temp_no_of_vehicles)
        #transfer_rate2 = (bandwidth*no_of_ap)/temp_no_of_vehicles
        transfer_rate2 = (bandwidth*no_of_ap)/no_of_vehicles
        transfer_time = math.ceil((data_size/transfer_rate2)*1000)  # in millisecond
        print("transfer time:", transfer_time)

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
                edge_exe_time=eet,
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

        # transfer time calculation
        say we have two vehicles
        for v1 transfer_time = 10 execution_time = 2
        for v2 transfer_time = 10 execution_time = 3
        the job schedule should be like below:

        10-(v1 j1)-12 12-(v2 j1)-15 22-(v1 j2)-24 24-(v2 j2)-28 
        34-(v1 j3)-36 38-(v2 j3)-41
        '''

        #span = period*temp_no_of_vehicles
        span = 70000
        #span = sum([vehicle.period for vehicle in vehicle_list])
        queue = []
        queued_vehicles = namedtuple(
            'vehicle',
            'name edge_exe_time start_time transfer_time end_time deadline job_no')
        period = dict()
        end = dict()
        job_no = 1
        current_time = 0
        deadline_missed_jobs = 0
        data = {
            "name": [],
            "job_no": [],
            "response_time": [],
        }
        response_time_df = pd.DataFrame(data)
        ignored_jobs_df = pd.DataFrame({"name": [], "job": []})

        for vehicle in vehicle_list:
            period[vehicle.name] = 0
            end[vehicle.name] = vehicle.transfer_time

        while (current_time < span):
            for vehicle in vehicle_list:
                vehicle_deadline = period[vehicle.name] + vehicle.deadline
                # start_time = current_time +  vehicle.transfer_time
                start_time = max(current_time, end[vehicle.name])
                end_time = start_time + vehicle.edge_exe_time
                prev_end_time = end[vehicle.name] - vehicle.transfer_time
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

                # calculate missed jobs
                deadline_missed = qt.end_time > qt.deadline

                response_time_df = response_time_df.append({
                    'name': qt.name,
                    'job_no': qt.job_no,
                    'response_time': qt.end_time - prev_end_time,
                }, ignore_index=True)

                if not deadline_missed:
                    # print(qt)
                    pass
                else:
                    deadline_missed_jobs += 1
                    #print('---------', qt)

            job_no += 1

        #print(*queue, sep='\n')

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
        print('no of jobs missing deadline:', deadline_missed_jobs)
        total_jobs = len(queue)
        #print ('total jobs:', total_jobs)
        #total_jobs_dropped = ignored_job_count['jobs_dropped'].sum()
        #total_demand = (total_jobs - total_jobs_dropped) * eet
        total_demand = (total_jobs) * eet
        #total_transfer_time = (total_jobs - total_jobs_dropped) * transfer_time
        server_utilization = total_demand/span
        #ap_utilization = ((((total_transfer_time)/span) * no_of_servers)/no_of_ap)
        #print('Total generated jobs:', total_jobs)
        #print('total no of jobs dropped:', total_jobs_dropped)
        #print('Average no of jobs dropped:', ignored_job_count['jobs_dropped'].mean())
        #print('percentage of jobs dropped:', (total_jobs_dropped/total_jobs))
        print('percentage of jobs missing deadline:', (deadline_missed_jobs/total_jobs))
        print('server utilization:', server_utilization)
        #print('bandwidth utilization:', ap_utilization)

        #print('Average no of jobs dropped:  ', avg_job_drop )

        result_csv = result_csv.append({
            "time_of_the_day": clk,
            "edge_exe_time": eet,
            "avg_response_time": total_avg_res_time,
            "percentage_of_d_miss_jobs": (deadline_missed_jobs/total_jobs),
            "server_utilization": server_utilization,
        }, ignore_index=True)
        # embed()

result_csv.to_csv(f"result_{blind_distance}.csv")