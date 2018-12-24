import pygame
from TicTacToeClass import TicTacToeClass

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


class GameClass():

    def __init__(self, window_w, window_h):

        self.font = font = pygame.font.SysFont('Calibri', 30, True, False)

        self.end = False
        self.player = 1
        self.winner = True
        self.window_w = window_w
        self.window_h = window_h

        self.game = []
        for row in range(3):
            self.game.append([])
            for column in range(3):
                self.game[row].append(TicTacToeClass(row, column, self.window_w, self.window_h))
        self.game[1][1].active = True

    def reset(self):

        for row in range(3):
            for column in range(3):
                self.game[row][column].reset()
        self.game[1][1].active = True
        self.player = 1
        self.end = False

    def update(self, player_position):

        for row in range(3):
            for column in range(3):
                if self.game[row][column].active:
                    data = self.game[row][column].update(player_position, self.player)
                    if data[1] == 1:
                        self.player = data[0]
                        data2 = self.game[row][column].deactive(player_position)
                        self.game[data2[0]][data2[1]].active = True

    def check_end(self):

        for row in range(3):
            for column in range(3):
                if not self.end:
                    self.end = self.game[row][column].check_win()

        if not self.end:
            self.end = True
            self.winner = False
            for row in range(3):
                for column in range(3):
                    for i in range(3):
                        for j in range(3):
                            if self.game[row][column].grid[i][j] == 0:
                                self.end = False
                                self.winner = True

    def draw(self, screen):

        screen.fill(BLACK)

        for row in range(3):
            for column in range(3):
                self.game[row][column].draw(screen, self.window_w, self.window_h, self.font)

        wid_w = (self.window_w // 100) // 2
        wid_h = (self.window_h // 100) // 2
        x = 3 * self.window_w//10 + 3 * self.window_w//100
        y = 3 * self.window_h//10 + 3 * self.window_h//100

        pygame.draw.line(screen, YELLOW, [x + wid_w, 0], [x + wid_w, self.window_h], wid_w + 1)
        pygame.draw.line(screen, YELLOW, [2 * x + wid_w , 0], [2 * x + wid_w, self.window_h], wid_w + 1)
        pygame.draw.line(screen, YELLOW, [0, y + wid_h], [self.window_w, y + wid_h], wid_h + 1)
        pygame.draw.line(screen, YELLOW, [0, 2 * y + wid_h], [self.window_w, 2 * y + wid_h], wid_h + 1)

        if self.end:
            if self.winner:
                if self.player == 1:
                    text = self.font.render("Player 2 won", True, BLUE)
                else:
                    text = self.font.render("Player 1 won", True, BLUE)
            else:
                text = self.font.render("DRAW!", True, BLUE)
            screen.blit(text, [self.window_w // 3, self.window_h // 3])
            text = self.font.render("R to RESTART", True, BLUE)
            screen.blit(text, [self.window_w // 3, self.window_h // 2])

        pygame.display.flip()