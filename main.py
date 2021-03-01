import pygame
from game import Game
pygame.init()

# genere la fenetre de notre jeu
pygame.display.set_caption("Jeu")
screen = pygame.display.set_mode((1200, 700))
background = pygame.image.load('./assets/bg.jpg')

# charger notre jeu
game = Game()

running = True

# boucle tant que cette condition est vrai

while running:

    # arriere plans
    screen.blit(background, (0, -200))

    # image joueur
    screen.blit(game.player.image, game.player.rect)

    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # si le joueur veut aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 1040:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -38:
        game.player.move_left()

    # mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'evenement est l'ouverture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #si un joueur appuie sur le clavier
        elif event.type == pygame.KEYDOWN:
            # quelle touche a été utilisée
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False