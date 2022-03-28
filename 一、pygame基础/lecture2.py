# 通过点击鼠标切换背景颜色

import pygame
# 游戏初始化的设置，他应该在游戏代码编写的最前边
pygame.init()
# 创建窗口以进行显示;screen定义了一个游戏的屏幕，后续游戏场景中的游戏对象，都要在这个screen上绘制
screen = pygame.display.set_mode((1280, 720))
# 设置当前游戏窗口的标题
pygame.display.set_caption("点击鼠标切换背景颜色")
# 最开始背景颜色是白色
screen.fill((255, 255, 255))
# 颜色标记
color = False

# 准备工作已完成，开始进行游戏主体循环
while True:
    # pygame.event.get()  游戏中的事件
    # 如果事件类型是退出，则退出程序
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                color = not color
                if color:
                    # 切换为绿色
                    screen.fill((0, 255, 0))
                else:
                    screen.fill((255, 255, 255))
    # 根据上一次更新的绘制数据，进行窗口更新
    pygame.display.update()
