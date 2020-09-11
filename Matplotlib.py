from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

#x=[2,4,6,8]
#y=[7,3,8,3]

#x2=[1,3,5,7]
#y2=[1,3,9,3]

#plt.scatter(x,y,'g',linewidth=3, label='Line 1')
#plt.plot(x2,y2,'c',linewidth=5, label='Line 2')

#plt.scatter(x,y,color='g')
#plt.plot(x2,y2, color='k')

#plt.bar(x,y,color='g',align='center')
#plt.bar(x2,y2, color='r',align='center')

x,y=np.loadtxt('mlibexample.csv',
               unpack=True,
               delimiter=',')
print(x)
print(y)

plt.bar(x,y)

plt.title('Sample Chart')
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
#plt.legend()


plt.show()
