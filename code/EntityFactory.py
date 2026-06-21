import random

from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIN_WIDTH, WIN_HEIGHT


#03.04
class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = [] #Lista criada para armazenar as imagens do Background
                for i in range(3):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg

            #04.02
            case 'Player1':
                return Player('Player1', position=(0, WIN_HEIGHT/3))

            #04.07
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(150, WIN_HEIGHT - 200)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(150, WIN_HEIGHT - 200)))
            case 'Enemy3':
                return Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(150, WIN_HEIGHT - 200)))

#!03.04
