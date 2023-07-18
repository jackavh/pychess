import arcade
from helper import *


HIGHLIGHT_COLOR = (0xFF, 0xa1, 0xa1)
WHITE_COLOR = (0xEF, 0xD9, 0xB5)
BLACK_COLOR = (0xb4, 0x88, 0x63)
BACKGROUND  = (0x29, 0x27, 0x21)


class Display(arcade.Window):

    def __init__(self, width, height, title, square_size=None, padding=None):
        self.display_size = (width, height)
        self.square_size = 64 if square_size is None else square_size
        self.padding = 0 if padding is None else padding
        self.highlights = None
        self.hover_square = None
        
        super().__init__(width, height, title)
        arcade.set_background_color(BACKGROUND)


    def on_draw(self):
        self.clear()

        # Draw the game squares
        for x in range(8):
            for y in range(8):
                # Manage highlighting
                highlighted = (x % self.square_size, y % self.square_size) in self.highlights
                col = WHITE_COLOR if (x % 2) ^ (y % 2) else BLACK_COLOR
                if highlighted:
                    col = color_mul(HIGHLIGHT_COLOR, col)
                
                # Highlight the hover square
                if self.hover_square == (x, y):
                    col = color_mul(HIGHLIGHT_COLOR, col)
                    
                # Draw the square
                arcade.draw_xywh_rectangle_filled(x*self.square_size + self.padding/2,
                                                  y*self.square_size + self.padding/2,
                                                  self.square_size,
                                                  self.square_size,
                                                  col)
        
        # DEBUG: write the hover square to the screen
        debug_str = f'Hover square: {self.hover_square}\nHighlighted: {self.highlights}'
        arcade.draw_text(debug_str, 16, self.display_size[1] - 32, arcade.color.BLACK, 16,
                         multiline=True, width=self.display_size[0] - 32)

    
    def setup(self):
        self.highlights = set()


    def update(self, delta_time):
        pass


    def on_key_press(self, key, modifiers):
        pass


    def on_key_release(self, key, modifiers):
        pass


    def on_mouse_motion(self, x, y, delta_x, delta_y):
        # Handle hover square
        in_left = x > self.padding/2
        in_right = x < self.square_size*8 + self.padding/2
        in_top = y < self.square_size*8 + self.padding/2
        in_bottom = y > self.padding/2
        x_in_bounds = in_left and in_right
        y_in_bounds = in_top and in_bottom

        # Catch out of bounds
        if not x_in_bounds and not y_in_bounds:
            self.hover_square = None
            return
        # Get board coordinates

        hx = int((x - self.padding/2) // self.square_size)
        hy = int((y - self.padding/2) // self.square_size)
        # Update the hover square

        self.hover_square = (hx, hy)
    
        



    def on_mouse_press(self, x, y, button, modifiers):
        pass


    def on_mouse_release(self, x, y, button, modifiers):
        pass


    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass


    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass