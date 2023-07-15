# Starating fen
start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Unicode characters for the board
mt = u'\u00b7' # eMpTy space
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

class Board:


    def __init__(self, fen=None) -> None:
        if fen is None:
            fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.board = self.gen_from_fen(fen) # 8x8 board representation as 1d array
        self.pieces = self.gen_pieces()     # datastructure storing pieces and their information
        self.to_move = fen.split(" ")[1]    # w or b
        self.castling = fen.split(" ")[2]   # KQkq, or - if no castling
        self.en_passant = fen.split(" ")[3] # e3, or - if no en passant
        self.halfmove = fen.split(" ")[4]   # counter for 50 move rule
        self.fullmove = fen.split(" ")[5]   # counter for full moves
    

    def __str__(self) -> str:
        ret = ''
        for i in range(8, 0, -1): # 8 to 1
            ret += str(i) + ' '
            for j in range(8, 0, -1):
                idx = (i*8) - j
                if self.board[idx] is None:
                    ret += mt + ' '
                else:
                    ret += pieces[self.board[idx]] + ' '
            ret += '\n'
        ret += '  a b c d e f g h'
        return ret
        

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
    

b = Board()
while True:
    print('\n' + str(b))
    print('\nEnter a move (or q to quit): ', end='')
    inp = input()
    if inp == 'q':
        exit()
    b.move(inp)