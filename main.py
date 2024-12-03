import pygame
from pygame.locals import *
import random

class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("persojaune.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30
        self.angle = 0

    def destroy(self):
        """Überprüft, ob Pacman außerhalb des Spielfelds ist."""
        if (
            self.rect.top > HAUTEUR
            or self.rect.bottom < 0
            or self.rect.left > LARGEUR
            or self.rect.right < 0
        ):
            self.kill()
            return True
        return False


pygame.init()
LARGEUR = 800
HAUTEUR = 550
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()

# Hintergrund
fond = pygame.sprite.Sprite()
fond.image = pygame.image.load("snakebackground.png").convert_alpha()
fond.rect = fond.image.get_rect()
fond.rect.x = 0
fond.rect.y = 0

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
liste_des_sprites.add(pacman)

# Gameover-Text
police = pygame.font.Font(None, 36)
texte = pygame.sprite.Sprite()
texte.image = police.render("Gameover", 1, (10, 10, 10), (255, 90, 20))
texte.rect = texte.image.get_rect()
texte.rect.centerx = fenetre.get_rect().centerx
texte.rect.centery = fenetre.get_rect().centery

pause = False
running = True
direction = "droite"

while running:
    fenetre.fill((0, 0, 0))
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
                
            if event.key == K_r and pause:
              pause = False
              direction = "droite"
              liste_des_sprites.remove(texte)
              pacman = Pacman()
              liste_des_sprites.add(pacman)

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

           

   
        # Überprüfe, ob Pacman zerstört werden muss
        if pacman.destroy():
            pause = True
            liste_des_sprites.add(texte)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
