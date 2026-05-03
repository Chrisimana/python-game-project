from game.snake import Snake
from game.food import Food
from utils.constants import BOARD_SIZE

class GameLogic:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.respawn_food()
    
    def respawn_food(self):
        self.food.respawn(self.snake.get_body())
    
    def update(self):
        if self.game_over:
            return False
        
        self.snake.move()
        
        # Cek tabrakan
        if self.snake.check_collision():
            self.game_over = True
            return False
        
        # Cek apakah makan makanan
        if self.snake.get_head() == self.food.get_position():
            self.snake.grow()
            self.score += 10
            self.respawn_food()
        
        return True
    
    def change_direction(self, direction):
        if not self.game_over:
            self.snake.set_direction(direction)
    
    def get_score(self):
        return self.score
    
    def is_game_over(self):
        return self.game_over
    
    def reset(self):
        self.snake.reset()
        self.score = 0
        self.game_over = False
        self.respawn_food()