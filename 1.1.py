import numpy as np
a = [1,2,3,4,np.nan]
b = a[np.isnan(a)]
print(b)