class Animal:
    def eat(self):
        print('吃')
    def drink(self):
        print('喝')
    def run(self):
        print('跑')
    def sleep(self):
        print('睡')


class Dog(Animal):
    def bark(self):
        print('wang')
class Lashi:
    def lashi(self):
        print('lashi')



class shengou(Dog,Lashi):# 多继承
    def bark(self):# 方法重写
        print('666')
        super().bark()# 方法拓展
        Dog.bark(self)


gou = shengou()
gou.lashi()

print(shengou.__mro__)