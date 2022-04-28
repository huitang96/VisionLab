'''
2: design network  
'''

# ----------------------------read------------------------------
import numpy as np
import matplotlib.pyplot as plt
from torch.autograd import Variable

x_data_r = [[0.]]*5000
#print(x_data_r)
y_data_r = [[0.]]*5000
j = 0

f = open('data.txt',"r") # only read
contents = f.readlines() # read all line

# convert x
for i in contents:
#	print(i.split('  ')[0])
	x_data_r[j] = [float(i.split('  ')[0])] # list to float
	j = j + 1
#print(x_data_r)

#convert y
j=0 
for i in contents:
	y_data_r[j] = [float(i.split('  ')[1])] # list to float
	j = j + 1
#print(y_data_r)

#plt.plot(x_data_r, y_data_r)
#plt.show()

# ----------------------------network---------------------------

import torch
#x_data_r -> list
x_data = torch.Tensor(x_data_r)
#print(x_data) # [100,1]
y_data = torch.Tensor(y_data_r)
print(y_data)
'''
x_data = torch.unsqueeze(torch.linspace(-1, 1, 10), dim=1)
print(x_data)
y_data = 2 * x_data   + 1 + torch.rand(x_data.size())
'''


class LinearModel(torch.nn.Module):
	def __init__(self):
		super(LinearModel, self).__init__()
		self.linear = torch.nn.Linear(1,1)

	def forward(self, x):
		y_pred = self.linear(x)
		return y_pred



model =  LinearModel()
#print(model)

criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-7)

num_epochs =1000
for epoch in range(num_epochs):
#	inputs = Variable(x_data)
#	target = Variable(y_data)
#forward
	y_pred = model(x_data)
	loss = criterion(y_pred, y_data)
	print(epoch, loss)

#backward
	optimizer.zero_grad()   #梯度归零
	loss.backward()
	optimizer.step()  #根据梯度和预先设置的学习率自动更新
	#if (epoch + 1) % 200 == 0:
	#	print('loss:'loss.data)
		#print('Epoch[{}/{}], loss:{:.6f}'.format(epoch + 1, 
		#	num_epochs, loss.data[0]))


#输出权重和偏置
print('w = ', model.linear.weight.item())
#weight是一个矩阵，需要显示数值用item()
print('b = ', model.linear.bias.item())

#测试
x_test =torch.Tensor([[4.0]])   #(1, 1)矩阵
y_test = model(x_test)
print('y_pred = ', y_test.data) #(1, 1)矩阵
