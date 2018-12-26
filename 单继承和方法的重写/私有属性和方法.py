class Women:
    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret(self):
        #私有方法和私有属性 在对象的方法内部是可以访问的
        print("%s %s"%(self.name, self.__age))

xiaofang = Women('消防')

print(xiaofang._Women__age)
#伪私有方法 在外界还是可以调用私有方法和私有属性


