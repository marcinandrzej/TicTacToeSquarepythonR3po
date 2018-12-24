import pygame
from GameClass import GameClass

WINDOW_H = 500
WINDOW_W = 500


def main():

    pygame.init()

    size = [WINDOW_W, WINDOW_H]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Tic Tac Toe SQUARE!")

    done = False

    clock = pygame.time.Clock()

    game = GameClass(WINDOW_W, WINDOW_H)

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_r:
                    game.reset()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game.end:
                player_position = pygame.mouse.get_pos()
                game.update(player_position)

        game.check_end()

        game.draw(screen)

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()