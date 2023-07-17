import arcade
from display import Display


PADDING = 32
SQUARE_SIZE = 64
SCREEN_WIDTH = 8 * SQUARE_SIZE + PADDING
SCREEN_HEIGHT = 8 * SQUARE_SIZE + PADDING
SCREEN_TITLE = "pyChess"


def main():
    game = Display(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,
                   square_size=SQUARE_SIZE, padding=PADDING)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()