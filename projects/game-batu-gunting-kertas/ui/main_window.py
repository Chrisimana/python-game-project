import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFrame, QGridLayout)
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QFont
from game.game_logic import GameLogic
from ui.styles import apply_styles
from utils.constants import (COLORS, OPTIONS, OPTIONS_EMOJI, STATUS_WIN, 
                           STATUS_LOSE, STATUS_DRAW, WINDOW_WIDTH, WINDOW_HEIGHT)

class SuitWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.game = GameLogic()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Batu Gunting Kertas')
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(apply_styles())
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 20, 30, 20)
        
        # Title
        title_label = QLabel('BATU GUNTING KERTAS')
        title_label.setObjectName('title')
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Score board
        score_frame = QFrame()
        score_layout = QHBoxLayout(score_frame)
        score_layout.setSpacing(50)
        
        # Player score
        player_widget = QWidget()
        player_layout = QVBoxLayout(player_widget)
        player_title = QLabel('ANDA')
        player_title.setObjectName('score_title')
        player_title.setAlignment(Qt.AlignCenter)
        self.player_score_label = QLabel('0')
        self.player_score_label.setObjectName('score_value')
        self.player_score_label.setAlignment(Qt.AlignCenter)
        player_layout.addWidget(player_title)
        player_layout.addWidget(self.player_score_label)
        
        # VS label
        vs_label = QLabel('VS')
        vs_label.setObjectName('vs_label')
        vs_label.setAlignment(Qt.AlignCenter)
        
        # AI score
        ai_widget = QWidget()
        ai_layout = QVBoxLayout(ai_widget)
        ai_title = QLabel('AI')
        ai_title.setObjectName('score_title')
        ai_title.setAlignment(Qt.AlignCenter)
        self.ai_score_label = QLabel('0')
        self.ai_score_label.setObjectName('score_value')
        self.ai_score_label.setAlignment(Qt.AlignCenter)
        ai_layout.addWidget(ai_title)
        ai_layout.addWidget(self.ai_score_label)
        
        score_layout.addWidget(player_widget)
        score_layout.addWidget(vs_label)
        score_layout.addWidget(ai_widget)
        
        main_layout.addWidget(score_frame)
        
        # Display pilihan
        choice_frame = QFrame()
        choice_layout = QHBoxLayout(choice_frame)
        choice_layout.setSpacing(30)
        
        # Player choice
        player_choice_widget = QWidget()
        player_choice_layout = QVBoxLayout(player_choice_widget)
        player_choice_label = QLabel('Pilihan Anda')
        player_choice_label.setObjectName('score_title')
        player_choice_label.setAlignment(Qt.AlignCenter)
        self.player_choice_display = QLabel('❓')
        self.player_choice_display.setObjectName('choice_display')
        self.player_choice_display.setAlignment(Qt.AlignCenter)
        player_choice_layout.addWidget(player_choice_label)
        player_choice_layout.addWidget(self.player_choice_display)
        
        # VS icon
        vs_icon = QLabel('⚔️')
        vs_icon.setObjectName('vs_label')
        vs_icon.setAlignment(Qt.AlignCenter)
        vs_icon.setStyleSheet(f"font-size: 48px;")
        
        # AI choice
        ai_choice_widget = QWidget()
        ai_choice_layout = QVBoxLayout(ai_choice_widget)
        ai_choice_label = QLabel('Pilihan AI')
        ai_choice_label.setObjectName('score_title')
        ai_choice_label.setAlignment(Qt.AlignCenter)
        self.ai_choice_display = QLabel('❓')
        self.ai_choice_display.setObjectName('choice_display')
        self.ai_choice_display.setAlignment(Qt.AlignCenter)
        ai_choice_layout.addWidget(ai_choice_label)
        ai_choice_layout.addWidget(self.ai_choice_display)
        
        choice_layout.addWidget(player_choice_widget)
        choice_layout.addWidget(vs_icon)
        choice_layout.addWidget(ai_choice_widget)
        
        main_layout.addWidget(choice_frame)
        
        # Result label
        self.result_label = QLabel('Pilih batu, gunting, atau kertas')
        self.result_label.setObjectName('result_label')
        self.result_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.result_label)
        
        # Choice buttons
        buttons_frame = QFrame()
        buttons_layout = QHBoxLayout(buttons_frame)
        buttons_layout.setSpacing(100)
        buttons_layout.setAlignment(Qt.AlignCenter)
        
        # Batu button
        self.batu_btn = QPushButton(f'{OPTIONS_EMOJI["batu"]}\nBatu')
        self.batu_btn.setObjectName('choice_btn')
        self.batu_btn.clicked.connect(lambda: self.play_round('batu'))
        buttons_layout.addWidget(self.batu_btn)
        
        # Gunting button
        self.gunting_btn = QPushButton(f'{OPTIONS_EMOJI["gunting"]}\nGunting')
        self.gunting_btn.setObjectName('choice_btn')
        self.gunting_btn.clicked.connect(lambda: self.play_round('gunting'))
        buttons_layout.addWidget(self.gunting_btn)
        
        # Kertas button
        self.kertas_btn = QPushButton(f'{OPTIONS_EMOJI["kertas"]}\nKertas')
        self.kertas_btn.setObjectName('choice_btn')
        self.kertas_btn.clicked.connect(lambda: self.play_round('kertas'))
        buttons_layout.addWidget(self.kertas_btn)
        
        main_layout.addWidget(buttons_frame)
        
        # Reset button and statistics
        bottom_frame = QFrame()
        bottom_layout = QHBoxLayout(bottom_frame)
        
        # Statistics
        stats_widget = QWidget()
        stats_layout = QVBoxLayout(stats_widget)
        stats_layout.setSpacing(5)
        
        self.draw_label = QLabel('Seri: 0')
        self.draw_label.setObjectName('score_title')
        self.rounds_label = QLabel('Total ronde: 0')
        self.rounds_label.setObjectName('score_title')
        
        stats_layout.addWidget(self.draw_label)
        stats_layout.addWidget(self.rounds_label)
        
        # Reset button
        self.reset_btn = QPushButton('Reset Game')
        self.reset_btn.setObjectName('reset_btn')
        self.reset_btn.clicked.connect(self.reset_game)
        
        bottom_layout.addWidget(stats_widget)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.reset_btn)
        
        main_layout.addWidget(bottom_frame)
        
        # Info label
        info_label = QLabel('Klik tombol di atas untuk bermain | Skor tertinggi menentukan pemenang')
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setStyleSheet(f"color: {COLORS['text_secondary']}; font-size: 11px; padding: 10px;")
        main_layout.addWidget(info_label)
    
    # Memainkan satu ronde permainan
    def play_round(self, player_choice):
        result = self.game.play_round(player_choice)
        
        if result:
            # Update display choices
            self.player_choice_display.setText(OPTIONS_EMOJI[result['player_choice']])
            self.ai_choice_display.setText(OPTIONS_EMOJI[result['ai_choice']])
            
            # Update scores
            self.update_scores()
            
            # Update result message
            if result['result'] == STATUS_WIN:
                self.result_label.setText('ANDA MENANG!')
                self.result_label.setStyleSheet(f"color: {COLORS['win']}; font-size: 24px; font-weight: bold;")
                self.animate_win()
            elif result['result'] == STATUS_LOSE:
                self.result_label.setText('AI MENANG!')
                self.result_label.setStyleSheet(f"color: {COLORS['lose']}; font-size: 24px; font-weight: bold;")
                self.animate_lose()
            else:
                self.result_label.setText('SERI!')
                self.result_label.setStyleSheet(f"color: {COLORS['draw']}; font-size: 24px; font-weight: bold;")
                self.animate_draw()
            
            # Update statistics
            stats = self.game.get_statistics()
            self.draw_label.setText(f'Seri: {stats["draw_count"]}')
            self.rounds_label.setText(f'Total ronde: {stats["rounds_played"]}')
    
    # Memperbarui tampilan skor
    def update_scores(self):
        stats = self.game.get_statistics()
        self.player_score_label.setText(str(stats['player_score']))
        self.ai_score_label.setText(str(stats['ai_score']))
        
        # Animasi perubahan skor
        self.animate_score_change()
    
    # Reset permainan ke kondisi awal
    def reset_game(self):
        self.game.reset_game()
        
        # Reset display
        self.player_choice_display.setText('❓')
        self.ai_choice_display.setText('❓')
        self.player_score_label.setText('0')
        self.ai_score_label.setText('0')
        self.draw_label.setText('Seri: 0')
        self.rounds_label.setText('Total ronde: 0')
        self.result_label.setText('Game direset! Pilih batu, gunting, atau kertas')
        self.result_label.setStyleSheet(f"color: {COLORS['text']}; font-size: 24px; font-weight: bold;")
        
        # Animasi reset
        self.animate_reset()
    
    # Animasi saat menang
    def animate_win(self):
        self.player_score_label.setStyleSheet(f"color: {COLORS['win']}; font-size: 32px; font-weight: bold;")
        self.result_label.setStyleSheet(f"color: {COLORS['win']}; font-size: 24px; font-weight: bold;")
        
        # Reset warna setelah 1 detik
        from PyQt5.QtCore import QTimer
        QTimer.singleShot(1000, lambda: self.player_score_label.setStyleSheet(f"color: {COLORS['primary']}; font-size: 32px; font-weight: bold;"))
    
    # Animasi saat kalah
    def animate_lose(self):
        self.ai_score_label.setStyleSheet(f"color: {COLORS['lose']}; font-size: 32px; font-weight: bold;")
        self.result_label.setStyleSheet(f"color: {COLORS['lose']}; font-size: 24px; font-weight: bold;")
        
        from PyQt5.QtCore import QTimer
        QTimer.singleShot(1000, lambda: self.ai_score_label.setStyleSheet(f"color: {COLORS['primary']}; font-size: 32px; font-weight: bold;"))
    
    # Animasi saat seri
    def animate_draw(self):
        self.result_label.setStyleSheet(f"color: {COLORS['draw']}; font-size: 24px; font-weight: bold;")
    
    # Animasi perubahan skor 
    def animate_score_change(self):
        # Efek scaling sederhana
        self.player_score_label.setStyleSheet(f"color: {COLORS['primary']}; font-size: 36px; font-weight: bold;")
        self.ai_score_label.setStyleSheet(f"color: {COLORS['primary']}; font-size: 36px; font-weight: bold;")
        
        from PyQt5.QtCore import QTimer
        QTimer.singleShot(200, lambda: self.player_score_label.setStyleSheet(f"color: {COLORS['primary']}; font-size: 32px; font-weight: bold;"))
        QTimer.singleShot(200, lambda: self.ai_score_label.setStyleSheet(f"color: {COLORS['primary']}; font-size: 32px; font-weight: bold;"))
    
    # Animasi saat reset
    def animate_reset(self):
        self.result_label.setStyleSheet(f"color: {COLORS['accent']}; font-size: 24px; font-weight: bold;")
        
        from PyQt5.QtCore import QTimer
        QTimer.singleShot(1000, lambda: self.result_label.setStyleSheet(f"color: {COLORS['text']}; font-size: 24px; font-weight: bold;"))

    # Shortcut keyboard untuk pilihan dan reset
    def keyPressEvent(self, event):
        key = event.key()
        
        # Shortcut untuk pilihan
        if key == Qt.Key_B or key == Qt.Key_1:
            self.play_round('batu')
        elif key == Qt.Key_G or key == Qt.Key_2:
            self.play_round('gunting')
        elif key == Qt.Key_K or key == Qt.Key_3:
            self.play_round('kertas')
        elif key == Qt.Key_R:
            self.reset_game()