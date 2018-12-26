import pygame
import time

pygame.init()

screen = pygame.display.set_mode((480,700),)
# 绘制背景图像
# 加载图像数据
bg = pygame.image.load("")
# 绘制图像
screen.blit(bg,(0,0))
# 更新图像
pygame.display.update()

# 绘制英雄的飞机
hero = pygame.image.load('')
screen.blit(hero,(200,500))
pygame.display.update()

clock = pygame.time.Clock()


hero_rect = pygame.Rect(150,300,102,126)
while True:
    #每秒60次运行
    clock.tick(60)
    # 捕获事件
    # evet_list = pygame.event.get()
    # if evet_list:
    #     print(evet_list)


    #监听事件
    for event in pygame.event.get():
        #判断事件类型是否为推出事件
        if event.type == pygame.QUIT:
            print('游戏推出')
            pygame.quit()
            exit()


    hero_rect.y -= 1
    # 判断飞机的位置
    if hero_rect.y<=0:
        hero_rect.y =  700

    screen.blit(hero,hero_rect)
    pygame.display.update()

    pass
pygame.quit()
