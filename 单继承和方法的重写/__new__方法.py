class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 1.创建对象时候new方法会被自动调用
        print('创建对象，分配空间')
        # 2.为对象分配空间
        return super().__new__(cls)
        # 3.返回对象的引用


    def __init__(self):
        print('播放器初始化')


player = MusicPlayer()

print(player)