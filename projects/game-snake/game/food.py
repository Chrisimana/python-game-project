import random
from utils.constants import BOARD_SIZE

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.respawn([])
    
    def respawn(self, snake_body):
        while True:
            x = random.randint(0, BOARD_SIZE - 1)
            y = random.randint(0, BOARD_SIZE - 1)
            if (x, y) not in snake_body:
                self.position = (x, y)
                break
    
    def get_position(self):
        return self.position