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


class Fantome(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("fantome1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

x_aleatoire = randint(20,40)
y_aleatoire = randint(20,40)

fantome1 = Fantome(x_aleatoire,y_aleatoire)


class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("persojaune.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30
        self.angle = 0
        self.perso = 0


    def tourne_vers_haut(self):
        angle_de_rotation = 90 - self.angle
        self.image = pygame.transform.rotate(self.image, angle_de_rotation)
        self.angle = 90

    def tourne_vers_gauche(self):
        angle_de_rotation = 180 - self.angle
        self.image = pygame.transform.rotate(self.image, angle_de_rotation)
        self.angle = 180

    def tourne_vers_bas(self):
        angle_de_rotation = 270 - self.angle
        self.image = pygame.transform.rotate(self.image, angle_de_rotation)
        self.angle = 270

    def tourne_vers_droit(self):
        angle_de_rotation = 0 - self.angle
        self.image = pygame.transform.rotate(self.image, angle_de_rotation)
        self.angle = 0


perso = Pacman()


liste_des_sprites.add(perso)
liste_des_sprites.add(fantome1)
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
                direction = "haut"


    if direction == "droite":
        perso.rect.x += 3
        perso.tourne_vers_droit()

    elif direction == "bas":
        perso.rect.y += 3
        perso.tourne_vers_bas()
    elif direction == "gauche":
        perso.rect.x += -3
        perso.tourne_vers_gauche()
    elif direction == "haut":
        perso.rect.y += -3
        perso.tourne_vers_haut()

    pygame.display.flip()
    fenetre.fill((0, 0, 0))
    clock.tick(60)




pygame.quit()




