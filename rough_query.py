
import pandas as pd
from IPython import embed
import math
import numpy as np

import numpy as np
import math

b= [2, 4, 5]
t = [1,2,3,4,5]
bb = len(b)
tt= len(t)


c_ap = np.random.randint(1, 5, size=(bb, tt))

c_ser= np.random.randint(1, 5, size=(bb, tt))


print(c_ap)

c_ap_avg =[]
c_ap_avg = np.round(c_ap.mean(axis=1))
# for i in range(0,2):
#   print (c_ap_avg[i])

# df = pd.DataFrame(c_ap_avg, columns=['No_of_Ap'], index=['blind_d_array index'])
df1 = pd.DataFrame(c_ap_avg)
df2= pd.DataFrame(c_ser)
print(df2)
df1.to_csv('file_name.csv')
df2.to_csv('file_name.csv')
