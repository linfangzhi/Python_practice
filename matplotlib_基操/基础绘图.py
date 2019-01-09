from matplotlib import pyplot as plt
import math
import random

u = lambda x:x**2

x = range(20)
#y = [u(i)for i in range(1,10)]
y = [random.randint(10,20) for i in range(20)]

#plt.figure(figsize = (20,8),dpi = 80)

#plt.xticks(x)
#_xtickes_lable = [i/2 for i in range(2,20)]
#plt.xticks(_xtickes_lable)
plt.yticks(range(min(y),max(y)+1))

plt.plot(x,y)

#plt.savefig('')
plt.show()