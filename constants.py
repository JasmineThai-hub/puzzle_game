import pygame

# Initialize pygame for fonts
pygame.init()

# Constants
TILE_SIZE = 100
BOARD_SIZE = 4
WIDTH, HEIGHT = BOARD_SIZE * TILE_SIZE, BOARD_SIZE * TILE_SIZE
BACKGROUND_COLOR = (255, 255, 255)
TILE_COLOR = (0, 128, 85)
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.SysFont('comicsansms', 36)
BORDER_SIZE = 5  # Width of the border in pixels
BORDER_COLOR = (0, 0, 0)  # Color of the border, set to black
n = 4 ## puzzle size 4x4
shuffle_num = 50

# Additional constants for buttons
BUTTON_COLOR = (150, 150, 150)
BUTTON_HOVER_COLOR = (100, 100, 100)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_FONT = pygame.font.SysFont('comicsansms', 18)
