import pygame
import sys
from pygame import SurfaceType

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window: SurfaceType, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        #03.05
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
        pass



