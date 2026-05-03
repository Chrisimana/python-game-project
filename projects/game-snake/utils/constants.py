# Warna
COLORS = {
    'bg': '#1A1A1A',
    'board': '#2A2A2A',
    'snake_head': '#4CAF50',
    'snake_body': '#66BB6A',
    'food': '#FF5252',
    'text': '#E0E0E0',
    'title': '#FFFFFF',
    'button': '#3A3A3A',
    'button_hover': '#4A4A4A',
    'border': '#404040',
    'score': '#FFD54F'
}

# Ukuran
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700
BOARD_SIZE = 20
CELL_SIZE = 25
BOARD_WIDTH = BOARD_SIZE * CELL_SIZE
BOARD_HEIGHT = BOARD_SIZE * CELL_SIZE

# Game settings
INITIAL_SPEED = 150  # milliseconds
SPEED_INCREMENT = 5
MIN_SPEED = 50

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = {
    'up': UP,
    'down': DOWN,
    'left': LEFT,
    'right': RIGHT
}

OPPOSITE = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT
}