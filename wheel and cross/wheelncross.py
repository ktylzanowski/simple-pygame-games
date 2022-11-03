import sys
from settings import *

class Game(object):
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.player = 'X'
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.clock = pygame.time.Clock()
        self.if_win = 0
        self.how_many_moves = 0
        self.run()

    def draw_window(self):
        # drawing a basic board
        self.WIN.fill(BLACK)
        pygame.draw.line(self.WIN, RED, (300, 0), (300, HEIGHT), LINEWIDTH)
        pygame.draw.line(self.WIN, RED, (600, 0), (600, HEIGHT), LINEWIDTH)
        pygame.draw.line(self.WIN, RED, (0, 200), (WIDTH, 200), LINEWIDTH)
        pygame.draw.line(self.WIN, RED, (0, 400), (WIDTH, 400), LINEWIDTH)

        # drawing wheels and cross
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 'X':
                    pygame.draw.line(self.WIN, BLUE, (50 + j * 300, 50 + i * 200), (250 + j * 300, 150 + i * 200),
                                     LINEWIDTH)
                    pygame.draw.line(self.WIN, BLUE, (50 + j * 300, 150 + i * 200), (250 + j * 300, 50 + i * 200),
                                     LINEWIDTH)
                if self.board[i][j] == 'O':
                    pygame.draw.circle(self.WIN, BLUE, (j * 300 + 150, i * 200 + 100), 70)

        pygame.display.update()

    def logic(self, x, y):
        self.how_many_moves += 1

        for i in range(3):
            # horizontal check
            if self.board[0][i] == self.player and self.board[1][i] == self.player and self.board[2][i] == self.player \
                    and not self.if_win:
                pygame.draw.line(self.WIN, WHITE, (x * 300 + 150, 0), (x * 300 + 150, HEIGHT), LINEWIDTH)
                self.if_win = 1
            # vertical check
            if self.board[i][0] == self.player and self.board[i][1] == self.player and self.board[i][2] == self.player \
                    and not self.if_win:
                pygame.draw.line(self.WIN, WHITE, (0, y * 200 + 100), (WIDTH, y * 200 + 100), LINEWIDTH)
                self.if_win = 1
            # diagonal check
            if i == 0 and self.board[i][i] == self.player and self.board[i + 1][i + 1] == self.player and \
                    self.board[i + 2][i + 2] == self.player and not self.if_win:
                pygame.draw.line(self.WIN, WHITE, (0, 0), (WIDTH, HEIGHT), LINEWIDTH)
                self.if_win = 1
            # diagonal check
            if i == 0 and self.board[i][i + 2] == self.player and self.board[i + 1][i + 1] == self.player and \
                    self.board[i + 2][i] == self.player and not self.if_win:
                pygame.draw.line(self.WIN, WHITE, (0, HEIGHT), (WIDTH, 0), LINEWIDTH)
                self.if_win = 1

        # writing out who won
        if self.if_win == 1:
            font = pygame.font.SysFont("arial", 200)
            text = font.render(self.player + " WON", True, GREEN)
            self.WIN.blit(text, (WIDTH / 2 - 300, HEIGHT / 2 - 125))

        # checking if the whole board is filled
        if self.how_many_moves == 9 and not self.if_win:
            self.__init__()
        pygame.display.update()

    def run(self):
        self.draw_window()
        while True:

            self.clock.tick(FPS)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    x = mouse_x // 300
                    y = mouse_y // 200

                    if self.board[y][x] == 0:
                        self.board[y][x] = self.player
                        self.draw_window()
                        self.logic(x, y)
                        self.player = 'O' if self.player == 'X' else 'X'
            # waiting for post-match reactions
            while self.if_win:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        self.__init__()
                    if event.type == pygame.QUIT:
                        self.if_win = 0

if __name__ == "__main__":
    game = Game()