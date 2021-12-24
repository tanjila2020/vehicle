



import numpy as np
import random
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#in average configuration no of Ap = 84, no of servers = 57, 
# this is choosen to get transfer time= 16 , Edge execution time was 14, local execution time= 200, edge speed factor= 15

#the peak configuration was  no of Ap = 177, no of servers = 121, 



plt.rcParams['font.size'] = '11'
plt.rcParams['lines.markersize'] = 5
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["legend.columnspacing"]=0.5
plt.rcParams["legend.handletextpad"]=0.2
plt.rcParams["legend.labelspacing"]=0.5
plt.rcParams["legend.borderpad"]=0.1
plt.rcParams["legend.borderaxespad"]=-0.2
plt.rcParams["legend.fontsize"]=11

fig, ax = plt.subplots()

#Time of the day (1AM to 11PM)
x1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

#Average Response time in millisecond
y1 = [15, 15, 15, 15, 21, 30, 43, 48, 34, 33, 41, 46, 31, 37, 35, 35, 36, 46, 33, 34, 19, 19,17 ] 

#percentage of jobs dropped while using the average configuration
y2 = [0, 0, 0, 0, 0, 0, 0.4, 0.49, 0.13, 0.13, 0.35, 0.44, 0.035, 0.24, 0.16, 0.21, 0.21, 0.45, 0.13, 0.13, 0, 0, 0]

#server utilization for average configuration
y3 = [0.07, 0.07, 0.07, 0.07, 0.35, 0.91, 1, 1, 0.98, 0.98, 1, 1, 0.95, 1, 1, 1, 1, 1, 0.98, 0.98, 0.28, 0.35, 0.21 ]

#server utilization for peak configuration
y4 = [0.016, 0.008, 0.012, 0.03, 0.17, 0.42, 0.84, 0.91, 0.56, 0.56, 0.77, 0.91, 0.49, 0.63, 0.56, 0.63, 0.63, 0.91, 0.56, 0.56, 0.14, 0.14, 0.09 ]

#no of vehicles:
y5 = [25, 3, 13, 45, 284, 704, 1349, 1570, 887, 870, 1241, 1476, 759, 1073, 960, 978, 988, 1479, 875, 892, 190, 231, 134]


#code to plot as bar graph
ax.bar(x1,y5)

#code to plot as line graph
#plt.plot(x1, y5, color='blue', linestyle='-',  marker='o', markerfacecolor='0')




plt.xlabel("Time of the day")
#plt.ylabel("No of jobs dropped ")
plt.ylabel("Number of vehicles")
















#plt.axhline(y = 14, color = 'r', linestyle = '-')
#plt.xlim(0, 2000)
#plt.ylim(0, 30)
# plt.yticks(np.arange(0, 1.1, 0.2))




right_side = ax.spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)

plt.legend()
plt.margins(0.02)

plt.legend(ncol=1, loc="upper left")
plt.savefig("C:/Users/hf1987/Desktop/EDF_docs/graphs/no_of_vehicles.pdf", dpi=300, bbox_inches = 'tight')
plt.show()





