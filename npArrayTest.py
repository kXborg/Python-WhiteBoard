
import numpy as np
a = np.array([3])

b = np.array([6])

c = np.array([5])
max_no = np.maximum(a.copy(),b.copy(),c.copy())
print('>>>', id(max_no))
print(max_no)
print('________________________________________')
min_no = np.minimum(a.copy(), b.copy(), c.copy())
print('>>>', id(min_no))
print(min_no)
print('________________________________________')
print('>>>', id(max_no))
print(max_no)
print('>>>', id(min_no))
print(min_no)