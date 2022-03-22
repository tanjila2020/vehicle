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
import math
from collections import namedtuple
from functools import reduce
from random import shuffle
import random
from  csv_read import times, avg_no_of_vehicles, avg_speeds

def final_scheduling(no_of_ap, no_of_server, transfer_time, edge_execution_time, avg_no_of_vehicle, deadline):
    temp_no_of_vehicles = int(math.ceil(avg_no_of_vehicle/no_of_server))#finding the no of vehicles per server
    if temp_no_of_vehicles == 0:
        temp_no_of_vehicles=1
    #temp_no_of_vehicles = 2
    print ("temp no of vehicles:", temp_no_of_vehicles)
    df = pd.read_csv('7am.csv')
    vehicle_name_array = df['name'].unique()
    # making vehicle class to store its attributes
    vehicle = namedtuple('vehicle', 'name edge_exe_time transfer_time period deadline')
    vehicle_list = []

    # for i, row in df.loc[df['time'] == time_array[0]][0:temp_no_of_vehicles].iterrows():
    for name in vehicle_name_array[:temp_no_of_vehicles]:

        v = vehicle(
            name=name,
            # no_of_ins=no_of_ins,
            # data_size=data_size,
            edge_exe_time=edge_execution_time,
            transfer_time=transfer_time,
            period=0,
            deadline=deadline
        )
        vehicle_list.append(v)

    #span = period*temp_no_of_vehicles
    span = 60000 #in ms (1min)
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
    flag=0
    while (current_time < span):
        if flag == 1:
            break
        for vehicle in vehicle_list:
            vehicle_deadline = period[vehicle.name] + vehicle.deadline
            # start_time = current_time +  vehicle.transfer_time
            start_time = max(current_time, end[vehicle.name])
            if start_time > span-edge_execution_time:
                flag=1
                break
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
                #print(qt)
                pass
            else:
                deadline_missed_jobs += 1
                #print('---------', qt)

        job_no += 1
    if deadline_missed_jobs == 1:
        deadline_missed_jobs = 0
    #print(*queue, sep='\n')

    
    average_response_time = response_time_df[['name', 'response_time']].groupby(['name']).mean()
    total_avg_res_time = response_time_df['response_time'].mean()
    max_response_time = response_time_df['response_time'].max()
    # response_time_df.loc[(response_time_df['name'] == 'v5') & (response_time_df['job_no'] == 5.0)]
    # print(ignored_jobs_df)
    ignored_job_count = ignored_jobs_df.groupby(['name']).size().reset_index(name='jobs_dropped')
    #print('No of jobs dropped\n', ignored_job_count)
    #avg_job_drop = ignored_jobs_df['jobs_dropped'].mean()
    # print('total average response time is:  ', total_avg_res_time)
    # print('no of jobs missing deadline:', deadline_missed_jobs)
    total_jobs = len(queue)
    #print ('total jobs:', total_jobs)
    #total_jobs_dropped = ignored_job_count['jobs_dropped'].sum()
    #total_demand = (total_jobs - total_jobs_dropped) * edge_execution_time
    total_demand = (total_jobs) * edge_execution_time
    #total_transfer_time = (total_jobs - total_jobs_dropped) * transfer_time
    server_utilization = total_demand/span
    if no_of_server > avg_no_of_vehicle:
        server_utilization= (avg_no_of_vehicle * server_utilization)/no_of_server
    
    if server_utilization > 1:
        server_utilization = 1
    
    server_utilization = round(server_utilization, 4)
     

    percent_deadline_missed_jobs = (deadline_missed_jobs/total_jobs) 
    percent_deadline_missed_jobs = round(percent_deadline_missed_jobs, 7)  
    #ap_utilization = ((((total_transfer_time)/span) * no_of_servers)/no_of_ap)
    #print('Total generated jobs:', total_jobs)
    #print('total no of jobs dropped:', total_jobs_dropped)
    #print('Average no of jobs dropped:', ignored_job_count['jobs_dropped'].mean())
    #print('percentage of jobs dropped:', (total_jobs_dropped/total_jobs))
    #max_safe_speed = blind_distance/(total_avg_res_time/1000)
    # print('percentage of jobs missing deadline:', (deadline_missed_jobs/total_jobs))
    # print('server utilization:', server_utilization)
    print("----end----")
    #print('max safe speed:', max_safe_speed)

    # return percent_deadline_missed_jobs, total_avg_res_time, max_response_time, server_utilization
    return percent_deadline_missed_jobs, total_avg_res_time, max_response_time