import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.set_caption("PONG")

CLICK = pygame.mixer.Sound("Sounds/click.wav")
CLICK.set_volume(0.2)

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH, HEIGHT = 800, 600
HALF_OF_WIDTH, HALF_OF_HEIGHT = WIDTH/2, HEIGHT/2
PLAYER_SPEED = 9
PLAYER2_SPEED = 9
launch_direction = [1, -1]

score_font = pygame.font.SysFont('arial', 68)
menu_font = pygame.font.SysFont('arial', 30)