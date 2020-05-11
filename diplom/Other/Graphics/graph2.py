import matplotlib.pyplot as plt

fig = plt.figure()
#anomaly
red=[1,0,0]
blue = 	[0 ,1 ,0]
black= [0,0,0]
magneta=[1,0,1]
sz= 25



x = [4.7,4.1,4.8,4.4,4,4.5,4.2,4.3, 4.5]
y = [4.2,4.5,4.2,4.4,4,4.5,4.6,4.5,4.3]
scatter2 = plt.scatter(x,y,50, blue)

x1=[1]
y1 = [5]
scatter2 = plt.scatter(x1,y1,100, black, marker="*")
plt.xlabel('параметр 1', fontsize=14, color='black')
plt.ylabel('параметр 2', fontsize=14, color='black')


x2=[6, 5]
y2 = [6, 5.5]
scatter3 = plt.scatter(x2,y2,100, red, marker=">")

text1 = plt.text(0.5, 0.5, 'Text on figure')
print('Text: ', type(text1))

grid1 = plt.grid(True)   # линии вспомогательной сетки

plt.savefig("2.png")
plt.show()
