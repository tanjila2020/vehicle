
import numpy as np
import random
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure



plt.rcParams['font.size'] = '13'
plt.rcParams['lines.markersize'] = 9
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["legend.columnspacing"]=0.5
plt.rcParams["legend.handletextpad"]=0.2
plt.rcParams["legend.labelspacing"]=0.5
plt.rcParams["legend.borderpad"]=0.1
plt.rcParams["legend.borderaxespad"]=-0.2

fig, ax = plt.subplots()


#schedulability ratio from real data


#blind distance
x1= [2, 4, 6, 8, 10, 12, 14, 16]

###########code for response time
# y1= [0.195545455,0.21931329,0.263449096,0.260506822,0.277184478,0.281759635,0.306418792,0.260986795 ]
# y2= [0.646200349,0.571876458,0.609965971,0.597774037,0.591202479,0.612217653,0.584061904,0.572208436]
# y3= [0.541063761,0.50327401,0.528508355,0.54598863,0.542155027,0.533922786,0.510866265,0.530778681]

# plt.plot(x1, y1, color='k', linestyle='dashdot',  marker='o', markerfacecolor='0.8', label = "low traffic")
# plt.plot(x1, y2, color='blue', marker='^', linestyle='--', markerfacecolor='0.8', label = "morderate traffic")
# plt.plot(x1, y3, color='red', marker='x', linestyle='-', markerfacecolor='0.8', label = "heavy traffic")
# # plt.xlim(109, 201)
# # plt.ylim(0, 1)
# plt.xlabel("blind distance (in meters)")
# #plt.ylabel("No of jobs dropped ")
# plt.ylabel("Average response time (in milliseconds)")
# right_side = ax.spines["right"]
# right_side.set_visible(False)
# top_side = ax.spines["top"]
# top_side.set_visible(False)

# plt.legend()
# plt.margins(0.02)
# # plt.savefig("D:\vehicle_graphs\response_time.pdf", dpi=300, bbox_inches = 'tight')
# plt.show()


####################code for percentage of deadline miss
# y1= [0,0,0,0,0,0,0,0 ]
# y2= [0,0.000152343,0.000228571,0.000229,0.000228629,0,0.000228943,0]
# y3= [0.998734575,0.376335288,0.377137438,0.254174038,0.254984938,0.254324313,0.256435988,0.255327488]

# plt.plot(x1, y1, color='k', linestyle='dashdot',  marker='o', markerfacecolor='0.8', label = "low traffic")
# plt.plot(x1, y2, color='blue', marker='^', linestyle='--', markerfacecolor='0.8', label = "morderate traffic")
# plt.plot(x1, y3, color='red', marker='x', linestyle='-', markerfacecolor='0.8', label = "heavy traffic")
# # plt.xlim(109, 201)
# # plt.ylim(0, 1)
# plt.xlabel("blind distance (in meters)")
# #plt.ylabel("No of jobs dropped ")
# plt.ylabel("Average percentage of deadline missed jobs")
# right_side = ax.spines["right"]
# right_side.set_visible(False)
# top_side = ax.spines["top"]
# top_side.set_visible(False)

# plt.legend()
# plt.margins(0.02)
# # plt.savefig("D:\vehicle_graphs\response_time.pdf", dpi=300, bbox_inches = 'tight')
# plt.show()
############# max safe speed for avg config########
# y1= [74.08088889,143.225,202.089,260.3672222,314.2938889,376.3761111,420.3466667,481.6011111 ]
y2= [5.119,10.68971429,13.32114286,15.37714286,15.85542857,16.41157143,16.00628571,17.491]
y3= [-3.776125,-0.685625,0.847375,1.31775,1.803125,1.982625,1.8055,2.497625]

# plt.plot(x1, y1, color='k', linestyle='dashdot',  marker='o', markerfacecolor='0.8', label = "low traffic")
plt.plot(x1, y2, color='blue', marker='^', linestyle='--', markerfacecolor='0.8', label = "morderate traffic")
plt.plot(x1, y3, color='red', marker='x', linestyle='-', markerfacecolor='0.8', label = "heavy traffic")
# plt.xlim(109, 201)
# plt.ylim(0, 1)
plt.xlabel("blind distance (in meters)")
#plt.ylabel("No of jobs dropped ")
plt.ylabel("Difference of max safe speed and avg speed(with avg config)")
right_side = ax.spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)

