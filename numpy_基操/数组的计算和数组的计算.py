import numpy as np

t1 = np.arange(12)

print(t1) # 输出数组
print(t1.shape) # 数组的维度
print(t1.ndim) # 数组的秩
print(t1.size) # 数组的元素总数
print(t1.dtype) # 数组中的元素类型
print(t1.itemsize) # 数组中的妹子元素的字节大小
print(t1.data) # 包含实际数组元素的缓冲区

# 创建数组

ar1 = np.array(range(10))
ar2 = np.arange(10)
ar3 = np.array([1,2,3,4,5,6,])
ar4 = np.array([[1,2,3,4,5,6,],[15,7,8,9,9]])

print(ar1)
print(ar2)
print(ar3)
print(ar4)
print(np.random.rand(10).reshape(2,5))

#

print(np.linspace(10,20,num=20))#10开始到20结束，等间距拆开20个

print(np.linspace(10,20,num=21,endpoint=True)) #开闭区间
print(np.linspace(10,20,num= 20,retstep=True)) #显示间距

print(np.zeros((3,7),dtype=np.int))

ar5 = np.array([list(range(10)),list(range(10,20))])

print(np.zeros_like(ar5)) #生成一个和ar5一样的0矩阵
print(np.ones_like(ar5)) # 生成一个和ar5一样的单位矩阵


print(np.eye(5)) # 对角单位矩阵

