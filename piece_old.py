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

class Piece:

    def __init__(self, board, position) -> None:
        self.type = board.get_piece(position) # type of piece
        self.color = 1 if self.type.isupper() else 0 # 0 for white, 1 for black
        self.position = position
        self.moves = self.gen_moves(board) # list of possible moves
        self.attacks = None # list of possible attacks
        self.pinned = None # True if pinned
        self.pinned_by = None # list of pieces pinning this piece
        self.pinned_to = None # list of pieces this piece is pinning
        self.pin_direction = None # direction of pin


    def gen_moves(self, board):
        if self.type.upper() == 'P':
            return self.gen_moves_pawn(board)
        elif self.type.upper() == 'N':
            return self.gen_moves_knight(board)
        elif self.type.upper() == 'B':
            return self.gen_moves_bishop(board)
        elif self.type.upper() == 'R':
            return self.gen_moves_rook(board)
        elif self.type.upper() == 'Q':
            return self.gen_moves_queen(board)
        elif self.type.upper() == 'K':
            return self.gen_moves_king(board)
        else:
            raise Exception("Invalid piece type")
        
    
    def gen_moves_knight(self, board):
        self.clear() # Clears moves and attacks
        p = self.position # Current position
        # All possible knight moves
        # TODO: Fix board wrapping (knight at a2 tries to move to a7)
        moves = []
        potential_moves = [p + 17, p + 15, # forward
                 p + 10, p - 6,  # right
                 p - 15, p - 17, # down
                 p - 10, p + 6]  # left
        # prune for out of bounds and friendly fire
        # TODO: add checks for pins in update_moves method
        for m in potential_moves:
            if (m < 0) or (m > 63):
                continue
            if board.get_piece(m) is None:
                moves.append(m)
            elif board.color_at(m) ^ self.color: # opposing color
                # TODO: add attacks method that loops through moves
                #       to find which moves are attacks
                moves.append(m)
        return moves
            

    
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
            forward_is_empty = board.get_piece(self.position + 16) is None
            on_second_rank = self.position in list(range(8, 16))
            if forward_is_empty and on_second_rank:
                self.moves.append(self.position + 16)
                # TODO: add en passant here
            
            # Single move behavior
            forward_is_empty = board.get_piece(self.position + 8) is None
            if forward_is_empty:
                self.moves.append(self.position + 8)
            
            # Capture behavior
            capture_left = board.get_piece(self.position + 9) is not None
            capture_right = board.get_piece(self.position + 7) is not None
            if capture_left:
                self.attacks.append(self.position + 9)
                self.moves.append(self.position + 9)
            if capture_right:
                self.attacks.append(self.position + 7)
                self.moves.append(self.position + 7)
            
            # En passant behavior
            
        # Black pawn
        elif (self.color == 'b') and (self.position in list(range(48, 56))):
            if board.get_piece(self.position - 16) is None:
                self.moves.append(self.position - 16)
                # TODO: add en pessant here
        
    
    def clear(self):
        self.moves = []
        self.attacks = []