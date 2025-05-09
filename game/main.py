import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((800, 600))

# 主循环
running = true
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false

    # 更新屏幕
    pygame.display.flip()

# 退出pygame
pygame.quit()
sys.exit()