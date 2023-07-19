import arcade
from helper import *
import os


# Size globals
PADDING = 64
SQUARE_SIZE = 128
SCREEN_WIDTH = 8 * SQUARE_SIZE + PADDING
SCREEN_HEIGHT = 8 * SQUARE_SIZE + PADDING
SCREEN_TITLE = "pyChess"

# Color globals
HIGHLIGHT_COLOR = (0xFF, 0xa1, 0xa1)
WHITE_COLOR = (0xEF, 0xD9, 0xB5)
BLACK_COLOR = (0xb4, 0x88, 0x63)
BACKGROUND  = (0x29, 0x27, 0x21)

# Spritesheet globals
PIECE_SPRITE_SHEET = os.path.join(os.getcwd(), 'assets', 'Chess_Pieces_Sprite.png')
PIECE_SPRITES = arcade.load_spritesheet(PIECE_SPRITE_SHEET,
                                        3840 / 6, 1280 / 2,
                                        6, 12, 0)


class DisplayPiece(arcade.Sprite):

    def __init__(self, piece: int):
        super().__init__()
        self.scale = SQUARE_SIZE * (1/640)
        self.texture = PIECE_SPRITES[get_sprite_from_piece(piece)]
        


    def set_board_position(self, idx):
        """
        Sets the coordinates of the sprite based on board index
        """
        x, y = flat_to_xy(idx)
        self.center_x = x * SQUARE_SIZE + SQUARE_SIZE / 2 + PADDING / 2
        self.center_y = y * SQUARE_SIZE + SQUARE_SIZE / 2 + PADDING / 2

    
    def set_xy_board_position(self, x, y):
        """
        Sets the coordinates of the sprite based on board position
        """
        self.center_x = x * SQUARE_SIZE + SQUARE_SIZE / 2 + PADDING / 2
        self.center_y = y * SQUARE_SIZE + SQUARE_SIZE / 2 + PADDING / 2


class Display(arcade.Window):

    def __init__(self, width, height, title, square_size=None, padding=None):
        self.display_size = (width, height)
        self.square_size = 64 if square_size is None else square_size
        self.padding = 0 if padding is None else padding
        self.highlights = None
        self.hover_square = None
        self.piece_sprites = None
        
        super().__init__(width, height, title)
        arcade.set_background_color(BACKGROUND)


    def on_draw(self):
        self.clear()

        # Draw the game squares
        for x in range(8):
            for y in range(8):
                # Manage highlighting
                highlighted = (x % self.square_size, y % self.square_size) in self.highlights
                col = WHITE_COLOR if (x % 2) ^ (y % 2) else BLACK_COLOR
                if highlighted:
                    col = color_mul(HIGHLIGHT_COLOR, col)
                
                # Highlight the hover square
                if self.hover_square == (x, y):
                    col = color_mul(HIGHLIGHT_COLOR, col)
                    
                # Draw the square
                arcade.draw_xywh_rectangle_filled(x*self.square_size + self.padding/2,
                                                  y*self.square_size + self.padding/2,
                                                  self.square_size,
                                                  self.square_size,
                                                  col)
        
        # DEBUG: write the hover square to the screen
        # debug_str = f'Hover square: {self.hover_square}\nHighlighted: {self.highlights}'
        # arcade.draw_text(debug_str, 16, self.display_size[1] - 32, arcade.color.BLACK, 16,
        #                  multiline=True, width=self.display_size[0] - 32)

        # Draw the pieces
        self.piece_sprites.draw()

        

    def add_piece(self, piece: int, idx: int):
        p = DisplayPiece(piece)
        p.set_board_position(idx)
        self.piece_sprites.append(p)

    
    def setup(self):
        self.highlights = set()
        self.piece_sprites = arcade.SpriteList()
        
        
        # DEBUG: For fun, draw all the pieces on the board manually
        self.add_piece(0b01101, 0) # white rook
        self.add_piece(0b01100, 1) # white knight
        self.add_piece(0b01011, 2) # white bishop
        self.add_piece(0b01010, 3) # white queen
        self.add_piece(0b01001, 4) # white king
        self.add_piece(0b01011, 5) # white bishop
        self.add_piece(0b01100, 6) # white knight
        self.add_piece(0b01101, 7) # white rook
        for i in range(8, 16):
            self.add_piece(0b01110, i) # white pawns
        self.add_piece(0b10101, 56) # black rook
        self.add_piece(0b10100, 57) # black knight
        self.add_piece(0b10011, 58) # black bishop
        self.add_piece(0b10010, 59) # black queen
        self.add_piece(0b10001, 60) # black king
        self.add_piece(0b10011, 61) # black bishop
        self.add_piece(0b10100, 62) # black knight
        self.add_piece(0b10101, 63) # black rook
        for i in range(48, 56):
            self.add_piece(0b10110, i) # black pawns




    def update(self, delta_time):
        pass


    def on_key_press(self, key, modifiers):
        pass


    def on_key_release(self, key, modifiers):
        pass


    def on_mouse_motion(self, x, y, delta_x, delta_y):
        # Handle hover square
        in_left = x > self.padding/2
        in_right = x < self.square_size*8 + self.padding/2
        in_top = y < self.square_size*8 + self.padding/2
        in_bottom = y > self.padding/2
        x_in_bounds = in_left and in_right
        y_in_bounds = in_top and in_bottom

        # Catch out of bounds
        if not x_in_bounds and not y_in_bounds:
            self.hover_square = None
            return
        # Get board coordinates

        hx = int((x - self.padding/2) // self.square_size)
        hy = int((y - self.padding/2) // self.square_size)
        # Update the hover square

        self.hover_square = (hx, hy)
    
        



    def on_mouse_press(self, x, y, button, modifiers):
        pass


    def on_mouse_release(self, x, y, button, modifiers):
        pass


    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass


    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass


# Run the game
def main():
    game = Display(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,
                   square_size=SQUARE_SIZE, padding=PADDING)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()