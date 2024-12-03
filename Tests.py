import pygame
from pygame.locals import *
from random import randint

pygame.init()
LARGEUR = 600
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()

fond = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(fond)
fond.image = pygame.image.load("snakebackground.png").convert_alpha()
fond.rect = fond.image.get_rect()

fond.rect.x = 0
fond.rect.y = 0
# Stockage du sprite dans une liste de sprites
liste_des_sprites = pygame.sprite.LayeredUpdates()
liste_des_sprites.add(fond)




perso = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(perso)
perso.image = pygame.image.load("persojaune.png").convert()
perso.rect = perso.image.get_rect()
perso.rect.x = 300
perso.rect.y = 300

liste_des_sprites.add(perso)
liste_des_sprites.add(fond)


continuer = True


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
            if event.key == K_LEFT:
                direction = "gauche"
            if event.key == K_UP:
                direction == "haut"

    if direction == "droite":
        perso.rect.x += 3
    elif direction == "bas":
        perso.rect.y += 3
    elif direction == "gauche":
        perso.rect.x += -3
    elif direction == "haut":
        perso.rect.y += -3

    pygame.display.flip()
    fenetre.fill((0, 0, 0))
    clock.tick(60)

pygame.quit()