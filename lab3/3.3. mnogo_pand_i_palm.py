import pygame
from pygame.draw import *
from pygame import gfxdraw


def leaf(height, width, x, y, angle):
    Fon_color = (255, 177, 129)
    surf = pygame.Surface((int(3 * width), height))
    surf.fill(Fon_color)
    ellipse(surf, (0, 104, 52), (0, 0, width, height))
    surf.set_colorkey(Fon_color)
    surface2 = pygame.transform.rotate(surf, angle)
    surface2.set_alpha(255)
    screen.blit(surface2, (x, y))


def bamboo(screen, height, width, x, y):
    leaf(int(0.20 * height), int(0.5 * width), x - int(4 * width), y
         - int(0.5 * height), 170)
    leaf(int(0.20 * height), int(0.5 * width), x - int(5 * width), y
         - int(0.53 * height), 170)
    leaf(int(0.20 * height), int(0.5 * width), x - int(6 * width), y
         - int(0.5 * height), 170)
    leaf(int(0.20 * height), int(0.5 * width), x - int(3 * width), y
         - int(0.70 * height), 170)
    leaf(int(0.20 * height), int(0.5 * width), x - int(4 * width), y
         - int(0.75 * height), 170)
    leaf(int(0.20 * height), int(0.5 * width), x - int(5 * width), y
         - int(0.78 * height), 170)
    leaf(int(0.20 * height), int(0.5 * width), x - int(6 * width), y
         - int(0.79 * height), 170)
    leaf(int(0.20 * height), int(0.5 * width), x - int(7 * width), y
         - int(0.81 * height), 170)
    leaf(int(0.20 * height), int(0.5 * width), x + int(3 * width), y
         - int(0.88 * height), 10)
    leaf(int(0.20 * height), int(0.5 * width), x + int(4 * width), y
         - int(0.93 * height), 10)
    leaf(int(0.20 * height), int(0.5 * width), x + int(5 * width), y
         - int(0.95 * height), 10)
    leaf(int(0.20 * height), int(0.5 * width), x + int(6 * width), y
         - int(0.95 * height), 10)
    leaf(int(0.20 * height), int(0.5 * width), x + int(7 * width), y
         - int(0.96 * height), 30)
    leaf(int(0.20 * height), int(0.5 * width), x + int(1 * width), y
         - int(0.55 * height), 10)
    leaf(int(0.20 * height), int(0.5 * width), x + int(2 * width), y
         - int(0.65 * height), 10)
    leaf(int(0.20 * height), int(0.5 * width), x + int(3 * width), y
         - int(0.68 * height), 17)
    line(screen, (0, 104, 52), (x, y), (x, y - int(0.23 * height)),
         width)
    line(screen, (0, 104, 52), (x, y - int(0.25 * height)), (x, y
         - int(0.5 * height)), width)
    line(screen, (0, 104, 52), (x - int(0.25 * width), y - int(0.52
         * height)), (x + int(0.25 * width), y - int(0.73 * height)),
         int(0.8 * width))
    line(screen, (0, 104, 52), (x, y - int(0.75 * height)), (x + width,
         y - height), int(0.4 * width))
    arc(
        screen,
        (0, 104, 52),
        (x - 6 * width, y - int(0.52 * height), int(5.5 * width),
         int(0.52 * height)),
        0.25,
        2,
        int(0.20 * width),
        )
    arc(
        screen,
        (0, 104, 52),
        (x - 13 * width, y - int(0.8 * height), int(15 * width),
         int(1.30 * height)),
        0.84,
        1.63,
        int(0.20 * width),
        )
    arc(
        screen,
        (0, 104, 52),
        (x + int(0.5 * width), y - int(0.67 * height), int(5.5
         * width), int(0.52 * height)),
        1.2,
        2.9,
        int(0.20 * width),
        )
    arc(
        screen,
        (0, 104, 52),
        (x - width, y - int(0.95 * height), int(15 * width), int(1.30
         * height)),
        1.45,
        2.45,
        int(0.20 * width),
        )


