from settings import *
from random import choice, randint
class Objects(object):

    def __init__(self, game):
        self.player1 = pygame.Rect(50, HALF_OF_HEIGHT - 50, 10, 100)
        self.player2 = pygame.Rect(WIDTH - 50, HALF_OF_HEIGHT - 50, 10, 100)

        self.ball = pygame.Rect(HALF_OF_WIDTH - 10, randint(50, HEIGHT - 50), 30, 30)

        self.ball_speedx = 12 * choice(launch_direction)
        self.ball_speedy = 12 * choice(launch_direction)

        self.game = game

    def player1_animation(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and self.player1.y > 0:
            self.player1.y -= PLAYER_SPEED
        if keys_pressed[pygame.K_s] and self.player1.y < HEIGHT - 100:
            self.player1.y += PLAYER_SPEED

    def player2_animation(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and self.player2.y > 0:
            self.player2.y -= PLAYER_SPEED
        if keys_pressed[pygame.K_DOWN] and self.player2.y < HEIGHT - 100:
            self.player2.y += PLAYER_SPEED

    def player2_animation_for_single(self):
        if self.player2.center[1] > self.ball.center[1] and self.player2.y > 0 and \
                self.ball_speedx > 0:
            self.player2.y -= PLAYER2_SPEED
        if self.player2.center[1] < self.ball.center[1] and self.player2.y < HEIGHT - 100 and\
                self.ball_speedx > 0:
            self.player2.y += PLAYER2_SPEED

    def ball_animation(self):
        self.ball.x += self.ball_speedx
        self.ball.y += self.ball_speedy

        if self.ball.top <= 0 and self.ball_speedy < 0:
            self.ball_speedy *= -1

        if self.ball.bottom >= HEIGHT and self.ball_speedy > 0:
            self.ball_speedy *= -1

        if self.ball.colliderect(self.player1) and self.ball_speedx < 0:
            self.ball_speedx *= -1
            self.ball_speedy = -1 * (self.player1.center[1] - self.ball.y - 15) / 5

        if self.ball.colliderect(self.player2) and self.ball_speedx > 0:
            self.ball_speedx *= -1
            self.ball_speedy = -1 * (self.player2.center[1] - self.ball.y - 15) / 5

    def misses(self):
        if self.ball.left + 60 < 0:
            self.game.green_score += 1
            self.if_misses()
        if self.ball.right - 60 > WIDTH:
            self.game.red_score += 1
            self.if_misses()

    def if_misses(self):
        self.ball = pygame.Rect(HALF_OF_WIDTH - 10, randint(50, HEIGHT - 50), 30, 30)
        self.ball_speedx = 12 * choice(launch_direction)
        self.ball_speedy = 12 * choice(launch_direction)