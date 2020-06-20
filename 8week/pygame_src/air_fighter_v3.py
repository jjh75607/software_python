# fighter_v3.py

import random

import pygame

# 게임 화면의 너비와 높이
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Player 클래스. pygame.sprite.Sprite의 서브 클래스
class Player(pygame.sprite.Sprite):
    # 생성자
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('res/plane_62_40.png').convert()
        self.image.set_colorkey((255, 255, 255))  # 투명색으로 WHITE 지정
        self.rect = self.image.get_rect()
        self.rect.move_ip(20, int(SCREEN_HEIGHT / 2))  # 좌측 중간쯤에 위치

    # 방향 키 입력에 따라 Player sprite의 움직임을 제어하기 위한 함수
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
            move_up_down_sound.play()
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
            move_up_down_sound.play()
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


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('res/bullet.png').convert()
        self.image.set_colorkey((255, 255, 255))  # 투명색으로 WHITE 지정
        self.rect = self.image.get_rect()
        self.rect.move_ip(player.rect.left, player.rect.top)

    def update(self):
        self.rect.move_ip(5, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


# Enemy 클래스. pygame.sprite.Sprite의 서브 클래스
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('res/missile_28_10.png').convert()
        self.image.set_colorkey((255, 255, 255))  # WHITE를 투명색으로 지정

        # enemy의 중심을 화면의 오른쪽 밖 20 ~ 100 사이에 임의로 위치 시킴
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT))
        )
        # enemy의 속도를 난수로 지정
        self.speed = random.randint(3, 10)

    # speed에 따라 enemy 스프라이트를 이동시킴
    # 스크린의 왼쪽 끝을 넘으면 enemy 스프라이트 제거
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        if self.rect.top < player.rect.top:
            self.rect.move_ip(0, self.speed / 3)
        elif self.rect.top > player.rect.top:
            self.rect.move_ip(0, -self.speed / 3)


# Cloud 클래스. pygame.sprite.Sprite의 한 종류
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('res/cloud_62_32.png').convert()
        self.image.set_colorkey((0, 0, 0))  # BLACK을 투명색으로 지정

        # cloud의 중심을 화면의 오른쪽 밖 31 ~ 100 사이에 임의로 위치 시킴
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 31, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # 일정 속도로 Cloud 스프라이트 이동시킴
    # 게임 화면의 왼쪽 끝을 넘으면 cloud 스프라이트 제거
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


# pygame 모듈을 초기화함
pygame.init()

# 배경음과 음향 효과를 위한 mixer 초기화
pygame.mixer.init()

# 배겸 음악을 적재하고 플레이 함
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load('res/Apoxode_-_Electric_1.mp3')
pygame.mixer.music.play(loops=-1)  # 무한 반복 플레이

# 효과음들을 적재함
# https://freesound.org/ 에서 가져온 효과음 파일들 사용
move_up_down_sound = pygame.mixer.Sound('res/fm5.wav')
collision_sound = pygame.mixer.Sound('res/explosion10.wav')

# framerate를 제어하기 위한 clock 객체 생성
clock = pygame.time.Clock()

# screen 객체 생성. 너비: SCREEN_WIDTH, 높이: SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 새 enemy를 추가하기 위한 사용자 정의 이벤트 ADDENEMY를 정의하고
# 250 밀리초마다 ADDENEMY 이벤트를 발생시키는 타이머 설정
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# 새 cloud를 추가하기 위한 사용자 정의 이벤트 ADDCLOUD를 정의하고
# 1초마다 ADDCLOUD 이벤트를 발생시키는 타이머 설정
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# player 생성.
player = Player()

# enemy 들의 sprite group인 enemies와 모든 sprite들의 그룹인 all_sprites 생성
# - enemies: 충돌 탐지와 위치 업데이트에 사용
# - clouds: 위치 업데이트에 사용
# - all_sprites: rendering에 사용
enemies = pygame.sprite.Group()  # 모든 enemy들이 담길 스프라이트 그룹
clouds = pygame.sprite.Group()  # 모든 cloud들이 담길 스프라이트 그룹
bullets = pygame.sprite.Group()  # 총알 그
all_sprites = pygame.sprite.Group()  # player를 포함한 모든 스프라이트들의 그룹

all_sprites.add(player)

# player의 생명이 0이 되면 게임 종료
player_lives = 3

# 게임 루프
while (player_lives > 0):
    for event in pygame.event.get():
        # KEYDOWN 이벤트가 발생하였으면
        if event.type == pygame.KEYDOWN:
            # ESC 키가 눌려진 것이면 게임 루프를 빠져나감
            if event.key == pygame.K_ESCAPE:
                player_lives = 0

            if event.key == pygame.K_SPACE:
                newBullet = Bullet()
                bullets.add(newBullet)
                all_sprites.add(newBullet)

        # QUIT 이벤트가 발생하였으면 게임 루프를 빠져나감
        elif event.type == pygame.QUIT:
            player_lives = 0

        # ADDENEMY 이벤트가 발생하였으면
        elif event.type == ADDENEMY:
            # 새 enemy를 만들어 스프라이트 그룹 enemies와 all_sprites에 추가
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # ADDCLOUD 이벤트가 발생하였으면
        elif event.type == ADDCLOUD:
            # 새 Cloud 객체를 만들어 스프라이트 그룹 clouds와 all_aprites에 추가
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # 현재 눌려진 키들을 알아냄
    pressed_keys = pygame.key.get_pressed()

    # 사용자의 키 입력에 따라 player sprite를 움직인다.
    player.update(pressed_keys)

    # enemies와 clouds의 위치 업데이트
    enemies.update()
    clouds.update()
    bullets.update()

    # screen을 하늘 색으로 칠함
    screen.fill((135, 206, 253))

    # player를 포함하는 모든 sprite들을 rendering 한다.
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    for b in bullets:
        pygame.sprite.spritecollide(b, enemies, True)

    # player가 enemies 그룹의 enemy와의 충돌하면
    if pygame.sprite.spritecollideany(player, enemies):
        # player의 생명 감소
        player_lives = player_lives - 1
        pygame.sprite.spritecollideany(player, enemies).kill()

        # 충돌음을 1초동안 내고
        collision_sound.play()
        pygame.time.delay(1000)

    pygame.display.flip()  # 화면을 실제로 업데이트

    # 초당 30 프레임으로 속도 제어. 숫자를 늘리면 키 반응 빨라짐 
    clock.tick(30)

# player_lives가 0이 되어 게임 루프 빠져나왔음 
# game을 종료하기 전 마무리 작업을 수행해야 함

# 배경음악을 중단하고
pygame.mixer.music.stop()

# 효과음들을 중단하고
move_up_down_sound.stop()
collision_sound.stop()

# 믹서를 종료하고
pygame.mixer.quit()

# 모든 스프라이트들을 소멸시키고
all_sprites.empty()

# pygame을 종료
pygame.quit()
