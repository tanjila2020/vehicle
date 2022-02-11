import pandas as pd
from IPython import embed

#time_slots = [3600, 7200, 10800, 14400, 18000, 21600, 25200, 28800, 32400, 36000, 39600, 43200, 46800, 50400, 54000, 57600, 61200, 64800, 68400, 72000, 75600, 79200, 82800 ]
time_slots = [3635, 86400]
offset = 0
#no_of_rows =6000000
no_of_rows =1500000000
time = 0

while time < 90000:
    df = pd.read_csv("koln-pruned.tr",
                    skiprows=offset, nrows=no_of_rows, header=None, delimiter=' ',
                    names=['time', "name", 'x', 'y', 'speed'],
                    dtype={"time": "int64", "name": "string", "x": "float64", "y": "float64"})
    offset += no_of_rows

    start_time = int(df['time'].head(1))
    end_time = int(df['time'].tail(1))

    print(int(start_time), int(end_time))

    filtered_times = [time for time in time_slots if time >= start_time and time <= end_time]
    print(filtered_times)

    for ft in filtered_times:
        temp_df = df.query(f'time>={ft} and time<={ft+900} and x<14500 and x>12500 and y<14000 and y>12000')
        temp_df.to_csv(f'{ft} - {len(temp_df)}.csv')
    
    
    time = end_time
    

# embed()