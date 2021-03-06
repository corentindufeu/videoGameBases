import pygame
from game import Game

pygame.init()

# genere la fenetre de notre jeu
pygame.display.set_caption("Jeu")
screen = pygame.display.set_mode((1200, 700))
background = pygame.image.load('./assets/bg.jpg')

# charger notre jeu
game = Game()

running: bool = True
doJump: bool = False

stopwatch_projectile: float = 0
stopwatch_spawnMonster: float = 0
spawnMonster: bool = True

# boucle tant que cette condition est vrai

while running:
    # time
    stopwatch = pygame.time.get_ticks()
    stopwatchSeconds = int(stopwatch/1000)

    # arriere plans
    screen.blit(background, (0, -200))

    # image joueur
    screen.blit(game.player.image, game.player.rect)

    game.player.update_health_bar(screen)

    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # applique l'ensemble des images de mon groupe de monstres
    game.all_monsters.draw(screen)

    # spawn monsters all 10 seconds
    if stopwatchSeconds % 5 == 0 and spawnMonster is True:
        stopwatch_spawnMonster = stopwatchSeconds + 5
        game.spawn_monster()
        spawnMonster = False
    if stopwatchSeconds >= stopwatch_spawnMonster:
        spawnMonster = True

    # recuperer les monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # si le joueur veut aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 1040:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -38:
        game.player.move_left()

    if game.pressed.get(pygame.K_UP) and doJump is False:
        doJump = True

    doJump = game.player.jump(doJump)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'evenement est l'ouverture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # si un joueur appuie sur le clavier
        elif event.type == pygame.KEYDOWN:
            # quelle touche a été utilisée
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE and stopwatch_projectile <= stopwatch:
                stopwatch_projectile = stopwatch + 150  # intervalle entre chaque projectiles en ms
                game.player.launch_projectile()  # lancer de projectiles
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

