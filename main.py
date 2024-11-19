import pygame
from pygame.locals import *
from random import randint

pygame.init()
LARGEUR = 600
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()
continuer = True

perso = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(perso)
perso.image = pygame.image.load("perso.png").convert_alpha()
perso.rect = perso.image.get_rect()
perso.rect.x = 300
perso.rect.y = 300

liste_des_sprites = pygame.sprite.LayeredUpdates()
liste_des_sprites.add(perso)

direction = "droite"

while continuer:
    liste_des_sprites.draw(fenetre)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direction = "droite"
            if event.key == K_DOWN:
                direction = "bas"
            # A compléter...

    if direction == "droite":
        perso.rect.x += 3
    elif direction == "bas":
        perso.rect.y += 3
    # A compléter...

    pygame.display.flip()
    fenetre.fill((0, 0, 0))
    clock.tick(60)

pygame.quit()