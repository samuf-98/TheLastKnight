from abc import ABC, abstractmethod

import pygame

from code.const import ENTITY_HEALTH, ENTITY_SCORE, ENTITY_DAMAGE


class Entity(ABC):

    #03.02 - Criando a classe abstrata
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.score = ENTITY_SCORE[self.name] #07.02
        self.health = ENTITY_HEALTH[self.name] #07.03
        self.damage = ENTITY_DAMAGE[self.name] #08.07
        self.last_dmg = 'None' #08.07
    #!03.02

    @abstractmethod
    def move(self):
        pass

