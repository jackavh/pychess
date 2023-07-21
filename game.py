import cfg
import arcade
from helper import *
from display import Display


class Board():

    def __init__(self) -> None:
        self.board = [cfg.NONE] * 64
        self.legal_moves = []
        # Test pieces
        self.board[0] = cfg.WHITE ^ cfg.ROOK
        self.board[63] = cfg.BLACK ^ cfg.QUEEN
        self.board[7] = cfg.WHITE ^ cfg.BISHOP
    

    # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
    def setup_from_fen(self, fen) -> None:
        board = [cfg.NONE] * 64
        for i, row in enumerate(fen.split(' ')[0].split('/')[::-1]):
            for j, c in enumerate(row):
                if c.isdigit():
                    for k in range(int(c)):
                        board[i*8+j+k] = cfg.NONE
                else:
                    board[i*8+j] = get_piece_from_char(c)
        self.board = board

    
    def move_idx(self, start: int, end: int):
        # Move the piece
        self.board[end] = self.board[start]
        self.board[start] = cfg.NONE
    

    def is_legal(self, start: int, end: int) -> bool:
        pass


# Run the game
def main():
    b = Board()
    b.setup_from_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    game = Display(cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT, cfg.SCREEN_TITLE,
                   square_size=cfg.SQUARE_SIZE, padding=cfg.PADDING, board=b)
    game.setup()
    game.update_display_board()
    arcade.run()


if __name__ == "__main__":
    main()