import pandas
df = pandas.read_csv('vehicle dataset.csv',
                    index_col='#',)
# print(df[0:5])

time_array = df['time'].unique()

for time in time_array:
    matched_loc = df.loc[df['time'] == time]
    # print(matched_loc['name'])
    # print(matched_loc['x'][0:5])
    print(sum(matched_loc['x']), len(matched_loc))

    df.loc[df['time'] == time,'centroid_x'] = sum(matched_loc['x']) / len(matched_loc)
    df.loc[df['time'] == time,'centroid_y'] = sum(matched_loc['y']) / len(matched_loc)
    
    print(df[0:5])
    # matched_loc['centroid_x'] = matched_loc['x'] / len(matched_loc)
    # matched_loc['centroid_y'] = matched_loc['y'] / len(matched_loc)


    exit()

print(df['time'].unique())
print(len())

# df[0:5].to_csv('output.csv')
