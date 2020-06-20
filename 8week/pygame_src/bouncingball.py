# bouncingball.py
import sys
import pygame

pygame.init()
pygame.display.set_caption("Bouncing Ball")

#size = width, height = 320, 240
WIDTH = 640
HEIGHT = 480
BLACK = (0, 0, 0)

speed = [4, 4]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball = pygame.image.load("res/intro_ball.gif")

# 배경음과 음향 효과를 위한 mixer 초기화
pygame.mixer.init()
collision_sound = pygame.mixer.Sound('res/ball3.wav')

ballrect = ball.get_rect()

running_flag = True

while (running_flag == True):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running_flag = False
            
    ballrect = ballrect.move(speed)
    if (ballrect.left < 0) or (ballrect.right > WIDTH):
        speed[0] = -speed[0]
        collision_sound.play()
        
    if (ballrect.top < 0) or (ballrect.bottom > HEIGHT):
        speed[1] = -speed[1]
        collision_sound.play()

    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    clock.tick(30) # 초당 40프레임
    
# running_flag == False
pygame.mixer.quit()
pygame.quit()
sys.exit()



