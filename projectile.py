import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player, game):
        super().__init__()
        self.game = game
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        if self.rect.x > 1200:
            self.remove()
        for monster in self.game.check_collision(self, self.game.all_monsters):
            self.remove()
            monster.get_damage(self.player.attack)