def panda(screen, width, height, x, y):
    ellipse(screen, (0, 0, 0), (x + int(0.6 * width), y + int(0.70
            * height), int(0.20 * width), int(0.4 * height)))
    circle(screen, (0, 0, 0), (x + int(0.9 * width), y + int(0.30
           * height)), int(0.20 * height))
    ellipse(screen, (255, 255, 255), (x, y, width, height))
    ellipse(screen, (255, 255, 255), (x, y + int(0.43 * height),
            int(0.9 * width), int(0.70 * height)))
    polygon(screen, (0, 0, 0), [(x + int(0.30 * width), y + int(1)), (x
            + int(0.5 * width), y + int(1)), (x + int(0.5 * width), y
            + int(1 * height)), (x + int(0.30 * width), y + int(1
            * height))])
    polygon(screen, (0, 0, 0), [(x + int(0.25 * width), y + int(1.5
            * height)), (x + int(0.55 * width), y + int(1.4 * height)),
            (x + int(0.5 * width), y + int(1 * height)), (x + int(0.30
            * width), y + int(1 * height))])
    polygon(screen, (0, 0, 0), [(x + int(0 * width), y + int(0
            * height)), (x + int(0.1 * width), y + int(0 * height)), (x
            + int(0.20 * width), y + int(1.2 * height)), (x + int(0
            * width), y + int(1.5 * height)), (x - int(0.05 * width), y
            + int(1.2 * height))])
    ellipse(screen, (0, 0, 0), (x + int(0.20 * width), y + int(1.25
            * height), int(0.30 * width), int(0.30 * height)))
    ellipse(screen, (0, 0, 0), (x + int(0.25 * width), y + int(1.25
            * height), int(0.30 * width), int(0.30 * height)))
    ellipse(screen, (0, 0, 0), (x + int(0.28 * width), y + int(1.30
            * height), int(0.25 * width), int(0.30 * height)))
    ellipse(screen, (0, 0, 0), (x + int(0.23 * width), y + int(1.30
            * height), int(0.30 * width), int(0.20 * height)))
    ellipse(screen, (0, 0, 0), (x + int(0.20 * width), y + int(1.30
            * height), int(0.30 * width), int(0.30 * height)))
    circle(screen, (0, 0, 0), (x, y), int(0.20 * height))
    circle(screen, (255, 255, 255), (x + int(0.20 * width), y
           + int(0.30 * height)), int(0.55 * height))
    circle(screen, (0, 0, 0), (x + int(0.30 * width), y), int(0.20
           * height))
    ellipse(screen, (0, 0, 0), (x - int(0.08 * width), y + int(0.20
            * height), int(0.1 * width), int(0.30 * height)))
    circle(screen, (0, 0, 0), (x + int(0.15 * width), y + int(0.4
           * height)), int(0.14 * height))
    circle(screen, (0, 0, 0), (x + int(0.04 * width), y + int(0.6
           * height)), int(0.07 * height))
    ellipse(screen, (0, 0, 0), (x + int(0.85 * width), y + int(0.45
            * height), int(0.20 * width), int(0.9 * height)))
    ellipse(screen, (0, 0, 0), (x + int(0.8 * width), y + int(0.95
            * height), int(0.20 * width), int(0.4 * height)))


pygame.init()

FPS = 30
x = 981
y = 654
screen = pygame.display.set_mode((x, y))

rect(screen, (255, 177, 129), (0, 0, x, y))
bamboo(screen, 360, 20, 800, 368)
bamboo(screen, 360, 30, 408, 368)
bamboo(screen, 290, 15, 277, 374)
bamboo(screen, 290, 15, 177, 400)
panda(screen, 250, 125, 500, 300)
panda(screen, 100, 50, 300, 500)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    pygame.display.update()
