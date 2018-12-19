class Dog(object):
    def __init__(self,name):
        self.name = name

    def game(self):
        print('%s 普通玩'% self.name)

class XiaoTianDog(Dog):

    def game(self):
        print('%s 飞到天上'%self.name)

class Person:
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog):
        print('%s 和 %s play togeder '%(self.name,dog.name))

        dog.game()

# 创建一个狗对象
#waicai =  Dog('wangcai')
waicai = XiaoTianDog('飞天旺财 ')
# 创建一个人对象

xiaoming = Person('xiaoming ')

xiaoming.game_with_dog(waicai)

# 让小名和狗 玩耍


