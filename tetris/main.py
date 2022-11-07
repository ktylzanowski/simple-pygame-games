import sys
from random import randint
import pygame


pygame.init()
pygame.font.init()

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
        [[[-1, 0], [-2, 0], [0, 0], [1, 0]], [[0, 0], [0, -1], [0, 1], [0, 2]], [[0, 0], [-1, 0], [1, 0], [2, 0]],
         [[0, 0], [0, -1], [0, 1], [0, 2]]],

        [[[0, -1], [-1, -1], [-1, 0], [0, 0]]],

        [[[-1, 0], [-1, 1], [0, 0], [0, -1]], [[0, 0], [-1, 0], [0, 1], [1, 1]]],

        [[[0, 0], [-1, 0], [0, 1], [-1, -1]], [[0, 0], [1, 0], [0, 1], [-1, 1]]],

        [[[0, 0], [0, -1], [0, 1], [-1, -1]], [[0, 0], [1, 0], [-1, 0], [-1, 1]],
         [[0, 0], [0, -1], [0, 1], [1, 1]], [[0, 0], [-1, 0], [1, 0], [1, -1]]],

        [[[0, 0], [0, -1], [0, 1], [-1, 0]], [[0, 0], [1, 0], [-1, 0], [0, 1]], [[0, 0], [0, 1], [0, -1], [1, 0]],
         [[0, 0], [1, 0], [-1, 0], [0, -1]]]

    ]

    def __init__(self):
        self.x = 4
        self.y = 1
        self.kind = randint(0, len(self.shapes)-1)
        self.color = (randint(10, 250), randint(10, 250), randint(10, 250))
        self.rotation = 0

    def image(self):
        return self.shapes[self.kind][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shapes[self.kind])

class Game(object):
    time, speed, time_limit = 0, 60, 2000
    score_font = pygame.font.SysFont('arial', 68)

    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = [[0 for _ in range(w)] for _ in range(h)]
        self.score = 0
        self.gamemode = True
        self.figure = Figure()
        self.run()

    def new_Figure(self):
        self.figure = Figure()

    def drawGrid(self):
        for x in range(0, playWidth, CUBE):
            for y in range(0, HEIGHT, CUBE):
                rect = pygame.Rect(x, y, CUBE, CUBE)
                pygame.draw.rect(self.WIN, BLACK, rect, 1)

    def draw(self):
        self.WIN.fill(WHITE)
        self.drawGrid()
        txt_score = self.score_font.render("SCORE:", True, BLACK)
        score = self.score_font.render(str(self.score), True, BLACK)
        self.WIN.blit(txt_score, (400, 50))
        self.WIN.blit(score, (480, 120))
        for i in range(4):
            pygame.draw.rect(self.WIN, self.figure.color,
                             [CUBE * (self.figure.image()[i][0] + self.figure.x) + 1,
                              CUBE * (self.figure.image()[i][1] + self.figure.y) + 1,
                              CUBE - 2, CUBE - 2])

        for i in range(h):
            for j in range(w):
                if self.board[i][j] != 0:
                    pygame.draw.rect(self.WIN, self.board[i][j], [j * CUBE + 1, i * CUBE + 1, CUBE-2, CUBE-2])

        pygame.display.update()

    def check_borders(self, d):
        collision = False
        for i in range(4):
            x1 = self.figure.image()[i][0] + self.figure.x
            if x1 + d >= w or 0 > x1 + d:
                collision = True
        return collision

    def check_y(self):
        collision = False
        for i in range(4):
            x1 = self.figure.image()[i][0] + self.figure.x
            y1 = self.figure.image()[i][1] + self.figure.y
            if y1 + 1 == h or self.board[y1+1][x1] != 0:
                collision = True
        return collision

    def check_rotate(self):
        actual_rotate = self.figure.rotation
        self.figure.rotate()
        for i in range(4):
            x1 = self.figure.image()[i][0] + self.figure.x
            if x1 > w - 1 or 0 > x1:
                self.figure.rotation = actual_rotate

    def check_line(self):
        for i in range(0, h):
            line_count = 0
            for j in range(0, w):
                if self.board[i][j] != 0:
                    line_count += 1
                else:
                    continue
            if line_count == w:
                return i
        return False

    def clear_line(self):
        if self.check_line():
            i = self.check_line()
            while i > 0:
                for j in range(0, w):
                    self.board[i][j] = self.board[i-1][j]
                i -= 1
            self.score += 1

    def freeze(self):
        if self.check_y():
            for i in range(4):
                x1 = self.figure.image()[i][0] + self.figure.x
                y1 = self.figure.image()[i][1] + self.figure.y
                self.board[y1][x1] = self.figure.color
            self.new_Figure()

    def gameover(self):
        if self.board[1][4] != 0:
            pygame.quit()
            sys.exit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.figure.y += 1
                if event.key == pygame.K_LEFT and not self.check_borders(-1):
                    self.figure.x -= 1
                if event.key == pygame.K_RIGHT and not self.check_borders(1):
                    self.figure.x += 1
                if event.key == pygame.K_UP:
                    self.check_rotate()

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.draw()
            self.event()
            self.freeze()
            self.clear_line()
            self.gameover()
            self.time += self.speed
            if self.time > self.time_limit:
                self.time = 0
                self.figure.y += 1

if __name__ == "__main__":
    game = Game()