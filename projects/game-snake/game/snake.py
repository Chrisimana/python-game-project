from utils.constants import BOARD_SIZE, CELL_SIZE

class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        # Posisi awal ular di tengah
        start_x = BOARD_SIZE // 2
        start_y = BOARD_SIZE // 2
        self.body = [(start_x, start_y)]
        self.direction = (1, 0)  # Awal ke kanan
        self.grow_flag = False
    
    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        
        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False
    
    def grow(self):
        self.grow_flag = True
    
    def check_collision(self):
        head = self.body[0]
        
        # Tabrakan dengan dinding
        if (head[0] < 0 or head[0] >= BOARD_SIZE or 
            head[1] < 0 or head[1] >= BOARD_SIZE):
            return True
        
        # Tabrakan dengan tubuh sendiri
        if head in self.body[1:]:
            return True
        
        return False
    
    def set_direction(self, new_direction):
        # Mencegah ular berbalik arah
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
    
    def get_head(self):
        return self.body[0]
    
    def get_body(self):
        return self.body