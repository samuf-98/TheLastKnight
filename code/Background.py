from code.Entity import Entity
from code.const import WIN_WIDTH, ENTITY_SPEED


#03.03
class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    #03.05
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
    #!03.05
#!03.03

