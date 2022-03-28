# 测试pygame安装
import pygame
pygame.init()
myrect = pygame.Rect(300, 500, 200, 256)
print("myrect坐标原点：%d %d 大小：%d %d" % (myrect.x, myrect.y,myrect.width, myrect.height))
