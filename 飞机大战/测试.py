# 调用sys模块，负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境
import sys
# 调用pygame库
import pygame
# 调用pygame中的所有常量，便于使用（主要是懒）
from pygame.locals import *

white = 255, 255, 255
bule = 0, 0, 255
# 初始化pygame
pygame.init()
# 获取对显示系统的访问，并创建一个窗口，分别率位（600x500）screen:屏幕
screen = pygame.display.set_mode((600, 500))
# 创建字体对象，用于绘制文本(None,60)：none为默认字体，60是字体大小
myfont = pygame.font.Font(None, 60)
# 第一个参数是文本内容，第二个为抗锯齿字体，第三位颜色
textImage = myfont.render("Hello PyGame_PieGame",True,white)
# 等待退出（任意键退出）
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(bule)  # 清屏
    # 绘制一个圆
    color = 255, 255, 0
    position = 300, 250
    radius = 100
    width = 10
    # screen.blit(textImage,(100,100))#进行绘制
    pygame.draw.circle(screen, color, position, radius, width)
    pygame.display.update()  # 刷新显示


