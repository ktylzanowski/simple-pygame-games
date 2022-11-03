import sys

import pygame

w, h = 8, 16

CUBE = 50
WIDTH, HEIGHT = w * CUBE + 200, h * CUBE
playWidth = w * CUBE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

class Figure(object):
    shapes = [[1, 5, 9, 13], [4, 5, 6, 7]]
    colors = [[120, 0, 0], [0, 0, 0]]

    def __init__(self, kind, color):
        self.x = 3
        self.y = 0
        self.kind = self.shapes[kind]
        self.color = self.colors[color]
        self.rotation = 0


class Game(object):
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(w)] for _ in range(h)]
        self.figure = Figure(0, 0)
        self.run()

    def drawGrid(self):
        for x in range(0, playWidth, CUBE):
            for y in range(0, HEIGHT, CUBE):
                rect = pygame.Rect(x, y, CUBE, CUBE)
                pygame.draw.rect(self.WIN, BLACK, rect, 1)

    def draw(self):
        self.WIN.fill(WHITE)
        self.drawGrid()
        pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.draw()
            print(self.board)
            self.event()


if __name__ == "__main__":
    game = Game()