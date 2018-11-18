import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

fig = plt.figure()
#anomaly
red=[1,0,0]
blue = 	[0 ,1 ,0]
black= [0,0,0]
magneta=[1,0,1]
sz= 25



x2 = [4.7,4.1,4.8,4.4,4,4.5,4.2,4.3, 5.5,4.3,4.28]
y2 = [5.7,5.5,4.2,3,4,4.5,4.6,2.1,4.3, 4.2, 4.56]
scatter2 = plt.scatter(x2,y2,25, blue)

x1=[-1,  10]
y1 = [3, 6]
scatter2 = plt.scatter(x1,y1,100, black, marker="*")
plt.xlabel('параметр 1', fontsize=14, color='black')
plt.ylabel('параметр 2', fontsize=14, color='black')

a=2
b=2
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
x, y = np.meshgrid(x, y)
plt.contour(x+4, y+4,(x*x/(a*a) + y*y/(b*b)), [1], colors='r')


grid1 = plt.grid(True)   # линии вспомогательной сетки

plt.savefig("4.png")
plt.show()
