import pygame, sys

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
fenetre_width = 800
fenetre_height = 600
fenetre = pygame.display.set_mode((fenetre_width, fenetre_height))
pygame.display.set_caption("Vecteur 3D")
timer = pygame.time.Clock()

# Position du vecteur en 3D
h = 300
walls = [(1, 0), (1, 1), (1, 2), (1, 3)]

# Convertir les coordonnées 3D en coordonnées 2D pour l'affichage sur l'écran
def create_text(x, y, size, color, text):
    # Créer une police avec la taille donnée
    font = pygame.font.Font("data/font/5x5.ttf", size)

    # Créer une surface de texte avec la police et la couleur données
    text_surface = font.render(text, True, color)

    # Obtenir la position du texte
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)

    # Afficher le texte sur la fenêtre Pygame
    pygame.display.get_surface().blit(text_surface, text_rect)
    
def project_3d_to_2d(pm1, pm2):
    global h, pz
    if pm1[2] + 0.1 + pz > 0 and pm2[2] + 0.1 + pz > 0:
        x, y, z = pm1
        
        z += 0.1 + pz
        
        p1 = (x/z*h + fenetre.get_width()/2, y/z*h + fenetre.get_height()/2)
    
        
        x, y, z = pm2
        
        z += 0.1 + pz
        
        p2 = (x/z*h + fenetre.get_width()/2, y/z*h + fenetre.get_height()/2)
        
        
        
        pygame.draw.line(fenetre, (0, 255, 0), p1, p2)
def pr_wall(wall):
        #print(wall, wall[0], wall[1])
        project_3d_to_2d((wall[0], 1, wall[1]), (wall[0], 1, wall[1] + 1))
        
        project_3d_to_2d((wall[0], -1.5, wall[1]), (wall[0], -1.5, wall[1] + 1))
        
        project_3d_to_2d((wall[0], -1.5, wall[1]), (wall[0], 1, wall[1]))
        
        project_3d_to_2d((wall[0], -1.5, wall[1] + 1), (wall[0], 1, wall[1] + 1))
        
        
        project_3d_to_2d((wall[0]-2, 1, wall[1]), (wall[0]-2, 1, wall[1] + 1))
        
        project_3d_to_2d((wall[0]-2, -1.5, wall[1]), (wall[0]-2, -1.5, wall[1] + 1))
        
        project_3d_to_2d((wall[0]-2, -1.5, wall[1]), (wall[0]-2, 1, wall[1]))
        
        project_3d_to_2d((wall[0]-2, -1.5, wall[1] + 1), (wall[0]-2, 1, wall[1] + 1))
        
        
        project_3d_to_2d((wall[0]-2, 1, wall[1]), (wall[0], 1, wall[1]))
        
        project_3d_to_2d((wall[0]-2, 1, wall[1] + 1), (wall[0], 1, wall[1] + 1))
        
        
        project_3d_to_2d((wall[0]-2, -1.5, wall[1]), (wall[0], -1.5, wall[1]))
        
        project_3d_to_2d((wall[0]-2, -1.5, wall[1] + 1), (wall[0], -1.5, wall[1] + 1))
        


# Boucle principale du jeu
running = True


pz = 0

Z = False
S = False

n = 0

while running:
    fenetre.fill((0, 0, 0))
    timer.tick(60)
    
    if Z:
       pz -= 0.025 
    if S:
        pz += 0.025
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Z = True
            if event.key == pygame.K_DOWN:
                S = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Z = False
            if event.key == pygame.K_DOWN:
                S = False
        
    project_3d_to_2d((1, 0, 1-pz), (-1, 0, 1-pz))
    
    project_3d_to_2d((0, 0, 1-pz), (0, 1, 1-pz))
    
    for i in range(len(walls)):
        pr_wall(walls[i])
    
    create_text(30, 10, 20, (0, 255, 0), str(-int(pz*100)/100))
    
    create_text(30, 30, 20, (0, 255, 0), str(int(timer.get_fps())))
    
    pygame.display.flip()

