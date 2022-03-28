# 让加载的图片运动起来
import pygame
import sys

# 全局初始化
pygame.init()

# 设置窗口的分辨率、画布对象和标题
resolution = width, height = 1280, 720
windowSurface = pygame.display.set_mode(resolution)
pygame.display.set_caption("风景如画")

# 加载背景图，返回的表面可以用于绘制其它对象于其上
bgSurface = pygame.image.load("temp.jpg").convert()
frameRect = bgSurface.get_rect()
# 添加时钟
clock = pygame.time.Clock()

# 开始循环
while True:

    for event in pygame.event.get():
        # 处理退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 将背景图像bgSurface绘制于窗口表面windowSurface
    windowSurface.blit(bgSurface, (0, 0), frameRect)
    # 每次绘制的x坐标都要+1
    frameRect.x += 1
    # 绘制结束，刷新界面
    pygame.display.flip()
    # 时钟停留一帧的时长
    clock.tick(60)
