import math
from collections import namedtuple
from functools import reduce
from random import shuffle
from IPython import embed

no_of_servers = 3
no_of_ap = 10
no_of_vehicles = 5
data_height = 200  # inpixel
data_width = 300  # inpixel
bit_depth = 30  # in bit
data_size = (data_height * data_width * bit_depth) / 1000000  # in megabit (Mb)
bandwidth = 1000  # in Mbps (megabit)
no_of_ins = 1000  # in millions
period = 40
deadline = period

# calculating local and edge capacity
v = 7.683
o = -4558.52
freq = 2.5  # cpu frequency in GHz
no_of_cores = 1
# millons of instructions per milisecond
local_cpu_capacity = math.ceil(((v * (freq*1000) + o) * no_of_cores) * 0.001)
#local_cpu_speed = math.floor(local_cpu_speed)
local_execution_time = math.ceil(
    no_of_ins/local_cpu_capacity)  # in millisecond
edge_speed_factor = 7
edge_execution_time = math.ceil(
    local_execution_time/edge_speed_factor)  # in millisecond

# calculating transfer time
transfer_rate = (bandwidth*no_of_ap)/no_of_vehicles
transfer_time = math.ceil((data_size/transfer_rate)*1000)  # in millisecond

# print(edge_execution_time)
# print(local_execution_time)
# print(data_size)
# print(transfer_time)

vehicle = namedtuple(
    'vehicle', 'name no_of_ins data_size edge_exe_time transfer_time period deadline')
vehicle_list = []

for i in range(1, no_of_vehicles + 1):
    v = vehicle(
        name=f'v{i}',
        no_of_ins=no_of_ins,
        data_size=data_size,
        edge_exe_time=edge_execution_time,
        transfer_time=transfer_time,
        period=period,
        deadline=deadline
    )
    vehicle_list.append(v)


def create_queue(vehicles, time_span):
    queue = []
    queued_vehicles = namedtuple(
        'vehicle', 'name edge_exe_time start_time transfer_time deadline job_no')

    for vehicle in vehicles:
        for i in range(0, time_span + 1 - vehicle.period, vehicle.period):
            vehicle_deadline = i + vehicle.deadline
            qt = queued_vehicles(
                name=vehicle.name,
                edge_exe_time=vehicle.edge_exe_time,
                # time when requests arrives after transfer
                start_time=i + vehicle.transfer_time,
                transfer_time=vehicle.transfer_time,
                deadline=vehicle_deadline,
                job_no=None
            )
            queue.append(qt)

    queue = sorted(queue, key=lambda qt: (qt.deadline, qt.start_time))
    vehicle_counter = []

    for i in range(len(queue)):
        vehicle_counter.append(queue[i].name)
        task_count = vehicle_counter.count(queue[i].name)
        queue[i] = queue[i]._replace(job_no=task_count)
    # embed()
    for i in range(0, len(queue), no_of_vehicles):
        sublist = queue[i: i + no_of_vehicles]
        shuffle(sublist)
        queue[i: i + no_of_vehicles] = sublist
    # print(queue)
    return queue


span = sum([vehicle.period for vehicle in vehicle_list])
queue = create_queue(vehicle_list, span)
vehicle_period_map = {vehicle.name: vehicle.period for vehicle in vehicle_list}
cpu_current_time = 0
discarded_job = []

for vehicle in queue:
    if vehicle.name in discarded_job:
        print(discarded_job)
        print('ignored ', vehicle)
        discarded_job.remove(vehicle.name)
        continue

    vehicle = vehicle._replace(start_time=max(
        vehicle.start_time, cpu_current_time))
    vehicle_end_time = vehicle.start_time + vehicle.edge_exe_time
    deadline_missed = vehicle_end_time > vehicle.deadline

    Job = namedtuple(
        'Job', 'name start_time edge_exe_time end_time deadline deadline_missed job_no')

    job = Job(name=vehicle.name,
              start_time=vehicle.start_time,
              edge_exe_time=vehicle.edge_exe_time,
              end_time=vehicle_end_time,
              deadline=vehicle.deadline,
              deadline_missed=deadline_missed,
              job_no=vehicle.job_no)

    if not deadline_missed:
        period = (vehicle.job_no - 1) * vehicle_period_map[vehicle.name]
        #response_time = vehicle_end_time - period
        cpu_current_time = vehicle_end_time
        print(job)
    else:
        period = (vehicle.job_no - 1) * vehicle_period_map[vehicle.name]
        #response_time = vehicle_end_time - period
        cpu_current_time = vehicle_end_time
        discarded_job.append(job.name)
        print('---------', job)
