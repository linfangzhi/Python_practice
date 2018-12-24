title = '模块1'
def say_hello():
    print('hello')

class Dog(object):
    pass


print(__name__)

if __name__ == '__main__':
    # 常用 开头 下面的是用来做测试用的，可以保证程序被重复调用
    print('开发的函数')
    say_hello()