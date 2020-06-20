# move_surf1.py program
import pygame

pygame.init() # pygame 초기화

# 폭 500 높이 500의 screen 생성
screen = pygame.display.set_mode([500, 500])

# 폭 100 높이 100인 Surface 객체 surf1 생성
surf1 = pygame.Surface((100, 100))
surf1.fill((0, 0, 255)) # blue로 칠함
surf1_pos = [250-50, 250-50] # surf1의 초기 위치는 screen 중앙

running = True

# 사용자가 게임 창을 닫는 버튼을 클릭하거나 ESC 키를 누를 때까지 반복 
while (running):
    # event queue에서 event를 꺼내어 처리
    for event in pygame.event.get():
        # 사용자가 게임 창을 닫는 버튼을 클릭
        if event.type == pygame.QUIT:
            running = False

        # 사용자가 키보드를 누름    
        elif event.type == pygame.KEYDOWN:
            # 현재 눌려진 키들이 무엇인가 알아냄
            pressed_keys = pygame.key.get_pressed()    
            print(surf1_pos)

            # 눌린 방향키 방향으로 surf1을 5 픽셀만큼 움직임
            if pressed_keys[pygame.K_UP]: # 위 방향키
                surf1_pos[1] = surf1_pos[1] - 5
            elif pressed_keys[pygame.K_DOWN]: # 아래 방향키
                surf1_pos[1] = surf1_pos[1] + 5
            elif pressed_keys[pygame.K_LEFT]: # 좌 방향키
                surf1_pos[0] = surf1_pos[0] - 5
            elif pressed_keys[pygame.K_RIGHT]: # 우 방향키
                surf1_pos[0] = surf1_pos[0] + 5
            elif pressed_keys[pygame.K_ESCAPE]: # ESC 키
                running = False
        
    # screen을 흰색으로 칠함
    screen.fill((255, 255, 255)) # rgb white

    # screen에 surf1을 그림
    screen.blit(surf1, surf1_pos)
    
    # 이때 screen의 내용이 모니터에 실제로 그려짐.
    pygame.display.flip()

# 게임 루프 종료되어 게임을 종료함
pygame.quit()
