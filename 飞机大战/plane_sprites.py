import pygame

class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_name,speed=1):
    #调用父类的初始化方法
        super().__init__()
        #改写定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        pass

    def update(self, *args):
        # 在屏幕上的移动方向

        self.rect.y += self.speed