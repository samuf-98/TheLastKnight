from code.Menu import Menu

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT

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
            menu.run() #executa o metodo run da classe Menu
        #!02.05



