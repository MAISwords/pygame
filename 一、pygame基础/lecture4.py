# 显示图像操作

import pygame
import sys
# 全局初始化
pygame.init()
# 设置窗口的分辨率
resolution = width, height = 1280, 720
# 拿到画布
windowSurface = pygame.display.set_mode(resolution)
# 设置标题
pygame.display.set_caption("风景如画")
# 加载背景图，返回的表面可以用于绘制其它对象于其上
# bgSurface = pygame.image.load("temp.jpg").convert()
# 使图片适应给定的分辨率
bgSurface = pygame.transform.scale(pygame.image.load("temp.jpg"), (1280, 720)).convert()
# 准备工作就绪，开始进行循环体处理
while True:
    for event in pygame.event.get():
        # 处理退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 将背景图像bgSurface绘制于画布windowSurface上，从画布的坐标0,0开始绘制
    windowSurface.blit(bgSurface, (0, 0))
    # 绘制数据准备完毕，刷新屏幕
    pygame.display.update()
