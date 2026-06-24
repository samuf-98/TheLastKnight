import pygame
from pygame import event

from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, ENTITY_SHOT_DELAY, PLAYER_KEY_SHOOT

#04.01
class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name] #06.09

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

    #06.05
    def shoot(self):
        #06.10
        self.shot_delay -=1 #Decrementando o valor do shot_delay
        if self.shot_delay == 0: #Se shot_delay for igual a 0, faça...
            self.shot_delay = ENTITY_SHOT_DELAY[self.name] #shot_delay recebe o valor da const ENTITY_SHOT_DELAY novamente
        #!06.10
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]: #Se a tecla for pressionada, faça...
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery)) #Instanciar o PlayerShot (Tiro), na no meio do Player
    #!06.05




        #self.shot_delay -= 1
        #if self.shot_delay == 00:
            #self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            #pressed_key = pygame.key.get_pressed()
            #if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                #return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

        pass
