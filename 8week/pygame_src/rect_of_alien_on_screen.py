# rect_of_alien_on_screen.py
import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])

alien1 = pygame.image.load('C:/Program Files/Python38' +
     '/Lib/site-packages/pygame/examples/data/alien1.jpg')

rect1 = alien1.get_rect() # alien1을 덮는 Rect 객체 반환
rect1.move_ip(200, 200) # rect1의 좌측 상단의 좌표를 200, 200으로 이동
print(rect1) # <rect(200, 200, 80, 71)>

screen.blit(alien1, rect1.topleft)
pygame.display.flip()