plt.legend()
plt.margins(0.02)
# plt.savefig("D:\vehicle_graphs\response_time.pdf", dpi=300, bbox_inches = 'tight')
plt.show()

############# max safe speed for peak config########
# y1= [74.08088889,143.225,202.089,260.3672222,314.2938889,376.3761111,420.3466667,481.6011111 ]
# y2= [5.119,10.68971429,13.32114286,15.37714286,15.85542857,16.41157143,16.00628571,17.491]
# y3= [-3.776125,-0.685625,0.847375,1.31775,1.803125,1.982625,1.8055,2.497625]

# plt.plot(x1, y1, color='k', linestyle='dashdot',  marker='o', markerfacecolor='0.8', label = "low traffic")
# plt.plot(x1, y2, color='blue', marker='^', linestyle='--', markerfacecolor='0.8', label = "morderate traffic")
# plt.plot(x1, y3, color='red', marker='x', linestyle='-', markerfacecolor='0.8', label = "heavy traffic")
# # plt.xlim(109, 201)
# # plt.ylim(0, 1)
# plt.xlabel("blind distance (in meters)")
# #plt.ylabel("No of jobs dropped ")
# plt.ylabel("Difference of max safe speed and avg speed(with avg config)")
# right_side = ax.spines["right"]
# right_side.set_visible(False)
# top_side = ax.spines["top"]
# top_side.set_visible(False)

# plt.legend()
# plt.margins(0.02)
# # plt.savefig("D:\vehicle_graphs\response_time.pdf", dpi=300, bbox_inches = 'tight')
# plt.show()
######## plot for transfer rates
# y1= [215.9486046,205.5271401,202.0516163,200.544779,199.9906088,199.750898,200.009296,200.009296]
# y2= [48.31309811,15.05354932,10.15266687,7.381505577,6.473908812,5.636085825,4.693239391,4.045157826]
# y3= [60.71149136,17.49981074,9.469097229,7.079182781,5.77540554,4.552245437,4.130756829,3.480313534]

# plt.plot(x1, y1, color='k', linestyle='dashdot',  marker='o', markerfacecolor='0.8', label = "low traffic")
# plt.plot(x1, y2, color='blue', marker='^', linestyle='--', markerfacecolor='0.8', label = "morderate traffic")
# plt.plot(x1, y3, color='red', marker='x', linestyle='-', markerfacecolor='0.8', label = "heavy traffic")
# # plt.xlim(109, 201)
# # plt.ylim(0, 1)
# plt.xlabel("blind distance (in meters)")
# #plt.ylabel("No of jobs dropped ")
# plt.ylabel("transfer rates (in Mbps)")
# right_side = ax.spines["right"]
# right_side.set_visible(False)
# top_side = ax.spines["top"]
# top_side.set_visible(False)

# plt.legend()
# plt.margins(0.02)
# # plt.savefig("D:\vehicle_graphs\response_time.pdf", dpi=300, bbox_inches = 'tight')
# plt.show()

######## plot for logical cores
# y1= [26,18,13,11,11,9,8,8]
# y2= [103,70,49,38,29,25,24,21]
# y3= [187,118,93,71,58,49,41,37]

# plt.plot(x1, y1, color='k', linestyle='dashdot',  marker='o', markerfacecolor='0.8', label = "low traffic")
# plt.plot(x1, y2, color='blue', marker='^', linestyle='--', markerfacecolor='0.8', label = "morderate traffic")
# plt.plot(x1, y3, color='red', marker='x', linestyle='-', markerfacecolor='0.8', label = "heavy traffic")
# # plt.xlim(109, 201)
# # plt.ylim(0, 1)
# plt.xlabel("blind distance (in meters)")
# #plt.ylabel("No of jobs dropped ")
# plt.ylabel("No of logical cores needed")
# right_side = ax.spines["right"]
# right_side.set_visible(False)
# top_side = ax.spines["top"]
# top_side.set_visible(False)

# plt.legend()
# plt.margins(0.02)
# # plt.savefig("D:\vehicle_graphs\response_time.pdf", dpi=300, bbox_inches = 'tight')
# plt.show()




