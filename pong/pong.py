import sys
from menu import *
from objects import *

class Game(object):
    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.mode = 0
        self.objects = Objects(self)
        self.menu = Menu(self)
        self.red_score = 0
        self.green_score = 0
        self.run()

    def draw(self):
        self.WIN.fill(BLACK)
        pygame.draw.line(self.WIN, WHITE, (HALF_OF_WIDTH, 0), (HALF_OF_WIDTH, HEIGHT))

        red_score = score_font.render(str(self.red_score), True, WHITE)
        green_score = score_font.render(str(self.green_score), True, WHITE)
        self.WIN.blit(red_score, (275, 100))
        self.WIN.blit(green_score, (WIDTH - 300, 100))

        pygame.draw.ellipse(self.WIN, BLUE, self.objects.ball)
        pygame.draw.rect(self.WIN, RED, self.objects.player1)
        pygame.draw.rect(self.WIN, GREEN, self.objects.player2)

        pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # game mode selection
            if event.type == pygame.MOUSEBUTTONDOWN and self.mode == 0:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.menu.SINGLE.x + 200 >= mouse_x >= self.menu.SINGLE.x and \
                        self.menu.SINGLE.y + 100 >= mouse_y >= self.menu.SINGLE.y:
                    self.mode = 1
                    CLICK.play()
                if self.menu.MULTI.x + 200 >= mouse_x >= self.menu.MULTI.x and self.menu.MULTI.y + 100 >= mouse_y >= \
                        self.menu.MULTI.y:
                    self.mode = 2
                    CLICK.play()

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.check_events()
            if self.mode == 0:
                self.menu.draw_menu()

            if self.mode != 0:
                self.draw()
                self.objects.ball_animation()
                self.objects.player1_animation()
                self.menu.back_to_menu()
                self.objects.misses()

            if self.mode == 1:
                self.objects.player2_animation_for_single()

            if self.mode == 2:
                self.objects.player2_animation()


if __name__ == "__main__":
    game = Game()