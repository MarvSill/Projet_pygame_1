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
        self.perso = 0

    def destroy(self):
        if (
                self.rect.top > HAUTEUR
                or self.rect.bottom < 0
                or self.rect.left > LARGEUR
                or self.rect.right < 0
        ):
            self.kill()
            return True
        return False

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

pygame.init()
LARGEUR = 800
HAUTEUR = 550
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()

fond = pygame.sprite.Sprite()
fond.image = pygame.image.load("snakebackground.png").convert_alpha()
fond.rect = fond.image.get_rect()
fond.rect.x = 0
fond.rect.y = 0

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("wall.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Fantome(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("fantome1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vitesse_x = 3
        self.vitesse_y = 0
        self.temps_du_dernier_changement = pygame.time.get_ticks()

    def bouger_aleatoirement(self):
        self.rect.x += self.vitesse_x
        self.rect.y += self.vitesse_y
        if self.rect.y > HAUTEUR:
            self.rect.y -= 549
        elif self.rect.x > LARGEUR:
            self.rect.x -= 799
        elif self.rect.y + 550 < HAUTEUR:
            self.rect.y += 549
        elif self.rect.x + 800 < LARGEUR:
            self.rect.x += 799


        self.changement_direction()

    def changement_direction(self):
        temps_actuel = pygame.time.get_ticks()
        if self.temps_du_dernier_changement + 500 <= temps_actuel:
            nombre_aleatoire = random.randint(1,4)
            if nombre_aleatoire == 1:
                self.vitesse_x = 3
                self.vitesse_y = 0
            elif nombre_aleatoire == 2:
                self.vitesse_x = -3
                self.vitesse_y = 0
            elif nombre_aleatoire == 3:
                self.vitesse_x = 0
                self.vitesse_y = 3
            elif nombre_aleatoire == 4:
                self.vitesse_x = 0
                self.vitesse_y = -3
            self.temps_du_dernier_changement = temps_actuel





            #Changement de direction



x_aleatoire1 = random.randint(20, 400)
y_aleatoire1 = random.randint(20, 400)
x_aleatoire2 = random.randint(20, 400)
y_aleatoire2 = random.randint(20, 400)


fantome1 = Fantome(x_aleatoire1, y_aleatoire1)
fantome2 = Fantome(x_aleatoire2, y_aleatoire2)

wall1 = Wall(x_aleatoire1, y_aleatoire1)


x_aleatoire = random.randint(200, 400)
y_aleatoire = random.randint(200, 400)

fantomes = []
walls = []

fantomes.append(fantome1)
fantomes.append(fantome2)


walls.append((wall1))


perso = Pacman()

liste_des_sprites = pygame.sprite.Group()
liste_des_sprites.add(fond)
liste_des_sprites.add(perso)
liste_des_sprites.add(fantome1)
liste_des_sprites.add(fantome2)
liste_des_sprites.add(wall1)

#liste_des_sprites est tout ce qui est afficher sur l'écran


score = 0

police = pygame.font.Font(None, 50)
texte = pygame.sprite.Sprite()
texte2 = pygame.sprite.Sprite()
texte.image = police.render("Gameover", 1, (0, 10, 10), (255, 90, 20))
texte2.image = police.render("Score : " + str(score),1, (10, 10, 10), (0, 128, 128))
texte.rect = texte.image.get_rect()
texte.rect.centerx = fenetre.get_rect().centerx
texte.rect.centery = fenetre.get_rect().centery
texte2.rect = texte.image.get_rect()
texte2.rect.centerx = fenetre.get_rect().centerx
texte2.rect.centery = 330


pause = False
running = True
direction = "droite"


while running:
    fenetre.fill((0, 0, 0))
    liste_des_sprites.draw(fenetre)

    for fantome in fantomes:
        fantome.bouger_aleatoirement()

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
                liste_des_sprites.remove(texte2)
                perso = Pacman()
                liste_des_sprites.add(perso)
                liste_des_sprites.add(fantome)
                liste_des_sprites.add(fantome1)
                liste_des_sprites.add(wall)

    if pause == False:

        if direction == "droite":
            perso.rect.x += 3
            perso.tourne_vers_droit()

        elif direction == "bas":
            perso.rect.y += 3
            perso.tourne_vers_bas()

        elif direction == "gauche":
            perso.rect.x -= 3
            perso.tourne_vers_gauche()

        elif direction == "haut":
            perso.rect.y -= 3
            perso.tourne_vers_haut()

        if perso.destroy():
            pause = True
            liste_des_sprites.add(texte)
            #le texte est afficher
            liste_des_sprites.add(texte2)
            for fantome in fantomes:
                fantome.kill()
            for wall in walls:
                wall.kill()

        for fantome in fantomes:
            if fantome.rect.colliderect(perso):
                liste_des_sprites.remove(fantome)
                fantomes.remove(fantome)
                fantome.kill()
                score += 1
                texte2.image = police.render("Score : " + str(score), 1, (10, 10, 10), (0, 128, 128))
                x_aleatoire_fantome = random.randint(20, LARGEUR - 40)
                y_aleatoire_fantome = random.randint(20, HAUTEUR - 40)
                nouveau_fantome = Fantome(x_aleatoire_fantome, y_aleatoire_fantome)
                x_aleatoire_wall = random.randint(20, LARGEUR - 40)
                y_aleatoire_wall = random.randint(20, HAUTEUR - 40)
                nouveau_wall = Wall(x_aleatoire_wall, y_aleatoire_wall)
                fantomes.append(nouveau_fantome)
                walls.append(nouveau_wall)
                liste_des_sprites.add(nouveau_fantome)
                liste_des_sprites.add(nouveau_wall)


        for wall in walls:
            if wall.rect.colliderect(perso):
                liste_des_sprites.remove(perso)
                perso.kill()
                pause = True
                liste_des_sprites.add(texte)
                # le texte est afficher
                liste_des_sprites.add(texte2)
                for fantome in fantomes:
                    fantome.kill()
                for wall in walls:
                    wall.kill()



    pygame.display.flip()
    clock.tick(60)

pygame.quit()