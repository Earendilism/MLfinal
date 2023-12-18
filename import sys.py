from datetime import datetime
from datetime import timedelta
import numpy as np


# dates in string format
str_d1 = '2023/08/31 , 19:30:00'
str_d2 = '2023/08/27 , 21:00:00'

# convert string to date object
d1 = datetime.strptime(str_d1, "%Y/%m/%d ,  %H:%M:%S")
d2 = datetime.strptime(str_d2, "%Y/%m/%d ,  %H:%M:%S")
# difference between dates in timedelta
delta = d1 - d2
dt_store = np.char.array(np.zeros((340200, 4)), unicode=True)
i = 0
while delta.days > 0 or delta.seconds//3600 > 0 or \
      delta.seconds % 3600//60 > 0 or delta.seconds % 3600 % 60 > 0:
    delta -= timedelta(days=0, seconds=1, microseconds=0,
                       milliseconds=0, minutes=0, hours=0, weeks=0)
    dt_store[i, 0] = str(delta.days)
    dt_store[i, 1] = str(delta.seconds//3600)
    dt_store[i, 2] = str(delta.seconds % 3600//60)
    dt_store[i, 3] = str(delta.seconds % 3600 % 60)
    i += 1
dt_store = np.char.zfill(dt_store, 2)
print(dt_store[0,3][1])
