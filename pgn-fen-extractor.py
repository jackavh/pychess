# rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
import pickle
import chess.pgn
import numpy as np
from tqdm import tqdm
from datetime import datetime
from collections import defaultdict


GITHUB_PGNS = "assets/lichess_db_standard_rated_2013-01.pgn"
LOCAL_PGNS  = "local/lichess_db_standard_rated_2015-08.pgn"


rng = np.random.default_rng()
pgn = open(LOCAL_PGNS)
positions = defaultdict(list)
fen_positions = []


for i in tqdm(range(150_000)):
    game = chess.pgn.read_game(pgn)
    moves = game.mainline_moves()
    board = game.board()

    # Random even move count and an upper bound
    move_limit = rng.integers(8, 16) << 1
    at_least_x_moves = move_limit + 20
    min_pieces = 8

    # Plays out the game to move_limit
    # then records the fen string
    fen = ''
    moves_played = 0
    for move in moves:
        board.push(move)
        moves_played += 1
        if moves_played == move_limit:
            fen = board.fen()

    # Qualifications to record a fen
    pieces_left = len([c for c in fen if c in 'RNBQrnbq'])
    enough_pieces = pieces_left >= min_pieces
    enough_moves = moves_played > at_least_x_moves

    if enough_pieces and enough_moves:
        # Just records the fenstrings
        fen_positions.append(fen)
        # Records in a dict with opening : fen position pairs
        positions[game.headers['Opening']].append(fen)

# Write to file
print('Writing to file...')
time = datetime.now().strftime('%Y-%m-%d_%H.%M')
with open(f'local/opening_positions_{time}.pkl', 'wb') as file:
    pickle.dump(positions, file)

with open(f'local/fen_positions_{time}.txt', 'w') as file:
    for fen in fen_positions:
        file.write(f'{fen}\n')
print('Task complete!')