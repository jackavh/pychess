from helper import *
import cfg
import display_piece


class Piece(object):

    def __init__(self, board=None, piece=None, color=None,
                 xy_pos=None, idx_pos=None, moves=None,
                 display=None, scale=None, sprite=None, sprite_pos=None):
        # What does a piece represent?
        self.board = None # A reference to the board object the piece is "on"
        self.id = None # For hashing purposes
        self.piece = None # The piece type, includes color. Refer to cfg.py
        self.color = None # 0 for black, 1 for white
        self.xy_pos = None # Tuple representing the position on the board
        self.idx_pos = None # Integer from 0-63
        self.moves = None # List of valid moves
        
        # Display variables
        self.display = None # The display object, inherits from arcade.Sprite
        self.scale = None # The scale of the sprite
        self.sprite = None # The sprite object
        self.sprite_pos = None # The position of the sprite on the screen

        # Initialize the piece
        self.init_piece(board, piece, color, xy_pos, idx_pos, moves,
                        display, scale, sprite, sprite_pos)
        

    def init_piece(self, board=None, piece=None, color=None,
                    xy_pos=None, idx_pos=None, moves=None,
                    display=None, scale=None, sprite=None, sprite_pos=None):
        
    
    def __str__(self) -> str:
        return get_char_from_piece(self.piece)
    

