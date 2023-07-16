from board import string_to_pos


pieces = {
    0x0 : 'P',
    0x1 : 'N',
    0x2 : 'B',
    0x3 : 'R',
    0x4 : 'Q',
    0x5 : 'K',
    0x6 : 'p',
    0x7 : 'n',
    0x8 : 'b',
    0x9 : 'r',
    0xA : 'q',
    0xB : 'k',
}

pieces_inverse = {v: k for k, v in pieces.items()}

# Piece Encoding
# 0
# x
# 0 - B: Piece type and color
# 0 - F: Position
# 0 - 3: Position


def encode(piece, position):
    return (position << 4) + pieces_inverse[piece]


class Piece:

    def __init__(self, encode) -> None:
        self.encode = encode
        self.type = pieces[encode & 0xF] # Last digit of encode
        self.color = 'w' if self.type.isupper() else 'b'
        self.position = encode >> 4 # First 2 digits of encode
        self.moves = None # list of possible moves
        self.attacks = None # list of possible attacks
        self.pinned = None # True if pinned
        self.pinned_by = None # list of pieces pinning this piece
        self.pinned_to = None # list of pieces this piece is pinning
        self.pin_direction = None # direction of pin


    def gen_moves(self, board):
        if self.type == 'P':
            self.gen_moves_pawn(board)
        elif self.type == 'N':
            self.gen_moves_knight(board)
        elif self.type == 'B':
            self.gen_moves_bishop(board)
        elif self.type == 'R':
            self.gen_moves_rook(board)
        elif self.type == 'Q':
            self.gen_moves_queen(board)
        elif self.type == 'K':
            self.gen_moves_king(board)
        else:
            raise Exception("Invalid piece type")
        
    
    def gen_moves_pawn(self, board):
        self.clear() # Clears moves and attacks

        # If pinned, can only move along pinning line
        if self.pinned:
            # TODO: Implement pinning line
            # For now just return if pinned
            return
        
        # White pawn
        if (self.color == 'w'):

            # Double move behavior
            forward_is_empty = board[self.position + 16] is None
            on_second_rank = self.position in list(range(8, 16))
            if forward_is_empty and on_second_rank:
                self.moves.append(self.position + 16)
                # TODO: add en pessant here
            
            # Single move behavior
            forward_is_empty = board[self.position + 8] is None
            if forward_is_empty:
                self.moves.append(self.position + 8)
            
            # Capture behavior
            capture_left = board[self.position + 9] is not None
            capture_right = board[self.position + 7] is not None
            if capture_left:
                self.attacks.append(self.position + 9)
                self.moves.append(self.position + 9)
            if capture_right:
                self.attacks.append(self.position + 7)
                self.moves.append(self.position + 7)
            
            # En pessant behavior
            

        elif (self.color == 'b') and (self.position in list(range(48, 56))):
            if board[self.position - 16] is None:
                self.moves.append(self.position - 16)
                # TODO: add en pessant here
        
        