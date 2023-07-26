from piece_old import Piece
from pieces import Pieces


# Starating fen
start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Unicode characters for the board
mt = u'\u00b7' # eMpTy space
marker = u'\u25cf'   # marker for possible moves
pieces = {           # These colors are inverted, console black is white
    'P' : u'\u265F', # White Pawn
    'R' : u'\u265C', # White Rook
    'N' : u'\u265E', # White Knight
    'B' : u'\u265D', # White Bishop
    'Q' : u'\u265B', # White Queen
    'K' : u'\u265A', # White King
    'p' : u'\u2659', # Black Pawn
    'r' : u'\u2656', # Black Rook
    'n' : u'\u2658', # Black Knight
    'b' : u'\u2657', # Black Bishop
    'q' : u'\u2655', # Black Queen
    'k' : u'\u2654', # Black King
}


def string_to_pos(s):
    # Converts a string like e2 to 12, 28 to match the board array
    l = len(s)
    if l % 2 != 0: # TODO: should also check for valid characters
        raise Exception("Invalid string")
    if l == 2: # single positon
        return (int(s[1]) - 1) * 8 + (ord(s[0]) - 97)
    else:
        return [(int(s[i+1]) - 1) * 8 + (ord(s[i]) - 97) for i in range(0, l, 2)]

class Board:


    def __init__(self, fen=None) -> None:
        if fen is None:
            fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        split = fen.split(" ")
        self.board = self.gen_from_fen(fen) # 8x8 board representation as 1d array
        # self.pieces = self.gen_pieces()     # datastructure storing pieces and their information
        self.to_move = split[1]    # w or b
        self.castling = split[2]   # KQkq, or - if no castling
        ep = split[3] # en passant string
        self.en_passant = string_to_pos(ep) if ep != '-' else None # e3, or - if no en passant
        self.halfmove = split[4]   # counter for 50 move rule
        self.fullmove = split[5]   # counter for full moves

        self.markers = [] # list of markers for debugging
    

    def __str__(self) -> str:
        ret = ''
        for i in range(8, 0, -1): # 8 to 1
            ret += str(i) + ' '
            for j in range(8, 0, -1):
                idx = (i*8) - j
                if idx in self.markers:
                    ret += marker + ' '
                elif self.board[idx] is None:
                    ret += mt + ' '
                else:
                    ret += pieces[self.board[idx]] + ' '
            ret += '\n'
        ret += '  a b c d e f g h'
        return ret


    def add_marker(self, pos):
        self.markers.append(pos)
    

    def clear_markers(self):
        self.markers = []
    

    def color_at(self, pos):
        # returns 1 for white and 0 for black
        if self.board[pos] is None:
            return None
        return 1 if self.board[pos].isupper() else 0


    def get_piece(self, pos):
        return self.board[pos]
        

    def move_piece(self, s):
        move = list(s.lower())
        for c in move:
            if (c not in 'abcdefgh12345678') or (len(move) != 4):
                raise Exception("Invalid move")
        # Converts a move like e2e4 to 12, 28 to match the board array
        start = (int(move[1]) - 1) * 8 + (ord(move[0]) - 97)
        end = (int(move[3]) - 1) * 8 + (ord(move[2]) - 97)
        # Check if the move is a capture
        if self.board[end] is not None:
            self.capture(self.board[end])
        # Move the piece
        self.board[end] = self.board[start]
        self.board[start] = None
    

    def capture(self, idx):
        # TODO: Implement capture update behavior
        pass


# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
    def gen_from_fen(self, fen) -> list:
        board = [None] * 64
        for i, row in enumerate(fen.split(' ')[0].split('/')[::-1]):
            for j, c in enumerate(row):
                if c.isdigit():
                    for k in range(int(c)):
                        board[i*8+j+k] = None
                else:
                    board[i*8+j] = c
        return board
    

    def print_from_fen(self, fen):
        brd = ''
        for i, row in enumerate(fen.split(" ")[0].split("/")):
            brd += str(8-i) + " "
            for c in row:
                if c.isdigit():
                    brd += mt * int(c)
                else:
                    brd += pieces[c] + " "
            brd += "\n"
        brd += "  a b c d e f g h"
        print(brd)


    def get_en_passant(self):
        return 
    

b = Board()
while True:
    print('\n' + str(b))
    print('\nEnter a move (or q to quit): ', end='')
    inp = input()
    if inp == 'q':
        break
    b.move(inp)


knight_pos = [1, 6, 57, 62]
knights = [Piece(b, i) for i in knight_pos]
for k in knights:
    print(f'Moves for knight at {k.position}: {k.moves}')
    for m in k.moves:
        b.add_marker(m)
    print(b)
    b.clear_markers()
    print('\n')