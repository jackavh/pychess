import cfg
import arcade
from helper import *
import os


class DisplayPiece(arcade.Sprite):

    def __init__(self, piece: int, spritesheet):
        super().__init__()
        self.piece = piece
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

    def __init__(self, width, height, title, square_size=None, padding=None, board=None):
        self.display_size = (width, height)
        self.square_size = 64 if square_size is None else square_size
        self.padding = 0 if padding is None else padding
        self.highlights = None
        self.hover_square = None
        self.piece_sprites = None
        
        # Piece dragging variables
        self.dragged_piece = None
        self.drag_start = None
        self.drag_end = None
        
        self.board = board # A reference to a Board object

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
        if self.dragged_piece is not None:
            self.dragged_piece.draw()

        
    def setup(self):
        self.highlights = set()
        # self.piece_sprites = arcade.SpriteList()
        
        
        # # DEBUG: For fun, draw all the pieces on the board manually
        # self.add_piece(0b01101, 0) # white rook
        # self.add_piece(0b01100, 1) # white knight
        # self.add_piece(0b01011, 2) # white bishop
        # self.add_piece(0b01010, 3) # white queen
        # self.add_piece(0b01001, 4) # white king
        # self.add_piece(0b01011, 5) # white bishop
        # self.add_piece(0b01100, 6) # white knight
        # self.add_piece(0b01101, 7) # white rook
        # for i in range(8, 16):
        #     self.add_piece(0b01110, i) # white pawns
        # self.add_piece(0b10101, 56) # black rook
        # self.add_piece(0b10100, 57) # black knight
        # self.add_piece(0b10011, 58) # black bishop
        # self.add_piece(0b10010, 59) # black queen
        # self.add_piece(0b10001, 60) # black king
        # self.add_piece(0b10011, 61) # black bishop
        # self.add_piece(0b10100, 62) # black knight
        # self.add_piece(0b10101, 63) # black rook
        # for i in range(48, 56):
        #     self.add_piece(0b10110, i) # black pawns


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
        
        # If there is a dragged piece, attach it to the mouse
        if self.dragged_piece is not None:
            self.dragged_piece.set_position(x, y)
    
        
    def on_mouse_press(self, x, y, button, modifiers):
        if self.get_hover_square(x, y) is None:
            return
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(f'{self.get_time}click')
        #     hover = self.get_hover_square(x, y)
        #     self.drag_start = xy_to_flat(*hover)
        #     print(f"Drag start: {self.drag_start}") # DEBUG
        #     if self.board.board[self.drag_start] != 0:
        #         self.dragged_piece = self.piece_sprites[self.drag_start]
        #         self.remove_piece(self.drag_start)
        # elif button == arcade.MOUSE_BUTTON_RIGHT:
        #     # TODO: Implement arrow drawing
        #     pass
                

            



    def on_mouse_release(self, x, y, button, modifiers):
        pass
        # if button == arcade.MOUSE_BUTTON_LEFT:
        #     hover = self.get_hover_square(x, y)
        #     self.drag_end = xy_to_flat(*hover)
        #     print(f"Drag end: {self.drag_end}") # DEBUG
            
        #     # If there is no dragged piece, do nothing
        #     if self.dragged_piece is None:
        #         return
            
        #     if self.drag_end is not None:
        #         move = (self.drag_start, self.drag_end)
        #     else:
        #         # TODO: this is a hacky way to do this
        #         move = (self.drag_start, -1)

        #     outside_board = hover is None
        #     valid_move = self.board.is_legal(*move) # Should check if drag_end is None
        #     same_square = self.drag_start == self.drag_end

        #     # Return the piece to its original position
        #     if outside_board or (not valid_move) or same_square:
        #         self.add_piece(self.dragged_piece.piece, self.drag_start)
        #         self.dragged_piece = None
        #         return
            
        #     # Move the piece
        #     self.move_on_board(move)
        #     self.dragged_piece = None
        #     self.update_display_board()

            


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


    def update_display_board(self):
        # Create sprites for all pieces on the board
        self.piece_sprites = arcade.SpriteList()
        for i, piece in enumerate(self.board.board):
            if piece != 0:
                self.add_piece(piece, i)


    def move_on_board(self, move):
        if self.board.is_legal(*move):
            self.board.move_idx(*move)
        


    def draw_squares(self):
        """Cool and fun but very slow way to draw the squares"""
        # Draw the game squares
        for x in range(8):
            for y in range(8):
                # TODO: Rework highlighting
                col = cfg.WHITE_COLOR if (x % 2) ^ (y % 2) else cfg.BLACK_COLOR
                # Highlight the hover square
                if self.hover_square is not None and (x, y) == self.hover_square:
                    col = color_add(col, cfg.HOVER_COLOR)
                arcade.draw_xywh_rectangle_filled(x*self.square_size + self.padding/2,
                                                  y*self.square_size + self.padding/2,
                                                  self.square_size, self.square_size, col)
    

    def get_hover_square(self, x, y):
        """Returns the board coordinates of the square the mouse is hovering over"""""
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

        return self.get_board_coordinates(x, y)


    def get_board_coordinates(self, _x, _y):
        """Converts mouse coordinates to 2d board coordinates"""
        x = int((_x - self.padding/2) // self.square_size)
        y = int((_y - self.padding/2) // self.square_size)
        return x, y