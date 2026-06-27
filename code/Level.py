import pygame
import sys
import random
from pygame import SurfaceType

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.const import EVENT_ENEMY, C_BRANCO, WIN_HEIGHT, WIN_WIDTH, ENTITY_HEALTH, C_GREEN
from code.Player import Player
from code.Enemy import Enemy
from code.EntityMediator import EntityMediator

class Level:

    def __init__(self, window: SurfaceType, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = [] #04.03
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg')) #03.05
        self.entity_list.append(EntityFactory.get_entity('Player1')) #04.03
        pygame.time.set_timer(EVENT_ENEMY, 1500)#04.08

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
                if isinstance(ent, (Player, Enemy)): #Se a ent atual for do tipo Player ou Enemy, faça..
                    shoot = ent.shoot() #shoot recebe o retorno do tiro, da classe Player ou Enemy
                    if shoot is not None: #Se existir o retorno do tiro, da classe Player ou Enemy
                        self.entity_list.append(shoot) #Adicione o metodo 'shoot' da classe Player ou Enemy a entity_list
                    #07.04
                if ent.name == 'Player1':
                    self.level_text(text_size=20, text=f'Health: {ent.health} | Score: {ent.score}', text_color=C_BRANCO, text_pos=(70, 20))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #04.09
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(text_size=30, text=f'Entidades: {len(self.entity_list)}', text_color=C_BRANCO, text_pos=(70, WIN_HEIGHT - 15))

            pygame.display.flip()

            #08.05
            EntityMediator.verify_health(entity_list=self.entity_list)
            EntityMediator.verify_collision(entity_list=self.entity_list)

        pass

    #07.00
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Cinzel", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
    #!07.00



