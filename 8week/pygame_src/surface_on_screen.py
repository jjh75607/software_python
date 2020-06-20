# surface_on_screen.py
import pygame

pygame.init() # pygame 초기화

# 폭 500, 높이 500의 게임 화면을 표현하는 Surface 객체 screen을 생성
screen = pygame.display.set_mode((500, 500))

# 폭 100, 높이 100인 Surface 객체 surf1을 만들고, 
# surf1을 파랑으로 칠하고, surf1위에 반경이 30인 노랑 원을 그림
surf1 = pygame.Surface((100, 100))
surf1.fill((0, 0, 255)) # 파랑
pygame.draw.circle(surf1, (255, 255, 0), (50, 50), 30) # 노랑

# 게임 화면 객체 screen 위에 surf1을 그림
screen.blit(surf1, (50, 50))

# 게임 화면의 내용을 디스플레이에 실제로 그림
pygame.display.flip()

pygame.quit()
