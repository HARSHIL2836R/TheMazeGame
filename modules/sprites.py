import pygame

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, image: pygame.Surface, width: int, height: int)->None: 
        super().__init__()
        self.image = image
        pygame.draw.rect(screen, screen.get_at((0,0)),[0,0,width,height])
        self.rect = self.image.get_rect() 