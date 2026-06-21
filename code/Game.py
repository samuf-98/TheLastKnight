from code.Level import Level
from code.Menu import Menu

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS


class Game:

    def __init__(self):
        #02.01 - Criação da tela do jogo
        pygame.init() #?001
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) #002
        #!02.01

    def run(self):

        #02.05 - Chamar o metodo run da classe Menu
        while True:
            menu = Menu(self.window) #cria a variavel menu que recebe a classe Menu
            menu_return = menu.run() #executa o metodo run da classe Menu
        #!02.05

            if menu_return == MENU_OPTIONS[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == 1:
                pass
            else:
                pygame.quit()
                quit()



