import sys
from random import randint
import pygame

w, h = 8, 16

CUBE = 50
WIDTH, HEIGHT = w * CUBE + 200, h * CUBE
playWidth = w * CUBE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 60


class Figure(object):
    shapes = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]
    colors = [[120, 0, 0], [0, 0, 0]]

    def __init__(self):
        self.x = 2
        self.y = 0
        self.kind = randint(0, len(self.shapes) - 1)
        self.color = 0
        self.rotation = 0

    def image(self):
        return self.shapes[self.kind][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shapes[self.kind])


class Game(object):
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(w)] for _ in range(h)]
        self.figure = Figure()
        self.run()

    def new_Figure(self):
        self.figure = Figure()

    def drawGrid(self):
        for x in range(0, playWidth, CUBE):
            for y in range(0, HEIGHT, CUBE):
                rect = pygame.Rect(x, y, CUBE, CUBE)
                pygame.draw.rect(self.WIN, BLACK, rect, 1)
            if self.figure is not None:
                for i in range(4):
                    for j in range(4):
                        p = i * 4 + j
                        if p in self.figure.image():
                            pygame.draw.rect(self.WIN, self.figure.colors[self.figure.color],
                                             [CUBE * (j + self.figure.x) + 1,
                                              CUBE * (i + self.figure.y) + 1,
                                              CUBE - 2, CUBE - 2])

    def draw(self):
        self.WIN.fill(WHITE)
        self.drawGrid()
        pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.figure.y += 1
                if event.key == pygame.K_LEFT and self.figure.x >= 0:
                    self.figure.x -= 1
                if event.key == pygame.K_RIGHT and self.figure.x <= 5:
                    self.figure.x += 1
                if event.key == pygame.K_UP:
                    self.figure.rotate()

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.draw()
            self.event()


if __name__ == "__main__":
    game = Game()
