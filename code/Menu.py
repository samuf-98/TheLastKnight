import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import C_DOURADA, WIN_WIDTH, C_BRANCO


class Menu:
    def __init__(self, window):
        #02.02 - Criação da tela do menu
        self.window = window #?003
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha() #?004
        self.rect = self.surf.get_rect(left=0, top=0) #?005
        #!02.02

    def run(self):
        #02.03 - Carregando a música do Menu
        pygame.mixer.music.load('./asset/Menu.mp3') #?006
        pygame.mixer.music.play(-1) #?007
        pygame.mixer.music.set_volume(0.3) #?008
        #!02.03

        #02.04 - Carregando as imagens na tela
        while True:
            self.window.blit(source=self.surf, dest=self.rect) #?009

            #02.06
            self.menu_text(50, "The Last", C_DOURADA, (((WIN_WIDTH/2)-150), 300))
            self.menu_text(200, "Knight", C_DOURADA, ((WIN_WIDTH / 2), 380))
            self.menu_text(70, "Começar", C_BRANCO, ((WIN_WIDTH / 2), 500))
            self.menu_text(70, "Score", C_BRANCO, ((WIN_WIDTH / 2), 580))
            self.menu_text(70, "Sair", C_BRANCO, ((WIN_WIDTH / 2), 660))
            #!02.06


            #Checagem de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip() #Atualiza a tela

            pass #Usado para manter o while em loop infinito
        #!02.04

    #02.05
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Cinzel", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
    #!02.05

