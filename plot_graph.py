from datetime import time
import math
import numpy as np
import random
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pyrsistent import v


df1= pd.read_csv('server_utilization_avg.csv')
print(df1)

df2 = pd.read_csv('server_utilization_peak.csv')
print(df2)