def xy_to_flat(x, y):
    return y * 8 + x


def flat_to_xy(i):
    return i % 8, i // 8


def remap(x, a, b, c, d):
    """
    Remaps x from range [a, b] to range [c, d]
    assumes x is in range [a, b]
    """
    return c + (x - a) * (d - c) / (b - a)


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