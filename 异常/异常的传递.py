def demol1():
 return int(input('输入整数：'))

def demol2():
    return demol1()
# 利用异常的传递性，再主程序捕获异常

try:
    print(demol1())
except Exception as result:
    print(result)

