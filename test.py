import pandas as pd
import sys

# load the data, which consists of a single column 'x'
df = pd.read_csv('x.csv')

# add lots of empty float columns
for i in range(200):
    df[i] = 0.0

filename = sys.argv[1]

# write the dataframe to with 'x' as a data_column

# if we sort the series before writing, the bug goes away
# df.sort_values('x', inplace=True)

df.to_hdf(filename, 'df', format='t', data_columns=['x'])

# our query
where = 'x == 2012'

# query the hdf file directly
print(pd.read_hdf(filename, 'df', where=where).shape)
# (27237, 201)

# load the hdf file and then query
print(pd.read_hdf(filename,'df').query(where).shape)
# (27371, 201)
