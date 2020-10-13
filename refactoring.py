import pygame
from pygame.draw import *

# draw house
def house(canvas, x, y, size: {(0, 1)}):
    rect(
        canvas, 
        (0, 0, 0), 
        (x + 125*size, y + 47*size, 17*size, 27*size)
    )
    rect(
        canvas, 
        (128, 128, 0), 
        (x + 25*size, y + 100*size, 175*size, 250*size)
    )
    polygon(
        canvas, 
        (0, 0, 0), 
        (
            (x + 12*size, y + 100*size),
                                (x + 212*size, y + 100*size),
                                (x + 187*size, y + 37*size),
                                (x + 37*size, y + 75*size)
        )
    )
    rect(
        canvas, 
        (128, 128, 128), 
        (x + 12*size, y + 187*size, 200*size, 25*size)
    )
    rect(
        canvas, 
        (128, 0, 0), 
        (x + 37*size, y + 112*size, 150*size, 62*size)
    )
    rect(
        canvas, 
        (128, 0, 0), 
        (x + 37*size, y + 237*size, 40*size, 62*size)
    )
    rect(
        canvas, 
        (255, 255, 0), 
        (x + 137*size, y + 237*size, 40*size, 62*size)
    )
    rect(
        canvas, 
        (128, 0, 0), 
        (x + 87*size, y + 237*size, 40*size, 62*size)
    )
    rect(
        canvas, 
        (0, 0, 0), 
        (x + 75*size, y + 42*size, 10*size, 40*size)
    )
    rect(
        canvas, 
        (128, 128, 128), 
        (x + 15*size, y + 155*size, 195*size, 5*size)
    )
    for i in range(5):
        rect(
            canvas, 
            (128, 128, 128), 
            (x + 30*size + 36*size * i, y + 160*size, 20*size, 40*size)
        )
    return

# draw ghost
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

# draw sky
def sky(screen, x, y):
    rect(screen, (90, 90, 90), (x, y, x + 720, y + 540))
    rect(screen, (0, 0, 0), (x, y, x + 720, y))

# draw clouds
def clouds(screen, x, y, lenth, height):
    ellipse(screen, (100, 100, 100), (2*x + 50, y + 75, 5*lenth, 4*height))
    ellipse(screen, (128, 128, 128), (x, 3*y - 20, 6*lenth, 3*height))
    ellipse(screen, (60, 60, 60), (x, y, 6*lenth, 4*height))

# draw transpanent ghost
def surface(x, y, angle):
    surf = pygame.Surface((200, 200))
    surf.set_colorkey((0, 0, 0))
    surf.set_alpha(angle)
    ghost(surf, 0, 0, 1)
    screen.blit(surf, (x, y))

# draw transpapent cloud
def transp_cloud(x, y, angle):
    surf_6 = pygame.Surface((x, y))
    surf_6.set_colorkey((0, 0, 0))
    surf_6.set_alpha(angle)
    ellipse(surf_6, (105, 105, 105), (0, 0, x, y - 50))
    screen.blit(surf_6, (2*y, x - 50))

# draw fog
def fog(x, y, angle):
    surf_5 = pygame.Surface((y - 100, 3 * x))
    surf_5.set_colorkey((0, 0, 0))
    surf_5.set_alpha(angle)
    screen.blit(surf_5, (x, y))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((720, 1080))


sky(screen, 0, 0)
clouds(screen, 100, 100, 100, 25)

# moon
circle(screen, (255, 255, 255), (600, 90), 70)

# one more cloud
ellipse(screen, (140, 140, 140), (500, 100, 600, 75))

fog(50, 700, 200)

house(screen, 500, 200, 1)
house(screen, 200, 320, 1)
house(screen, 30, 380, 1)

transp_cloud(600, 150, 200)

surface(500, 600, 100)
surface(450, 650, 200)
surface(500, 600, 100)

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
