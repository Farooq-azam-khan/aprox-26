 import numpy as np 
 
 def f26(n=10_000):
    arr = np.arange(n, dtype=np.float32)
    return np.sum(np.power(arr, 3) / np.power(2, arr))
