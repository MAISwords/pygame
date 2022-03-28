# 时钟测试
import pygame
clock = pygame.time.Clock()
i = 0
# 游戏循环
while True:
    # 设置屏幕刷新帧率
    clock.tick(60)
    print(i)
    i += 1