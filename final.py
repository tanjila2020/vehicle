from datetime import time
import math
import numpy as np
from collections import namedtuple
from functools import reduce
from random import shuffle
import random
from IPython import embed
from numpy.lib.function_base import piecewise
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pyrsistent import v
from  csv_read import times, avg_no_of_vehicles, avg_speeds
from scheduler import scheduling

####declaring and initializing arrays
#for test:
#blind_d = [x for x in range(2, 5, 2)]
blind_d = [x for x in range(2, 17, 2)]
deadlines = np.zeros((len(blind_d), len(times)))
perc_deadline_miss = np.zeros((len(blind_d), len(times)))
