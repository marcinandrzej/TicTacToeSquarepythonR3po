import pygame

WHITE = (255, 255, 255)
GREY = (120, 120, 120)


class TicTacToeClass():

    def __init__(self, offset_x=0, offset_y=0, window_w=500, window_h=500):

        self.circle_image = pygame.image.load("IMAGES\\Circle.png").convert()
        self.cross_image = pygame.image.load("IMAGES\\Cross.png").convert()
        self.sound = pygame.mixer.Sound("SOUNDS\\sfx_sounds_button11.wav")
        self.end_sound = pygame.mixer.Sound("SOUNDS\\game_over.ogg")

        self.cross_image.set_colorkey(WHITE)
        self.circle_image.set_colorkey(WHITE)

        self.width = window_w // 10
        self.height = window_h // 10
        self.margin_h = window_h // 100
        self.margin_w = window_w // 100

        self.end = False
        self.winner = False
        self.offset_x = offset_x * (self.width * 3 + self.margin_w * 3)
        self.offset_y = offset_y * (self.height * 3 + self.margin_h * 3)
        self.active = False

        self.grid = []
        for row in range(3):
            self.grid.append([])
            for column in range(3):
                self.grid[row].append(0)

    def check_win(self):

        if (self.grid[0][0] == self.grid [0][1] == self.grid [0][2] != 0) or \
                (self.grid[1][0] == self.grid [1][1] == self.grid [1][2] != 0) or \
                (self.grid[2][0] == self.grid [2][1] == self.grid [2][2] != 0) or \
                (self.grid[0][0] == self.grid [1][0] == self.grid [2][0] != 0) or \
                (self.grid[0][1] == self.grid [1][1] == self.grid [2][1] != 0) or \
                (self.grid[0][2] == self.grid [1][2] == self.grid [2][2] != 0) or \
                (self.grid[0][0] == self.grid [1][1] == self.grid [2][2] != 0) or \
                (self.grid[0][2] == self.grid [1][1] == self.grid [2][0] != 0):
                    self.winner = True
                    self.end = True
                    self.end_sound.play()

        return self.end

    def draw(self, screen, window_w, window_h, font):

        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == 1:
                    image = self.circle_image
                    if self.active:
                        color = WHITE
                    else:
                        color = GREY
                elif self.grid[row][col] == -1:
                    image = self.cross_image
                    if self.active:
                        color = WHITE
                    else:
                        color = GREY
                else:
                    image = None
                    if self.active:
                        color = WHITE
                    else:
                        color = GREY
                pygame.draw.rect(screen, color,
                                 [self.offset_x + self.margin_w + col * (self.width + self.margin_w), self.offset_y + self.margin_h +
                                  row * (self.height + self.margin_h), self.width, self.height])
                if image != None:
                    screen.blit(image, [self.offset_x + self.margin_w + col * (self.width + self.margin_w), self.offset_y + self.margin_h +
                                        row * (self.height + self.margin_h), self.width, self.height])
        return None

    def update(self, player_position, player):

        flag = 0
        if player_position[0] > self.offset_x and player_position[0] < self.offset_x + (3 * self.margin_w + 3*self.width) and \
            player_position[1] > self.offset_y and player_position[1] < self.offset_y + (3 * self.margin_h + 3 * self.height) and\
                self.active:
                            row = min((player_position[1] - self.offset_y) // (self.margin_h + self.height), 2)
                            col = min((player_position[0] - self.offset_x) // (self.margin_w + self.width), 2)
                            if self.grid[row][col] == 0 and not self.end:
                                self.grid[row][col] = player
                                player = player * (-1)
                                flag = 1
                                self.sound.play()
        return [player, flag]

    def deactive(self, player_position):

        row = min((player_position[1] - self.offset_y) // (self.margin_h + self.height), 2)
        col = min((player_position[0] - self.offset_x) // (self.margin_w + self.width), 2)
        self.active = False
        return [col, row]

    def reset(self):

        for row in range(3):
            for column in range(3):
                self.grid[row][column] = 0
        self.end = False
        self.winner = False
        self.active = False

        return None

