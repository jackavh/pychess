from piece_old import Piece


class Pieces():

    def __init__(self) -> None:
        self.white = []
        self.black = []
        self.all = []
    
    def add_piece(self, piece):
        if piece.color:
            self.white.append(piece)
        else:
            self.black.append(piece)
        self.all.append(piece)
    
    def gen_piece(self, piece, pos):
        p = Piece(piece, pos)
        self.add_piece(p)
        return p