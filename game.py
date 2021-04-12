import pygame
from player import Player
from monster import Monster


# class du jeu

class Game:

    def __init__(self):
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer les monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {
            "touche_fleche_gauche": True,
            "touche_fleche_droite": True
        }
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
