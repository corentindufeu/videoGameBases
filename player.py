import pygame
from projectile import Projectile


# class du joueur

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 100
        self.health = self.max_health
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('./assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.perception_gravity = 15

    def update_health_bar(self, surface):
        background_bar_color = (85, 74, 72)
        background_bar_position = [self.rect.x + 48, self.rect.y, self.max_health, 5]
        pygame.draw.rect(surface, background_bar_color, background_bar_position)
        bar_color = (111, 210, 46)  # rgb
        bar_position = [self.rect.x + 48, self.rect.y, self.health, 5]  # X, Y, Width, Heith
        pygame.draw.rect(surface, bar_color, bar_position)  # dessine un rectangle : écran, couleur, position

    def get_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("Your dead")

    def launch_projectile(self):
        # instance de projectile
        self.all_projectiles.add(Projectile(self, self.game))

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self, do_jump):
        if do_jump:
            if self.perception_gravity == 15:  # debut du saut
                self.perception_gravity = 5
            elif 5 <= self.perception_gravity <= 10:  # hauteur du saut
                self.rect.y -= self.perception_gravity
                self.perception_gravity += 0.1  # vitesse montée
            elif 10 <= self.perception_gravity <= 13:  # descente
                self.rect.y += self.perception_gravity
                self.perception_gravity += 0.1  # vitesse descente
            else:  # fin du saut
                self.rect.y = 500
                self.perception_gravity = 15
                do_jump = False

        return do_jump
