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
        pass