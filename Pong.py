import pygame
import sys

# Initialisation de Pygame
pygame.init()
version = "Beta"
# Paramètres initiaux
l_screen, L_screen = 1080, 720
l_rectangle, L_rectangle = 100, 25
vitesse_rectangle = 0.55
vitesse_balle_x, vitesse_balle_y = 0.65, 0.65
y = L_screen // 2
x_balle, y_balle = l_screen // 2, L_screen // 2
score = 21
vitesse_bot = 0.53
score_bot = 0

# Couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

# Configuration de la fenêtre
pygame.display.set_caption("Ping Pong Project")
screen = pygame.display.set_mode((l_screen, L_screen))

# Gestion d'image
trph = pygame.image.load("asset/trophee.png")


# Position initiale des raquettes
raquette_g_y = L_screen // 2 - l_rectangle // 2  # Position Y de la raquette gauche (fixe)
raquette_d_y = y  # Position Y de la raquette droite (mobile)

police = pygame.font.Font(None, 36)
police_end = pygame.font.Font(None, 80)

running =True
# Boucle de jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    screen.fill(NOIR)

    # Script des raquettes
    # > Raquette gauche fixe
    pygame.draw.rect(screen, BLANC, (50, raquette_g_y, L_rectangle, l_rectangle))
    if x_balle < (l_screen // 8)*5:
        if raquette_g_y + l_rectangle // 2 < y_balle:
            raquette_g_y += vitesse_bot
        elif raquette_g_y + l_rectangle // 2 > y_balle:
            raquette_g_y -= vitesse_bot

    # > Raquette droite mobile
    pygame.draw.rect(screen, BLANC, (1030, y, L_rectangle, l_rectangle))
    touche = pygame.key.get_pressed()
    if (touche[pygame.K_z] or touche[pygame.K_w] or touche[pygame.K_UP]) and y > 0:
        y -= vitesse_rectangle
    if (touche[pygame.K_s] or touche[pygame.K_DOWN]) and y < L_screen - l_rectangle:
        y += vitesse_rectangle

    # Script de la balle
    pygame.draw.circle(screen, BLANC, (x_balle, y_balle), 15)

    # Déplacement de la balle
    x_balle += vitesse_balle_x
    y_balle += vitesse_balle_y

    # Gestion des collisions de la balle avec les bords de l'écran
    if y_balle - 15 <= 0 or y_balle + 15 >= L_screen:
        vitesse_balle_y = -vitesse_balle_y

    if x_balle - 15 <= 0:
        score += 1
        x_balle, y_balle = l_screen // 2, L_screen // 2
    if x_balle + 15 >= l_screen:
        score_bot += 1
        x_balle, y_balle = l_screen // 2, L_screen // 2

    # > Gestion des score 
    texte = police.render(f"""Score \n{score_bot} : {score}""", True, BLANC)
    screen.blit(texte, (l_screen//2 - 36, 15))

    # >> Control du gagnant
    if score >= 21 or score_bot >= 21 :
        running = False


    # Collision de la balle avec les raquettes
    if (x_balle - 15 <= 50 + L_rectangle and raquette_g_y <= y_balle <= raquette_g_y + l_rectangle) or \
       (x_balle + 15 >= 1030 and y <= y_balle <= y + l_rectangle):
        vitesse_balle_x = -vitesse_balle_x

    # Mise à jour de l'affichage
    pygame.display.flip()


taille = 10
trophee = pygame.transform.scale(trph, (int(taille),int(taille)))


# Ending
running_end = True
while running_end:
    screen.fill(NOIR)
    version_txt = police.render(f"version : {version}",True,BLANC)
    screen.blit(version_txt,(900,700))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    if score_bot >= 21:
        game_over = pygame.font.Font(None, 80).render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over, (l_screen//3, L_screen//3))
        texte_end = police_end.render(f"Vous avez perdu {score_bot} à {score}.",True, BLANC)
        screen.blit(texte_end, (l_screen//5, L_screen // 2))

    elif score >= 21:
        screen.blit(trophee, (l_screen//4, L_screen//14))
        if taille < 500:
            taille += 0.5
            trophee = pygame.transform.scale(trph, (int(taille),int(taille)))

        texte_end = police_end.render(f"Vous avez gagné {score} à {score_bot}.",True, BLANC)
        screen.blit(texte_end, (l_screen//5, L_screen // 2))
    
    
    
    pygame.display.flip()
