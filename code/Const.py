# C
import pygame

COLOR_WHITE = (255, 247, 252)
COLOR_PINK = (235, 14, 205)
COLOR_YELLOW = (240, 198, 14)
# E
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Level1Bg7': 7,
                'Level1Bg8': 8,
                'Player1': 4,
                'Player2': 4,
                'Enemy1': 2,
                'Enemy2': 1
                }
EVENT_ENEMY = pygame.USEREVENT + 1


PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w, }
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s, }
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a, }
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d, }
# M
MENU_OPTION = ('NEW GAME 1P'
               , 'NEW GAME 2P - COOPERATIVE'
               , 'NEW GAME 2P - COMPETITIVE'
               , 'EXIT')
# W
WIN_WIDTH = 512
WIN_HEIGHT = 512
