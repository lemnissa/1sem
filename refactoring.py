import pygame
from pygame.draw import *


def house(canvas, x, y, size: {(0, 1)}):
    rect(
        canvas, 
        (0, 0, 0), 
        (x + 250*size, y + 95*size, 35*size, 55*size)
    )
    rect(
        canvas, 
        (128, 128, 0), 
        (x + 50*size, y + 200*size, 350*size, 500*size)
    )
    polygon(
        canvas, 
        (0, 0, 0), 
        (
            (x + 25*size, y + 200*size),
                                (x + 425*size, y + 200*size),
                                (x + 375*size, y + 150*size),
                                (x + 75*size, y + 150*size)
        )
    )
    rect(
        canvas, 
        (128, 128, 128), 
        (x + 25*size, y + 375*size, 400*size, 50*size)
    )
    rect(
        canvas, 
        (128, 0, 0), 
        (x + 75*size, y + 225*size, 300*size, 125*size)
    )
    rect(
        canvas, 
        (128, 0, 0), 
        (x + 75*size, y + 475*size, 80*size, 125*size)
    )
    rect(
        canvas, 
        (255, 255, 0), 
        (x + 275*size, y + 475*size, 80*size, 125*size)
    )
    rect(
        canvas, 
        (128, 0, 0), 
        (x + 175*size, y + 475*size, 80*size, 125*size)
    )
    rect(
        canvas, 
        (0, 0, 0), 
        (x + 150*size, y + 85*size, 20*size, 80*size)
    )
    rect(
        canvas, 
        (128, 128, 128), 
        (x + 30*size, y + 310*size, 390*size, 10*size)
    )
    for i in range(5):
        rect(
            canvas, 
            (128, 128, 128), 
            (x + 60*size + 72*size * i, y + 320*size, 40*size, 80*size)
        )
    return


def ghost(canvas, x, y, size: {(0, 1)}):
    circle(
        canvas, 
        (211, 211, 211), 
        (x + 75*size, y + 50*size), 
        30*size
    )
    circle(
        canvas, 
        (173, 216, 230), 
        (x + 63*size, y + 47*size), 
        7*size
    )
    circle(
        canvas, 
        (0, 0, 0), 
        (x + 63*size, y + 47*size), 
        2*size
    )
    circle(
        canvas, 
        (173, 216, 230), 
        (x + 82*size, y + 43*size), 
        7*size
    )
    circle(
        canvas, 
        (0, 0, 0), 
        (x + 82*size, y + 43*size), 
        2*size
    )
    polygon(
        canvas, 
        (211, 211, 211), 
        (
            (x + 75*size, y + 50*size), 
            (x + 50*size, y + 60*size),                          
            (x + 45*size, y + 90*size), 
            (x + 60*size, y + 130*size),
            (x + 40*size, y + 170*size), 
            (x + 80*size, y + 150*size),
            (x + 100*size, y + 165*size), 
            (x + 125*size, y + 145*size),
            (x + 140*size, y + 150*size), 
            (x + 160*size, y + 130*size),
            (x + 140*size, y + 100*size), 
            (x + 120*size, y + 80*size),
            (x + 105*size, y + 50*size)
        )
    )
    return


pygame.init()

FPS = 30
screen = pygame.display.set_mode((720, 1080))

# sky 
rect(screen, (90, 90, 90), (0, 0, 720, 540))
rect(screen, (0, 0, 0), (0, 540, 720, 540))

# clouds
ellipse(screen, (100, 100, 100), (250, 175, 500, 100))
ellipse(screen, (128, 128, 128), (100, 280, 600, 75))
ellipse(screen, (60, 60, 60), (100, 100, 600, 100))

# moon
circle(screen, (255, 255, 255), (600, 90), 70)

# one more cloud
ellipse(screen, (140, 140, 140), (500, 100, 600, 75))

# fog
surf_5 = pygame.Surface((600, 150))
surf_5.set_colorkey((0, 0, 0))
surf_5.set_alpha(200)
screen.blit(surf_5, (50, 700))

# houses
house(screen, 500, 200, 0.5)
house(screen, 200, 320, 0.4)
house(screen, 30, 380, 0.4)

# transparent cloud
surf_6 = pygame.Surface((600, 150))
surf_6.set_colorkey((0, 0, 0))
surf_6.set_alpha(200)
ellipse(surf_6, (105, 105, 105), (0, 0, 600, 100))
screen.blit(surf_6, (300, 550))

surf_1 = pygame.Surface((200, 200))
surf_1.set_colorkey((0, 0, 0))
surf_1.set_alpha(100)
ghost(surf_1, 0, 0, 1)
screen.blit(surf_1, (500, 600))

surf_2 = pygame.Surface((200, 200))
surf_2.set_colorkey((0, 0, 0))
surf_2.set_alpha(200)
ghost(surf_2, 0, 0, 1)
screen.blit(surf_2, (450, 650))

surf_3 = pygame.Surface((200, 200))
surf_3.set_colorkey((0, 0, 0))
surf_3.set_alpha(100)
ghost(surf_3, 0, 0, 1)
screen.blit(surf_3, (500, 600))

ghost(screen, 150, 610, 1)
ghost(screen, 80, 650, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
