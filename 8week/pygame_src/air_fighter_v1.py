# air_fighter_v1.py

import pygame
import random

# 게임 화면의 너비와 높이
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Player 클래스. pygame.sprite.Sprite의 서브 클래스
class Player(pygame.sprite.Sprite):
    # 생성자
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('res/plane_62_40.png').convert()
        self.image.set_colorkey((255, 255, 255)) # 투명색으로 WHITE 지정
        self.rect = self.image.get_rect()
        self.rect.move_ip(20, int(SCREEN_HEIGHT/2)) # 좌측 중간쯤에 위치

    # 방향키 입력에 따라 Player sprite의 움직임을 제어하기 위한 함수
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # player가 화면을 벗어나지 못하게 제어
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT    

# pygame 모듈을 초기화함
pygame.init()

# screen 객체 생성. 너비: SCREEN_WIDTH, 높이: SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# player 스프라이트 생성.
player = Player()

# player의 생명이 0이 되면 게임 종료
player_lives = 1

# 게임 루프
while (player_lives > 0):
    for event in pygame.event.get():
        # KEYDOWN 이벤트가 발생하였으면
        if event.type == pygame.KEYDOWN:
            # ESC 키가 눌려진 것이면 게임 루프를 빠져나감
            if event.key == pygame.K_ESCAPE:
                player_lives = player_lives - 1
                
        # QUIT 이벤트가 발생하였으면 게임 루프를 빠져나감
        elif event.type == pygame.QUIT:            
            player_lives = player_lives - 1

    # screen을 하늘색으로 칠함
    screen.fill((135, 206, 253))
    
    # player를 screen에 그림
    screen.blit(player.image, player.rect)
    
    # 현재 눌려진 키들을 알아냄
    pressed_keys = pygame.key.get_pressed()

    # 사용자의 키 입력에 따라 player sprite를 움직인다.
    player.update(pressed_keys)

    # 게임 화면이 실제로 그려짐
    pygame.display.flip()

# 게임 루프가 종료하여 게임을 종료함
pygame.quit() 
