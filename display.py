import cfg
import arcade
from helper import *
import os


class DisplayPiece(arcade.Sprite):

    def __init__(self, piece: int, spritesheet):
        super().__init__()
        self.scale = cfg.SQUARE_SIZE * (1/640)
        self.texture = spritesheet[get_sprite_from_piece(piece)]


    def set_board_position(self, idx):
        """
        Sets the coordinates of the sprite based on board index
        """
        x, y = flat_to_xy(idx)
        self.center_x = x * cfg.SQUARE_SIZE + cfg.SQUARE_SIZE / 2 + cfg.PADDING / 2
        self.center_y = y * cfg.SQUARE_SIZE + cfg.SQUARE_SIZE / 2 + cfg.PADDING / 2

    
    def set_xy_board_position(self, x, y):
        """
        Sets the coordinates of the sprite based on board position
        """
        self.center_x = x * cfg.SQUARE_SIZE + cfg.SQUARE_SIZE / 2 + cfg.PADDING / 2
        self.center_y = y * cfg.SQUARE_SIZE + cfg.SQUARE_SIZE / 2 + cfg.PADDING / 2


class Display(arcade.Window):

    def __init__(self, width, height, title, square_size=None, padding=None):
        self.display_size = (width, height)
        self.square_size = 64 if square_size is None else square_size
        self.padding = 0 if padding is None else padding
        self.highlights = None
        self.hover_square = None
        self.piece_sprites = None

        # Spritesheet setup
        sprite_path = os.path.join(os.getcwd(), 'assets', 'Chess_Pieces_Sprite.png')
        self.spritesheet = arcade.load_spritesheet(sprite_path, 3840 / 6, 1280 / 2, 6, 12, 0)

        # Window setup
        super().__init__(width, height, title)
        arcade.set_background_color(cfg.BACKGROUND)


    def on_draw(self):
        self.clear()
        self.draw_squares()
        self.piece_sprites.draw()

        
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
        # Update the hover square
        self.hover_square = self.get_hover_square(x, y)
        if self.hover_square is not None:
            self.hover_square_idx = xy_to_flat(*self.hover_square)
    
        
    def on_mouse_press(self, x, y, button, modifiers):
        # TODO: Implement piece dragging
        # 1. Get the piece at the mouse position
        # 2. Check if its a left clic
        # 3. If it is, set the piece as the dragging piece
        # 4. Attach the piece to the mouse
        # 5. If the piece is dropped, check if the move is valid
        # 6. If the move is valid, move the piece
        # 7. If the move is invalid, return the piece to its original position
        # 8. If the piece is dropped outside the board, return the piece to its original position
        pass


    def on_mouse_release(self, x, y, button, modifiers):
        # TODO: Other part of piece dragging
        # 1. Check if there is a piece being dragged currently
        # 2. If there is, check if the piece is over a square
        # 3. If it is, check if the move is valid
        # 4. If the move is valid, move the piece
        # 5. If the move is invalid, return the piece to its original position
        # 6. If the piece is dropped outside the board, return the piece to its original position
        pass


    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass


    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass


    def add_piece(self, piece: int, idx: int):
        p = DisplayPiece(piece, self.spritesheet)
        p.set_board_position(idx)
        self.piece_sprites.insert(idx, p)
    

    def remove_piece(self, idx: int):
        self.piece_sprites.pop(idx)


    def update_board(self, b):
        # Update the board
        # TODO: This is sloppy, we should not redraw all pieces every time
        self.piece_sprites = arcade.SpriteList()
        for i, piece in enumerate(b.board):
            if piece != 0:
                self.add_piece(piece, i)


    def draw_squares(self):
        # Draw the game squares
        for x in range(8):
            for y in range(8):
                # TODO: Rework highlighting
                col = cfg.WHITE_COLOR if (x % 2) ^ (y % 2) else cfg.BLACK_COLOR
                arcade.draw_xywh_rectangle_filled(x*self.square_size + self.padding/2,
                                                  y*self.square_size + self.padding/2,
                                                  self.square_size, self.square_size, col)


    def get_hover_square(self, x, y):
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

        return hx, hy