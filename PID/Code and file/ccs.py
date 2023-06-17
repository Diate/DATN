import matplotlib.pyplot as plt
import numpy as np

X = []
Y1 = [] 
Y2 = [] 
filename = 'KP150_TI20_KD2_TD1'
file = open(filename+'.txt','r')
  
for row in file:
    row = row.split(',')
    X.append(row[0])
    Y1.append(int(row[1]))
    Y2.append(int(row[2]))
  
plt.plot(X, Y1, color = 'r', label = 'Setpoint')
plt.plot(X, Y2, color = 'b', label = 'RealData')
  
plt.xlabel('Time', fontsize = 12)
plt.ylabel('Speed', fontsize = 12)
x = filename.split("_")
print(x)
name = ''
for i in x:
    name = name + " "+i
print(name)
plt.title(name, fontsize = 14)
plt.legend()
plt.show()