from code.Background import Background
from code.const import WIN_WIDTH


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

#!03.04
