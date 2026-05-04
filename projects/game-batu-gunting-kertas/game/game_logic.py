import random
from utils.constants import OPTIONS, RULES, STATUS_WIN, STATUS_LOSE, STATUS_DRAW

class GameLogic:
    def __init__(self):
        self.player_score = 0
        self.ai_score = 0
        self.draw_count = 0
        self.rounds_played = 0
        self.last_player_choice = None
        self.last_ai_choice = None
        self.last_result = None
    
    # Fungsi untuk memainkan satu ronde
    def play_round(self, player_choice):
        if player_choice not in OPTIONS:
            return None
        
        # AI memilih secara acak
        ai_choice = random.choice(list(OPTIONS.keys()))
        
        # Tentukan pemenang
        result = self.determine_winner(player_choice, ai_choice)
        
        # Update skor
        if result == STATUS_WIN:
            self.player_score += 1
        elif result == STATUS_LOSE:
            self.ai_score += 1
        else:
            self.draw_count += 1
        
        self.rounds_played += 1
        self.last_player_choice = player_choice
        self.last_ai_choice = ai_choice
        self.last_result = result
        
        return {
            'player_choice': player_choice,
            'ai_choice': ai_choice,
            'result': result,
            'player_score': self.player_score,
            'ai_score': self.ai_score
        }
    
    # Fungsi untuk menentukan pemenang berdasarkan pilihan pemain dan AI
    def determine_winner(self, player, ai):
        if player == ai:
            return STATUS_DRAW
        elif RULES[player] == ai:
            return STATUS_WIN
        else:
            return STATUS_LOSE
    
    # Fungsi untuk mereset permainan
    def reset_game(self):
        self.player_score = 0
        self.ai_score = 0
        self.draw_count = 0
        self.rounds_played = 0
        self.last_player_choice = None
        self.last_ai_choice = None
        self.last_result = None
    
    # Fungsi untuk mendapatkan statistik permainan
    def get_statistics(self):
        return {
            'player_score': self.player_score,
            'ai_score': self.ai_score,
            'draw_count': self.draw_count,
            'rounds_played': self.rounds_played
        }
    
    # Fungsi untuk mendapatkan pemenang keseluruhan
    def get_winner(self):
        if self.player_score > self.ai_score:
            return 'pemain'
        elif self.ai_score > self.player_score:
            return 'AI'
        else:
            return None if self.rounds_played == 0 else 'seri'