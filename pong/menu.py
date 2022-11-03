from settings import *

class Menu(object):
    def __init__(self, game):
        self.SINGLE = pygame.Rect((HALF_OF_WIDTH - 100, 265, 200, 80))
        self.MULTI = pygame.Rect((HALF_OF_WIDTH - 100, 410, 200, 80))
        self.game = game

    def draw_menu(self):
        self.game.WIN.fill(WHITE)

        pygame.draw.rect(self.game.WIN, BLACK, (HALF_OF_WIDTH - 110, 255, 220, 100))
        pygame.draw.rect(self.game.WIN, BLACK, (HALF_OF_WIDTH - 110, 400, 220, 100))

        single_color = multi_color = (215, 126, 126)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if HALF_OF_WIDTH + 110 >= mouse_x >= HALF_OF_WIDTH - 110 and 345 >= mouse_y >= 265:
            single_color = (215, 100, 100)
        if HALF_OF_WIDTH + 110 >= mouse_x >= HALF_OF_WIDTH - 110 and 490 >= mouse_y >= 410:
            multi_color = (215, 100, 100)

        pygame.draw.rect(self.game.WIN, single_color, self.SINGLE)
        pygame.draw.rect(self.game.WIN, multi_color, self.MULTI)
        text_single = menu_font.render('Single-player ', True, BLACK)
        text_multi = menu_font.render('Multi-player', True, BLACK)
        self.game.WIN.blit(text_single, (WIDTH/2 - 70, 285))
        self.game.WIN.blit(text_multi, (WIDTH/2 - 60, 430))

        text_left = menu_font.render("W - UP    S - DOWN", True, BLACK)
        text_right = menu_font.render("↑ - UP    ↓ - DOWN", True, BLACK)
        text_center = menu_font.render("ESC - MENU", True, BLACK)
        self.game.WIN.blit(text_left, (50, 100))
        self.game.WIN.blit(text_right, (WIDTH - 280, 100))
        self.game.WIN.blit(text_center, (HALF_OF_WIDTH - 80, 100))

        pygame.display.update()

    def back_to_menu(self):

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE]:
            CLICK.play()
            self.game.__init__()