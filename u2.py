

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import math
offset = 100000000
inc = 6000000


# file_name = "koln-pruned.tr"

# determining the time period
tb = pd.read_csv("/Users/tayebehbahreini/Desktop/IC2E/zoom.csv", nrows=inc/6)

Table_8 = pd.read_csv("/Users/tayebehbahreini/Desktop/IC2E/koln-pruned.tr",
                      skiprows=offset, nrows=inc/2, header=None, delimiter=' ',
                      names=['time', "name", 'x', 'y', 'speed'],
                      dtype={"time": "int64", "name": "string", "x": "float64", "y": "float64"})

min(Table_8['time'])

avg = 0
tb = Table_8.query('x<14500 and x>12500 and y<14000 and y>12000 ')

t = 0
avg = 0
for t in range(28874, 29104):
    tb1 = tb.query('time==@t')
    tb2 = tb.query('time==@t+180')
    a = set(tb1['name'])
    b = set(tb2['name'])
    c = a-b
    avg = avg+(len(c)/len(a))*100

avg/230
tb = pd.read_csv("/Users/tayebehbahreini/Desktop/IC2E/zoom.csv")
# tb["comb"].value_counts().nlargest(n=2).values[1]
# Calling a method of Counter object(count)
tb1 = tb.query('comb==45 and time==28886')
tb1.count()
Z = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
Z[14][0] = 1/26
Z[17][1] = 1/26
Z[16][2] = 3/26
Z[16][3] = 2/26
Z[16][3] = 2/26
Z[15][2] = 6/26
Z[15][3] = 4/26
Z[14][2] = 1/26
Z[14][3] = 1/26
Z[15][4] = 3/26
Z[15][5] = 1/26
Z[14][1] = 2/26

plt.pcolormesh(Z)
plt.colorbar(label='Probability')
plt.axis('off')
plt.show()


# Table_8=pd.read_csv("/Users/tayebehbahreini/Desktop/IC2E/koln-pruned.tr",skiprows=offset,nrows=inc,header=None, delimiter=' ' ,names=["time","name","x","y","speed"],dtype={"time":"float64","name":"string","x":"float64","y":"float64"})
# Table_8.to_csv( "/Users/tayebehbahreini/Desktop/IC2E/TB.csv")


Table_8 = pd.read_csv(
    "/Users/tayebehbahreini/Desktop/IC2E/TB.csv", nrows=inc/6)

Table_8.count()

x = np.array(Table_8['x'])[:120000]
y = np.array(Table_8['y'])[:120000]

grid_size = 250
h = 100

# GETTING X,Y MIN AND MAX
x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)

# CONSTRUCT GRID
x_grid = np.arange(x_min-h, x_max+h, grid_size)
y_grid = np.arange(y_min-h, y_max+h, grid_size)
x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)

# GRID CENTER POINT
xc = x_mesh+(grid_size/2)
yc = y_mesh+(grid_size/2)

# FUNCTION TO CALCULATE INTENSITY WITH QUARTIC KERNEL


def kde_quartic(d, h):
    dn = d/h
    P = (15/16)*(1-dn**2)**2
    return P


# PROCESSING
intensity_list = []
for j in range(len(xc)):
    intensity_row = []
    for k in range(len(xc[0])):
        kde_value_list = []
        for i in range(len(x)):
            # CALCULATE DISTANCE
            d = math.sqrt((xc[j][k]-x[i])**2+(yc[j][k]-y[i])**2)
            if d <= h:
                p = kde_quartic(d, h)
            else:
                p = 0
            kde_value_list.append(p)
        # SUM ALL INTENSITY VALUE
        p_total = sum(kde_value_list)
        intensity_row.append(p_total)
    intensity_list.append(intensity_row)

# HEATMAP OUTPUT
intensity = np.array(intensity_list)
plt.pcolormesh(x_mesh, y_mesh, intensity/len(x))

plt.colorbar(label='Probability')
plt.axis('off')
plt.show()


# plt.hist2d(Table_8['x'],Table_8['y'], bins=500,cmap="OrRd")
# plt.axis('off')
# plt.show()


#Table_8=pd.read_csv("/Users/tayebehbahreini/Desktop/IC2E/TB.csv" ,nrows=inc/6)


tb = Table_8.query('x<14500 and x>12500 and y<14000 and y>12000')
#tb.to_csv( "/Users/tayebehbahreini/Desktop/IC2E/zoom.csv")
# tb.count()
#tb=pd.read_csv("/Users/tayebehbahreini/Desktop/IC2E/zoom.csv" )


# plt.hist2d(tb['x'],tb['y'], bins=(100,100),cmap="OrRd")
# plt.axis('off')
# plt.show()
# sns.heatmap(tb['x'],tb['y'], cmap="OrRd")
# D1=2000
# D2=2000

# for i in range(D1):
#          for j in range(D2):
#              arr[i][j]=tb['x']

# np.savetxt('output.csv',arr,delimiter=",")

len(tb)
x = np.array(tb['x'])[:68491]
y = np.array(tb['y'])[:68491]

grid_size = 110
h = 60

# GETTING X,Y MIN AND MAX
x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)

# CONSTRUCT GRID
x_grid = np.arange(x_min-h, x_max+h, grid_size)
y_grid = np.arange(y_min-h, y_max+h, grid_size)
x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)

# GRID CENTER POINT
xc = x_mesh+(grid_size/2)
yc = y_mesh+(grid_size/2)


# FUNCTION TO CALCULATE INTENSITY WITH QUARTIC KERNEL
def kde_quartic(d, h):
    dn = d/h
    P = (15/16)*(1-dn**2)**2
    return P


# PROCESSING
intensity_list = []
for j in range(len(xc)):
    intensity_row = []
    for k in range(len(xc[0])):
        kde_value_list = []
        for i in range(len(x)):
            # CALCULATE DISTANCE
            d = math.sqrt((xc[j][k]-x[i])**2+(yc[j][k]-y[i])**2)
            if d <= h:
                p = kde_quartic(d, h)
            else:
                p = 0
            kde_value_list.append(p)
        # SUM ALL INTENSITY VALUE
        p_total = sum(kde_value_list)
        intensity_row.append(p_total)
    intensity_list.append(intensity_row)

# HEATMAP OUTPUT
intensity = np.array(intensity_list)
plt.pcolormesh(x_mesh, y_mesh, intensity/len(x))
plt.colorbar(label='Probability')
plt.axis('off')
plt.show()
len(intensity)
