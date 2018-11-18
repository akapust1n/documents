import matplotlib.pyplot as plt

fig = plt.figure()
#anomaly
red=[1,0,0]
blue = 	[0 ,1 ,0]
black= [0,0,0]
magneta=[1,0,1]
sz= 25

scatter1 = plt.scatter([0.0, 1.0],[8.0,8.0],100, red, marker=">")


x = [4.7,5.1,5.8,4.4,4,5,4.2,4.3]
y = [4.2,4.5,4.2,4.4,4,5,5.6,4.7]
scatter2 = plt.scatter(x,y,100, blue, marker="8")

x1=[4.7, 5.2, 4.9]
y1 = [7.2, 6.9, 7]
scatter3 = plt.scatter(x1,y1,100, black, marker="*")
plt.xlabel('параметр 1', fontsize=14, color='black')
plt.ylabel('параметр 2', fontsize=14, color='black')

x2= [3.2]
y2= [2.1]

scatter3 = plt.scatter(x2,y2,100, magneta, marker="s")




text1 = plt.text(0.5, 0.5, 'Text on figure')
print('Text: ', type(text1))

grid1 = plt.grid(True)   # линии вспомогательной сетки

plt.savefig("1.png")
plt.show()
