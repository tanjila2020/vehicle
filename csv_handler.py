import pandas
import math

df = pandas.read_csv('vehicle dataset.csv',
                     index_col='#')
time_array = df['time'].unique()

for time in time_array:
    matched_loc = df.loc[df['time'] == time]   #select the rows with the timestamp of sec
    print('Time:', time, 'Matched rows:', len(matched_loc))
    x1 = matched_loc['x']
    y1 = matched_loc['y']
    x2 = df.loc[df['time'] == time,'centroid_x'] = sum(matched_loc['x']) / len(matched_loc)
    y2 = df.loc[df['time'] == time,'centroid_y'] = sum(matched_loc['y']) / len(matched_loc)
    
    df.loc[df['time'] == time,'distance'] = ((x2 - x1)**2 + (y2 - y1)**2).pow(1./2)
    #math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )   
    # math.hypot(x2 - x1, y2 - y1)

    # print(df[0:5])

df.to_csv('output.csv')
