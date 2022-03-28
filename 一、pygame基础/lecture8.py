# 键盘监听操作
import pygame
import sys

pygame.init()
# 创建窗口以进行显示;screen定义了一个游戏的屏幕，后续游戏场景中的游戏对象，都要在这个screen上绘制
screen = pygame.display.set_mode((1280, 720))
# 设置当前游戏窗口的标题
pygame.display.set_caption("移动小球！")
# 最开始背景颜色是白色
screen.fill((255, 255, 255))

clock = pygame.time.Clock()

x, y = 640, 360
move_x = 0
move_y = 0

while True:
    for event in pygame.event.get():
        # 处理退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_x = -1
            if event.key == pygame.K_d:
                move_x = 1
            if event.key == pygame.K_w:
                move_y = -1
            if event.key == pygame.K_s:
                move_y = 1
        elif event.type == pygame.KEYUP:
            move_x = 0
            move_y = 0

    x += move_x
    y += move_y
    # 进行白色覆盖
    screen.fill((255, 255, 255))
    # 绘制小球
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20, 20)
    # 更新屏幕数据
    pygame.display.update()
    clock.tick(60)

