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
        
    


    for i in range(n):
        for j in range(n):
            fenetre = pygame.display.set_mode((640, 480))
                        
            fenetre.fill((200,200,200))
            
            if grid[i][j]==1:
                graphismes(5)
                perso8 = pygame.image.load("Perso1.png").convert_alpha()
                L.append((perso1,(j*128,i*96)))
                
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
                
            if grid[i][j]==16:
                graphismes(5)
                perso16 = pygame.image.load("Perso16.png").convert_alpha()
                L.append((perso16,(j*128,i*96)))
            if grid[i][j]==32:
                graphismes(5)
                perso32 = pygame.image.load("Perso32.png").convert_alpha()
                L.append((perso32,(j*128,i*96)))
            if grid[i][j]==64:
                graphismes(5)
                perso64 = pygame.image.load("Perso64.png").convert_alpha()
                L.append((perso64,(j*128,i*96)))
            if grid[i][j]==128:
                graphismes(5)
                perso128 = pygame.image.load("Perso64.png").convert_alpha()
                L.append((perso128,(j*128,i*96)))
            if grid[i][j]==256:
                graphismes(5)
                perso256 = pygame.image.load("Perso256.png").convert_alpha()
                L.append((perso256,(j*128,i*96)))
            if grid[i][j]==512:
                graphismes(5)
                perso512 = pygame.image.load("Perso512.png").convert_alpha()
                L.append((perso512,(j*128,i*96)))
            if grid[i][j]==1024:
                graphismes(5)
                perso1024 = pygame.image.load("Perso1024.png").convert_alpha()
                L.append((perso1024,(j*128,i*96)))
            if grid[i][j]==2048:
                graphismes(5)
                perso2048 = pygame.image.load("Perso2048.png").convert_alpha()
                L.append((perso2048,(j*128,i*96)))
            
    continuer=True
    while continuer:
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT:
                continuer = 0
                        
        for i in range(len(L)):
                            
            fenetre.blit(L[i][0], L[i][1])
        graphismes(5) 
        pygame.display.flip()
       
           
            
                        
                            
grid_to_graphismes([[2,0,0,0],[0,2048,0,4],[0,0,0,0],[8,0,0,0]])




    


