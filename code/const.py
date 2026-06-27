import pygame

#C
C_DOURADA = (212, 175, 55)
C_OURO = (250, 205, 155)
C_BRANCO = (240, 248, 255)
C_GREEN = (0, 128, 0)

#E
ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Player1': 1,
    'Player1Shot': 40,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy1Shot': 20,
    'Enemy2Shot': 20,
    'Enemy3Shot': 15
}



ENTITY_HEALTH = {#07.03
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Enemy1': 50,
    'Enemy2': 70,
    'Enemy3': 100,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1
}

ENTITY_SPEED = {
    'Level1Bg0': 0.6,
    'Level1Bg1': 0.7,
    'Level1Bg2': 0.8,
    'Player1': 4, #04.04
    'Player1Shot': 6, #06.03
    'Enemy1': 2,
    'Enemy2': 2.5,
    'Enemy3': 3,
    'Enemy1Shot': 7, #06.12
    'Enemy2Shot': 9, #06.12
    'Enemy3Shot': 12 #06.12
}

ENTITY_SCORE = { #07.02
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Player3': 0,
    'Player3Shot': 0,
    'Enemy1': 150,
    'Enemy2': 180,
    'Enemy3': 250,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0,
    'Enemy3Shot': 0
}



EVENT_ENEMY = pygame.USEREVENT + 1 #04.08

ENTITY_SHOT_DELAY = {
    'Player1': 20, #06.09
    'Player2': 20, #06.09
    'Enemy1': 150, #06.13
    'Enemy2': 130, #06.13
    'Enemy3': 100 #06.13
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

