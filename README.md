# nouveau_jeu_qui_d-chire
c'est un nouveau jeu qu'on va créer
Mix pac man/2048

Le joueur joue un chiffre (2^n ) se déplaçant dans une grille carrée. Son objectif est d'atteindre 2048. 

Pour cela, en plus du joueur il y a 2 types d'objets sur la grille de jeu : un objectif et un ennemi. L'objectif est un chiffre de valeur 2^(n+1) que celui du joueur ( donc 2^n ) et l'ennemi un chiffre d'une puissance de 2 en dessous de celui du joueur ( donc 2^(n-1)). 

Le joueur doit passer sur l'objectif pour voir sa valeur de n augmenter de 1 ( au premier tour, il joue un 2 et doit passer sur le 2 pour devenir un 4 ) et il doit éviter l'ennemi qui se déplace vers sous peine de game over.

Le jeu se joue au tour par tour, à chaque tour le joueur choisis une direction entre haut,bas,gauche,droite et se déplace, si il atteint l'objectif n vois sa valeur augmenter de 1 sinon n ne change pas. L'ennemi bouge d'un cran en se dirigeant vers le joueur, et il ne peut pas passer sur l'objectif. Quand l'ennemi est collé à l'objectif et se dirige vers sa case, il la saute et bouge de deux cases. L'objectif est fixe.


Fonctionnalité 1 : afficher une grille de jeu : créer une grille respectant les conditions initiales
                   

Fonctionnalité 2 : contrôler les positions des différents objets dans le jeu : ennemi, joueur, objectif grâce aux fonctions get_position


Fonctionnalité 3 : Implémenter les fonctions qui vont permettre de faire jouer un joueur et créer une fonction transformant la grille en                      string.

Fonctionnalité 4 : Déplacer les différents objets de la grille.

Fonctionnalité 5 : Assembler les différentes fonctions et finaliser notre jeu.

Sami TEST

