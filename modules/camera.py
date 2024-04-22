"""Module to store the class Camera"""

from modules.player import Player


class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def update(self, player: Player):
        self.x = player.rect.x - self.width / 2
        self.y = player.rect.y - self.height / 2

    def draw(self, screen, sprites):
        for sprite in sprites:
            screen.blit(sprite.image, (sprite.rect.x - self.x, sprite.rect.y - self.y))