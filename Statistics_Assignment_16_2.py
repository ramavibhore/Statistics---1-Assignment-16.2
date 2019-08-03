'''
Find the variance for the following set of data representing trees in California (heights in
feet):
3, 21, 98, 203, 17, 9
'''
## Defition . Variance is squared deviation of a random variable from its mean value. It measures how far the data are spread out from its average value.  

import numpy as np

data=[3, 21, 98, 203, 17, 9]
sigma=np.var(data)
print('Variance from the given dataset is: ',sigma)
               