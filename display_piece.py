from helper import *
import cfg
import arcade


class DisplayPiece(arcade.Sprite):

    def __init__(self, piece: int, spritesheet):
        super().__init__()
        self.piece = piece
        self.scale = cfg.SQUARE_SIZE * (1/640)
        self.texture = spritesheet[get_sprite_from_piece(piece)]
    

    def __str__ (self):
        return get_char_from_piece(self.piece)


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

