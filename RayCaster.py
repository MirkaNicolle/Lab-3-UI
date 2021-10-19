'''
sources: https://github.com/attreyabhatt/Space-Invaders-Pygame
         https://github.com/churly92/RayCaster/blob/main/RayCaster.py

Mirka Monzon 18139
Lab 3: UI

'''

import pygame 

#inicializar pygame
pygame.init()

#pantalla
screen = pygame.display.set_mode((565, 540))

#fondo
fondo = pygame.image.load('espacio.jpg')

#encabezado
pygame.display.set_caption("Shooter Infinite")
icon = pygame.image.load('ship.png')
pygame.display.set_icon(icon)

#titulo
font = pygame.font.Font('freesansbold.ttf', 30)
textX = 170
textY = 35

def show_title(x,y):
    title = font.render("Shooter Infinite", True, (255,255,255))
    screen.blit(title, (x,y))

#loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(pygame.Color("black"), (0,0,30,30) )
    screen.blit(fondo, (0,0))
    show_title(textX,textY)

    pygame.display.flip()