print([[i,j]for i in range(10)  for j in range(5)])

a = (i for i in range(10)) #生成器 迭代器
b = [i for i in range(10)] # 列表


c = lambda x,y : x+y
print(c(1,4))