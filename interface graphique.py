import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

fenetre.fill((200,200,200))
perso = pygame.image.load("perso0.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

def graphismes(n):
    for i in range(n):
        pygame.draw.line(fenetre,(255,0,0),((640//n)*i,0),((640//n)*i,480))
        pygame.draw.line(fenetre,(255,0,0),(0,(480//n)*i),((640,(480//n)*i)))

#Rafraîchissement de l'écran
pygame.display.flip()





#BOUCLE INFINIE
continuer = 1
while continuer:

    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0 
        if event.type == KEYDOWN:
            if event.key == K_UP:
                print("Up")
            if event.key == K_DOWN:
                print("Down")
                position_perso = position_perso.move(0,40)
                pygame.display.flip()

            if event.key == K_RIGHT:
                print("right")
            if event.key == K_LEFT:
                print("left")
            
            graphismes(5)
            pygame.display.flip()
            










