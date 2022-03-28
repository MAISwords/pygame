# 监听鼠标事件，获取鼠标坐标

import pygame
import sys

pygame.init()
# 创建窗口以进行显示;screen定义了一个游戏的屏幕，后续游戏场景中的游戏对象，都要在这个screen上绘制
screen = pygame.display.set_mode((1280, 720))
# 设置当前游戏窗口的标题
pygame.display.set_caption("打印鼠标坐标！")
# 最开始背景颜色是白色
screen.fill((255, 255, 255))


while True:
    for event in pygame.event.get():
        # 处理退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 获得鼠标位置
    x, y = pygame.mouse.get_pos()
    # 打印鼠标位置到控制台
    print("鼠标坐标：%d %d " % (x, y))
    # 将光标画上去
    # screen.blit(img, (x, y))
    # 刷新画面
    pygame.display.update()
