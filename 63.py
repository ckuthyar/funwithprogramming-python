import numpy as np
info1=np.array([2,4,6,8])
info2=np.array([1,3,5,7])
print(np.vstack([info1,info2]))
print(np.hstack([info1,info2]))


info2=info1
print(info2)
