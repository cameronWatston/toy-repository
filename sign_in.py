import numpy as np

import pandas as pd

signed_in = [
  "ting",
  "sizhe",
  "Cameron",
  "hellooooemi",
  "lc",
  "abdullah",
  "blabalabalablabkla"
]






import numpy as np

def linear_regression(X, y):

    n = len(X)
    

    mean_x = np.mean(X)
    mean_y = np.mean(y)
    
   
    b1 = np.sum((X - mean_x) * (y - mean_y)) / np.sum((X - mean_x) ** 2)
    
   
    b0 = mean_y - b1 * mean_x
    
    return b0, b1


X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

b0, b1 = linear_regression(X, y)
print(f"Intercept (b0): {b0}")
print(f"Slope (b1): {b1}")
