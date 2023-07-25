# Chess encoding methods
# No piece is 0, indexed from sprite sheet
pieces = { 'k': 1, 'q': 2, 'b': 3,
           'n': 4, 'r': 5, 'p': 6, }
pieces_inverse = {v: k for k, v in pieces.items()}

def get_sprite_from_piece(p: int) -> int:
    """Returns the sprite index from a piece encoding"""
    # White pieces are 0-5, black pieces are 6-11
    index = get_char_from_piece(p).lower()
    color_offset = 6 * (not color_of(p)) # color_of returns 1 for white and 0 for black
    return pieces[index] + color_offset - 1

def get_piece_from_char(c: str) -> int:
    """Returns the piece encoding from a character"""
    color = 8 if c.isupper() else 16;
    return color ^ pieces[c.lower()]


def get_char_from_piece(p: int) -> str:
    """Returns the character of a piece from a piece encoding"""
    if p == 0:
        return '_' # No piece
    is_white = p & 8
    c = pieces_inverse[p & 7]
    return c.upper() if is_white else c


def color_of(p: int) -> int:
    """Returns the color of a piece as 1 as white or 0 as black from a piece encoding"""
    return 1 if p & 8 else 0


# Coordinate methods
def xy_to_flat(x: int, y: int) -> int:
    """Converts x, y coordinates to a flat index 0-63"""
    return y * 8 + x


def flat_to_xy(i: int) -> tuple:
    """Converts a flat index 0-63 to x, y coordinates"""
    return i % 8, i // 8


# Math methods
def remap(x, a, b, c, d):
    """
    Remaps x from range [a, b] to range [c, d]
    assumes x is in range [a, b]
    """
    return c + (x - a) * (d - c) / (b - a)


# Color methods
def color_mul(_a, _b):
    """
    Returns a color by the multiply blend mode formula
    f(a, b) = a * b
    param: a: three element tuple of (r, g, b) (int)
    param: b: three element tuple of (r, g, b) (int)
    """
    a = [x / 255 for x in _a]
    b = [x / 255 for x in _b]
    c = [a[i] * b[i] for i in range(3)]
    return tuple([int(x * 255) for x in c])


def color_screen(_a, _b):
    """
    Returns a color by the screen blend mode formula
    f(a, b) = 1 - (1 - a) * (1 - b)
    param: a: three element tuple of (r, g, b) (int)
    param: b: three element tuple of (r, g, b) (int)
    """
    a = [x / 255 for x in _a]
    b = [x / 255 for x in _b]
    c = [1 - (1 - a[i]) * (1 - b[i]) for i in range(3)]
    return tuple([int(x * 255) for x in c])


def color_add(a, b):
    return tuple([min(a[i] + b[i], 255) for i in range(3)])