import pygame

# créer une classe qui va gérer la notion de monstre sur notre jeu


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 100
        self.health = self.max_health
        self.attack = 1
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 540
        self.velocity = 3

    def update_health_bar(self, surface):
        background_bar_color = (85, 74, 72)
        background_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        pygame.draw.rect(surface, background_bar_color, background_bar_position)
        bar_color = (241, 53, 19)  # rgb
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]  # X, Y, Width, Heith
        pygame.draw.rect(surface, bar_color, bar_position)  # dessine un rectangle : écran, couleur, position

    def get_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        self.game.all_monsters.remove(self)
        self.kill()

    def attack_player(self):
        self.game.player.get_damage(self.attack)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            if self.rect.x == -5:
                self.die()
        else:
            self.attack_player()
            self.die()
