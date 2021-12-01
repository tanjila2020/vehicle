import pandas as pd
from IPython import embed

time_slots = [10800, 18000, 21600]
offset = 0
no_of_rows = 1000000
time = 0

while time < 23000:
    df = pd.read_csv("koln-pruned.tr",
                    skiprows=offset, nrows=no_of_rows, header=None, delimiter=' ',
                    names=['time', "name", 'x', 'y', 'speed'],
                    dtype={"time": "int64", "name": "string", "x": "float64", "y": "float64"})
    offset += no_of_rows

    start_time = int(df['time'].head(1))
    end_time = int(df['time'].tail(1))

    print(int(start_time), int(end_time))

    filtered_times = [time for time in time_slots if start_time <= time and time <= end_time]
    print(filtered_times)

    for ft in filtered_times:
        temp_df = df.query(f'time>{ft} and time<{ft+900} and x<14500 and x>12500 and y<14000 and y>12000')
        temp_df.to_csv(f'{ft} - {len(temp_df)}.csv')
    
    
    time = end_time
    

# embed()