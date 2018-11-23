import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))


def graphismes(n):
    for i in range(n):
        pygame.draw.line(fenetre, (255, 0, 0), ((640 // n) * i, 0), ((640 // n) * i, 480))
        pygame.draw.line(fenetre, (255, 0, 0), (0, (480 // n) * i), ((640, (480 // n) * i)))

def fenetre_game_over():

        fenetre = pygame.display.set_mode((640, 480))
        fenetre.fill((200, 200, 200))
        fenetre = pygame.display.set_mode((640, 480))

        fenetre.fill((200, 200, 200))
        graphismes(5)
        game_over = pygame.image.load("game_over").convert_alpha()
        fenetre.blit(game_over)
        pygame.display.flip()