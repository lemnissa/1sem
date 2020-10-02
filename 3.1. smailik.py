import pygame
from pygame.draw import *


def eye(x, y, k):
    
    circle(screen, (255, 0, 0), (x, y), k*10)
    circle(screen, (0, 0, 0), (x, y), k*10, 1)
    
    circle(screen, (0, 0, 0), (x, y), k*5)
    circle(screen, (0, 0, 0), (x, y), k*5, 1)    
    

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((125, 125, 125))

circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (200, 175), 150, 1)

eye(140, 130, 4)
eye(260, 130, 3)

rect(screen, (0, 0, 0), (130, 240, 140, 30))

polygon(screen, (0, 0, 0), [(45, 70), (180, 105), (175, 110), (40, 75)])
polygon(screen, (0, 0, 0), [(45, 70), (180, 105), (175, 110), (40, 75)], 1)

polygon(screen, (0, 0, 0), [(360, 70), (370, 75), (250, 110), (240, 105)])
polygon(screen, (0, 0, 0), [(360, 70), (370, 75), (250, 110), (240, 105)], 1)
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()