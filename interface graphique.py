import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))



def graphismes(n):
    for i in range(n):
        pygame.draw.line(fenetre,(255,0,0),((640//n)*i,0),((640//n)*i,480))
        pygame.draw.line(fenetre,(255,0,0),(0,(480//n)*i),((640,(480//n)*i)))

#Rafraîchissement de l'écran






def grid_to_graphismes(grid):
    n=len(grid)
    fenetre = pygame.display.set_mode((640, 480))
    fenetre.fill((200,200,200))
    L=[]
        
    continuer=1
    while continuer:
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                continuer = 0      #On arrête la boucle

    
            for i in range(n-1):
                for j in range(n-1):
                    fenetre = pygame.display.set_mode((640, 480))
                        
                    fenetre.fill((200,200,200))
                    if grid[i][j]==2:
                        graphismes(5)
                        perso2 = pygame.image.load("Perso2.png").convert_alpha()
                        L.append((perso2,(j*128,i*96)))
                        
                        
                    if grid[i][j]==4:
                        graphismes(5)
                        perso4 = pygame.image.load("Perso4.png").convert_alpha()
                        L.append((perso4,(j*128,i*96)))
                            
                        
                        
                    
                    if grid[i][j]==8:
                        graphismes(5)
                        perso8 = pygame.image.load("Perso8.png").convert_alpha()
                        L.append((perso8,(j*128,i*96)))
                    
                    for i in range(len(L)-1):
                            
                        fenetre.blit(L[i][0], L[i][1])
                    graphismes(5)    
                    pygame.display.flip()
                        
           
            
                        
                            
grid_to_graphismes([[2,0,0,0],[0,0,0,4],[0,0,0,0],[8,0,0,0]])


    


