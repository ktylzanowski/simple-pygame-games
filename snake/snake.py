from settings import *
import sys
from random import randint

class Game(object):
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = pygame.Rect(CUBE * randint(0, 23), CUBE * randint(0, 13), CUBE, CUBE)
        self.food = pygame.Rect(CUBE * randint(0, 23), CUBE * randint(0, 13), CUBE, CUBE)
        self.snake_body = [self.snake.copy()]
        self.direction = (0, 0)
        self.length = 1
        self.time = 0
        self.previous_time = 50
        self.run()

    def draw(self):
        self.WIN.fill(BLACK)
        [pygame.draw.rect(self.WIN, GREEN, element) for element in self.snake_body]
        pygame.draw.rect(self.WIN, RED, self.food)
        pygame.display.update()

    def movement(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.previous_time:
            self.time = time_now

            self.snake.move_ip(self.direction)

            if self.snake.x < 0:
                self.snake.x = WIDTH
            if self.snake.x > WIDTH:
                self.snake.x = 0
            if self.snake.y > HEIGHT:
                self.snake.y = 0
            if self.snake.y < 0:
                self.snake.y = HEIGHT

            self.snake_body.append(self.snake.copy())
            self.snake_body = self.snake_body[-self.length:]

    def eating(self):
        if self.snake.center == self.food.center:
            self.food = pygame.Rect(CUBE * randint(0, 23), CUBE * randint(0, 13), CUBE, CUBE)
            self.length += 1

    def self_eating(self):
        if pygame.Rect.collidelist(self.snake, self.snake_body[:-1]) != -1:
            self.__init__()

    def food_collision(self):
        if pygame.Rect.collidelist(self.food, self.snake_body[:-1]) != -1:
            self.food = pygame.Rect(CUBE * randint(0, 23), CUBE * randint(0, 13), CUBE, CUBE)

    def event(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not self.direction == (0, CUBE):
                    self.direction = (0, -CUBE)
                if event.key == pygame.K_DOWN and not self.direction == (0, -CUBE):
                    self.direction = (0, CUBE)
                if event.key == pygame.K_LEFT and not self.direction == (CUBE, 0):
                    self.direction = (-CUBE, 0)
                if event.key == pygame.K_RIGHT and not self.direction == (-CUBE, 0):
                    self.direction = (CUBE, 0)

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.event()
            self.draw()
            self.movement()
            self.eating()
            self.food_collision()
            self.self_eating()

if __name__ == "__main__":
    game = Game()