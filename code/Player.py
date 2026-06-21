import pygame

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    #04.04
    def move(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP] and self.rect.top > 120:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT - 160:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass
