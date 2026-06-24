import pygame

#C
C_DOURADA = (212, 175, 55)
C_OURO = (250, 205, 155)
C_BRANCO = (240, 248, 255)

#E
ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Player1': 300,
    'Player1Shot': 1, #06.08
    'Enemy1': 200,
    'Enemy2': 250,
    'Enemy3': 300,
    'Enemy1Shot': 1, #06.12
    'Enemy2Shot': 1, #06.12
    'Enemy3Shot': 1 #06.12
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0.7,
    'Level1Bg2': 0.8,
    'Player1': 4, #04.04
    'Player1Shot': 6, #06.03
    'Enemy1': 2,
    'Enemy2': 2.5,
    'Enemy3': 3,
    'Enemy1Shot': 4, #06.12
    'Enemy2Shot': 5, #06.12
    'Enemy3Shot': 6 #06.12
}

EVENT_ENEMY = pygame.USEREVENT + 1 #04.08

ENTITY_SHOT_DELAY = {
    'Player1': 20, #06.09
    'Player2': 20, #06.09
    'Enemy1': 120, #06.13
    'Enemy2': 110, #06.13
    'Enemy3': 90 #06.13
}

#M
MENU_OPTIONS = ( #02.06
    'New Game',
    'Score',
    'Exit'
)

#P
PLAYER_KEY_SHOOT = {'Player1' : pygame.K_RCTRL} #06.04

#W
WIN_WIDTH = 1280
WIN_HEIGHT = 720

