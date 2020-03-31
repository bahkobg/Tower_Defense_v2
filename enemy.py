import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.speed = 1
        self.worth = 1
        self.fire_resistance = 0
        self.freeze_resistance = 0
        self.lighting_resistance = 0
        self.poison_resistance = 0

    def take_damage(self, damage):
        if self.health > 0:
            self.health -= damage

    def die(self):
        pass

    def jump(self):
        pass

    def move(self):
        pass

    def update(self, *args):
        pass

    def animation(self):
        pass

    def draw(self):
        pass
