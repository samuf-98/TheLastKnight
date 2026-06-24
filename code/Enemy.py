from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] #06.13

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    #06.11
    def shoot(self):
        #06.14
        self.shot_delay -= 1  # Decrementando o valor do shot_delay
        if self.shot_delay == 0:  # Se shot_delay for igual a 0, faça...
            self.shot_delay = ENTITY_SHOT_DELAY[self.name] ##shot_delay recebe o valor da const ENTITY_SHOT_DELAY novamente (reset)
        #!06.14
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery)) #retorna a instância do tiro
    #!06.11


