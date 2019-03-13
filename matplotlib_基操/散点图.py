from matplotlib import pyplot as plt
import math
import random
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r'C:\\WINDOWS\\Fonts\\simsun.ttc')

a = [random.randint(50,100) for i in range(100)]

b = [i for i in range(100)]

plt.scatter(b,a,label='图例')
plt.xticks(b[::5],['{}牛逼'.format(i)for i in b],fontproperties=my_font,rotation = 45)

plt.xlabel('x坐标名称',fontproperties=my_font)
plt.ylabel('y坐标名称',fontproperties=my_font)
plt.ylabel('标题',fontproperties=my_font)

plt.legend(prop = my_font)

plt.show()