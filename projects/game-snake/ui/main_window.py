import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFrame)
from PyQt5.QtCore import Qt, QTimer, QRect
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from game.game_logic import GameLogic
from ui.styles import apply_styles
from utils.constants import (BOARD_SIZE, CELL_SIZE, BOARD_WIDTH, BOARD_HEIGHT, MIN_SPEED, SPEED_INCREMENT,
                             WINDOW_WIDTH, WINDOW_HEIGHT, COLORS, INITIAL_SPEED)

class GameCanvas(QWidget):
    def __init__(self, game_logic):
        super().__init__()
        self.game_logic = game_logic
        self.setFixedSize(BOARD_WIDTH, BOARD_HEIGHT)
        self.setStyleSheet(f"background-color: {COLORS['board']}; border: 2px solid {COLORS['border']}; border-radius: 10px;")
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Gambar grid
        pen = QPen(QColor(COLORS['border']))
        pen.setWidth(1)
        painter.setPen(pen)
        
        for i in range(BOARD_SIZE):
            painter.drawLine(0, i * CELL_SIZE, BOARD_WIDTH, i * CELL_SIZE)
            painter.drawLine(i * CELL_SIZE, 0, i * CELL_SIZE, BOARD_HEIGHT)
        
        # Gambar makanan
        food_pos = self.game_logic.food.get_position()
        painter.setBrush(QBrush(QColor(COLORS['food'])))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(food_pos[0] * CELL_SIZE + 2, 
                           food_pos[1] * CELL_SIZE + 2,
                           CELL_SIZE - 4, CELL_SIZE - 4)
        
        # Gambar ular
        snake_body = self.game_logic.snake.get_body()
        for i, segment in enumerate(snake_body):
            x = segment[0] * CELL_SIZE
            y = segment[1] * CELL_SIZE
            
            if i == 0:  # Kepala
                painter.setBrush(QBrush(QColor(COLORS['snake_head'])))
                painter.drawRoundedRect(x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4, 5, 5)
                
                # Mata ular
                painter.setBrush(QBrush(QColor(COLORS['bg'])))
                head_dir = self.game_logic.snake.direction
                if head_dir == (1, 0):  # Kanan
                    painter.drawEllipse(x + CELL_SIZE - 8, y + 6, 3, 3)
                    painter.drawEllipse(x + CELL_SIZE - 8, y + CELL_SIZE - 9, 3, 3)
                elif head_dir == (-1, 0):  # Kiri
                    painter.drawEllipse(x + 5, y + 6, 3, 3)
                    painter.drawEllipse(x + 5, y + CELL_SIZE - 9, 3, 3)
                elif head_dir == (0, -1):  # Atas
                    painter.drawEllipse(x + 6, y + 5, 3, 3)
                    painter.drawEllipse(x + CELL_SIZE - 9, y + 5, 3, 3)
                else:  # Bawah
                    painter.drawEllipse(x + 6, y + CELL_SIZE - 8, 3, 3)
                    painter.drawEllipse(x + CELL_SIZE - 9, y + CELL_SIZE - 8, 3, 3)
            else:  # Badan
                painter.setBrush(QBrush(QColor(COLORS['snake_body'])))
                painter.drawRoundedRect(x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4, 5, 5)

class SnakeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game_logic = GameLogic()
        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.speed = INITIAL_SPEED
        self.init_ui()
        self.start_game()
    
    def init_ui(self):
        self.setWindowTitle('Snake Game')
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(apply_styles())
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(15)
        
        # Title
        title_label = QLabel('SNAKE GAME')
        title_label.setObjectName('title')
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Score panel
        score_layout = QHBoxLayout()
        score_layout.addStretch()
        self.score_label = QLabel('Skor: 0')
        self.score_label.setObjectName('score_label')
        score_layout.addWidget(self.score_label)
        score_layout.addStretch()
        main_layout.addLayout(score_layout)
        
        # Game canvas
        self.game_canvas = GameCanvas(self.game_logic)
        main_layout.addWidget(self.game_canvas, alignment=Qt.AlignCenter)
        
        # Control buttons
        control_layout = QHBoxLayout()
        
        self.start_btn = QPushButton('Mulai')
        self.start_btn.clicked.connect(self.start_game)
        control_layout.addWidget(self.start_btn)
        
        self.pause_btn = QPushButton('Jeda')
        self.pause_btn.clicked.connect(self.pause_game)
        self.pause_btn.setEnabled(False)
        control_layout.addWidget(self.pause_btn)
        
        self.reset_btn = QPushButton('Reset')
        self.reset_btn.clicked.connect(self.reset_game)
        control_layout.addWidget(self.reset_btn)
        
        main_layout.addLayout(control_layout)
        
        # Info text
        info_label = QLabel('Gunakan tombol panah (↑ ↓ ← →) untuk menggerakkan ular')
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setStyleSheet(f"color: {COLORS['border']}; font-size: 12px;")
        main_layout.addWidget(info_label)
        
        # Game over overlay (hidden by default)
        self.game_over_label = QLabel('GAME OVER')
        self.game_over_label.setObjectName('game_over_label')
        self.game_over_label.setAlignment(Qt.AlignCenter)
        self.game_over_label.hide()
        
        # Position overlay in center of canvas
        overlay_container = QWidget()
        overlay_layout = QVBoxLayout(overlay_container)
        overlay_layout.addWidget(self.game_over_label)
        overlay_layout.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(overlay_container)
        
        # Set focus to window for keyboard input
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()
    
    def start_game(self):
        if self.game_logic.is_game_over():
            self.game_logic.reset()
            self.game_canvas.update()
            self.update_score()
        
        if not self.timer.isActive():
            self.timer.start(self.speed)
            self.start_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)
            self.game_over_label.hide()
            self.setFocus()
    
    def pause_game(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pause_btn.setText('Lanjut')
        else:
            self.timer.start(self.speed)
            self.pause_btn.setText('Jeda')
    
    def reset_game(self):
        self.timer.stop()
        self.game_logic.reset()
        self.game_canvas.update()
        self.update_score()
        self.speed = INITIAL_SPEED
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.pause_btn.setText('Jeda')
        self.game_over_label.hide()
    
    def game_loop(self):
        if self.game_logic.update():
            self.game_canvas.update()
            self.update_score()
            
            # Speed up based on score
            new_speed = max(INITIAL_SPEED - (self.game_logic.get_score() // 10) * SPEED_INCREMENT, MIN_SPEED)
            if new_speed != self.speed:
                self.speed = new_speed
                if self.timer.isActive():
                    self.timer.stop()
                    self.timer.start(self.speed)
        else:
            self.game_over()
    
    def update_score(self):
        self.score_label.setText(f'Skor: {self.game_logic.get_score()}')
    
    def game_over(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.game_over_label.setText(f'GAME OVER!\nSkor Akhir: {self.game_logic.get_score()}')
        self.game_over_label.show()
    
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.game_logic.change_direction((0, -1))
        elif key == Qt.Key_Down:
            self.game_logic.change_direction((0, 1))
        elif key == Qt.Key_Left:
            self.game_logic.change_direction((-1, 0))
        elif key == Qt.Key_Right:
            self.game_logic.change_direction((1, 0))
        elif key == Qt.Key_Space:
            if self.timer.isActive():
                self.pause_game()
            elif not self.game_logic.is_game_over():
                self.start_game()
        elif key == Qt.Key_R:
            self.reset_game()