# alien_on_screen.py
import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])

alien1 = pygame.image.load('C:/Program Files/Python38' +
     '/Lib/site-packages/pygame/examples/data/alien1.jpg')
print(alien1) # <Surface(80x71x24 SW)>

screen.blit(alien1, (50, 50))
pygame.display.flip()
