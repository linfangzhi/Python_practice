import random
import math
from matplotlib import pyplot as plt


a = [random.randint(0,100) for i in range(10000)]


avr = [a[:i:] for i in range(1,10000)]

avr_list = [sum(i)/len(i) for i in avr]
plt.yticks(range(100)[::2])

plt.plot(range(1,10000),avr_list) #折线图

plt.show()