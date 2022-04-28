
# create data
import numpy as np

x_data = list(range(5000))
#print(x_data)

y_data=5000*[0]
for i in range(5000):
	y_data[i] = 3*i + 5 + np.random.rand()*10
#print(y_data)


f = open('data.txt','a') # open txt, not exist->create,'a':stream
with open('data.txt','ab') as f:
	np.savetxt(f, np.vstack((x_data,y_data)).T, fmt="%.2f", delimiter='  ')

