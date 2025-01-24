import pygame
from pygame.locals import *
import random

# Classe représentant le personnage principal (Pacman)
class Pacman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Chargement de l'image et position initiale
        self.image = pygame.image.load("persojaune.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30
        self.angle = 0
        self.perso = 0

    # Détruit Pacman si celui-ci sort de l'écran
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

    # Rotation de l'image selon la direction (haut)
    def tourne_vers_haut(self):
        angle_de_rotation = 90 - self.angle
        self.image = pygame.transform.rotate(self.image, angle_de_rotation)
        self.angle = 90

    # Rotation de l'image (gauche)
    def tourne_vers_gauche(self):
        angle_de_rotation = 180 - self.angle
        self.image = pygame.transform.rotate(self.image, angle_de_rotation)
        self.angle = 180

    # Rotation de l'image (bas)
    def tourne_vers_bas(self):
        angle_de_rotation = 270 - self.angle
        self.image = pygame.transform.rotate(self.image, angle_de_rotation)
        self.angle = 270

    # Rotation de l'image (droite)
    def tourne_vers_droit(self):
        angle_de_rotation = 0 - self.angle
        self.image = pygame.transform.rotate(self.image, angle_de_rotation)
        self.angle = 0

# Initialisation de pygame
pygame.init()
LARGEUR = 800 # Largeur de la fenêtre
HAUTEUR = 550 # Hauteur de la fenêtre
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()

# Classe pour afficher l'écran de bienvenue
class Welcome(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Chargement et redimensionnement de l'image
        self.image = pygame.image.load("welcomescreen.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (800, 550))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

# Chargement des éléments initiaux
welcome_screen = Welcome()

# Fond de l'écran
fond = pygame.sprite.Sprite()
fond.image = pygame.image.load("snakebackground.png").convert_alpha()
fond.rect = fond.image.get_rect()
fond.rect.x = 0
fond.rect.y = 0

# Classe pour représenter les murs
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Chargement et redimensionnement de l'image du mur
        self.image = pygame.image.load("wall.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Classe pour représenter les fantômes
class Fantome(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Initialisation du fantôme avec une vitesse aléatoire
        self.image = pygame.image.load("fantome1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vitesse_x = 3
        self.vitesse_y = 0
        self.temps_du_dernier_changement = pygame.time.get_ticks()

    # Déplacement aléatoire du fantôme
    def bouger_aleatoirement(self):
        self.rect.x += self.vitesse_x
        self.rect.y += self.vitesse_y
        # Gestion des sorties d'écran
        if self.rect.y > HAUTEUR:
            self.rect.y -= 549
        elif self.rect.x > LARGEUR:
            self.rect.x -= 799
        elif self.rect.y + 550 < HAUTEUR:
            self.rect.y += 549
        elif self.rect.x + 800 < LARGEUR:
            self.rect.x += 799
        # Changement de direction après un certain temps
        self.changement_direction()

    # Méthode pour changer la direction du fantôme
    def changement_direction(self):
        temps_actuel = pygame.time.get_ticks()
        if self.temps_du_dernier_changement + 500 <= temps_actuel:
            nombre_aleatoire = random.randint(1,4)
            # Direction aléatoire (haut, bas, gauche, droite)
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

# Création aléatoire des fantômes et murs
x_aleatoire1 = random.randint(20, 400)
y_aleatoire1 = random.randint(20, 400)
x_aleatoire2 = random.randint(20, 400)
y_aleatoire2 = random.randint(20, 400)

fantome1 = Fantome(x_aleatoire1, y_aleatoire1)
fantome2 = Fantome(x_aleatoire2, y_aleatoire2)
fantome3 = Fantome(x_aleatoire2, y_aleatoire2)

x_aleatoire = random.randint(200, 400)
y_aleatoire = random.randint(200, 400)

fantomes = []
walls = []

fantomes.append(fantome1)
fantomes.append(fantome2)
fantomes.append(fantome3)

# Initialisation du personnage Pacman
perso = Pacman()

# Score du joueur
score = 0

# Affichage du texte (score, game over)
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

# Création d'un groupe contenant tous les sprites à afficher sur l'écrant
liste_des_sprites = pygame.sprite.Group()
liste_des_sprites.add(fond) # Ajout du fond d'écran
liste_des_sprites.add(perso) # Ajout du personnage principal (Pacman)
# Ajout fantômes
liste_des_sprites.add(fantome1)
liste_des_sprites.add(fantome2)
liste_des_sprites.add(fantome3)
liste_des_sprites.add(welcome_screen) # Ajout de l'écran d'accueil

# Initialisation des variables pour le contrôle du jeu
pause = False # Indique si le jeu est en pause
running = False # Indique si le jeu est en cours
start = True # Contrôle l'écran d'accueil
direction = "droite" # Direction initiale du personnage

# Boucle principale pour l'écran d'accueil
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fermer la fenêtre
            start = False
        if event.type == KEYDOWN:
            # Détection des touches directionnelles pour définir la direction
            if event.key == K_RIGHT:
                direction = "droite"

            if event.key == K_DOWN:
                direction = "bas"
            if event.key == K_LEFT:
                direction = "gauche"
            if event.key == K_UP:
                direction = "haut"

            # Démarrage du jeu avec la touche 'S'
            if event.key == K_s:
                pause = False
                direction = "droite"
                # Réinitialisation des éléments du jeu
                liste_des_sprites.remove(texte)
                liste_des_sprites.remove(texte2)
                perso = Pacman()
                liste_des_sprites.empty() # Vide tous les sprites
                liste_des_sprites.add(fond)
                liste_des_sprites.add(perso)
                liste_des_sprites.add(fantomes)
                walls = [] # Réinitialisation des murs
                score = 0  # Réinitialisation du score
                texte2.image = police.render("Score : " + str(score), 1, (10, 10, 10), (0, 128, 128))
                running = True # Le jeu commence

            # Redémarrage après une pause avec la touche 'R'
            if event.key == K_r and pause:
                pause = False
                direction = "droite"
                liste_des_sprites.remove(texte)
                liste_des_sprites.remove(texte2)
                perso = Pacman()
                liste_des_sprites.empty()
                liste_des_sprites.add(fond)
                liste_des_sprites.add(perso)
                liste_des_sprites.add(fantomes)
                walls = []
                score = 0
                texte2.image = police.render("Score : " + str(score), 1, (10, 10, 10), (0, 128, 128))


    if running:
        # Mouvement aléatoire des fantômes
        for fantome in fantomes:
            fantome.bouger_aleatoirement()

        # Gestion des déplacements du personnage en fonction de la direction
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

            # Gestion de la condition de défaite (Pacman détruit)
            if perso.destroy():
                pause = True
                liste_des_sprites.add(texte)
                #le texte est afficher
                liste_des_sprites.add(texte2)
                for fantome in fantomes:
                    fantome.kill()
                for wall in walls:
                    wall.kill()

            # Gestion des collisions avec les fantômes
            for fantome in fantomes:
                if fantome.rect.colliderect(perso):
                    liste_des_sprites.remove(fantome)
                    fantomes.remove(fantome)
                    fantome.kill()
                    score += 1
                    texte2.image = police.render("Score : " + str(score), 1, (10, 10, 10), (0, 128, 128))
                    # Ajout de nouveaux fantômes et murs aléatoires
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

            # Gestion des collisions avec les murs
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

    # Affichage des sprites à l'écran
    liste_des_sprites.draw(fenetre)
    pygame.display.flip()
    clock.tick(60)

# Quitter le jeu
pygame.quit()