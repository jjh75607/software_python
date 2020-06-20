# blue_circle.py program
import pygame # pygame 임포트

pygame.init() # pygame 초기화

# 가로 세로 500 pixel의 screen 생성
screen = pygame.display.set_mode([500, 500])

radius = 100.0 # 원의 반경
running = True # loop flag

# 사용자가 종료 버튼을 누르면 while 루프 빠져나감
while running:
    # 사용자가 Window Quit 버튼을 누르면 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경 색을 white 즉 RGB (255, 255, 255)로 칠함
    screen.fill((255, 255, 255))

    # 좌표 (250, 250)에 반경이 radius인 청색 (0, 0, 255) 원을 그림.
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), int(radius))
        
    # 실제로 디스플레이에 화면을 그림
    pygame.display.flip()

# pygame을 종료함
pygame.quit()
