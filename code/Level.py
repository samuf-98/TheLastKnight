import pygame
import sys
import random
from pygame import SurfaceType

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.const import EVENT_ENEMY


class Level:

    def __init__(self, window: SurfaceType, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        #03.05
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        #04.03
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        #04.08
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):

        #03.06
        pygame.mixer.music.load('./asset/Level1.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        #!03.06
        #04.00
        clock = pygame.time.Clock()

        while True:
            #04.00
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #04.09
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            pygame.display.flip()
        pass



