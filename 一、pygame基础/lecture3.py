# 窗口大小变换

import pygame
pygame.init()
SCREEN_SIZE = (1280, 720)
# 设置窗口大小为1280*720 并且窗口可以拉伸
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
pygame.display.set_caption("窗口大小变化！")

while True:
    # 背景颜色填充为绿色
    screen.fill((0, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # 如果窗口大小发生了变化
        if event.type == pygame.VIDEORESIZE:
            # 返回当前窗口大小--元组(宽,高)
            SCREEN_SIZE = event.size
            # 打印当前窗口大小到控制台
            print(event.size)
            # 把新的窗口大小数据给screen对象
            screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    # 更新屏幕
    pygame.display.update()
