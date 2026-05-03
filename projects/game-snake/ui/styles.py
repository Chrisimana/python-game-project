from utils.constants import COLORS

def apply_styles():
    return f"""
        QMainWindow {{
            background-color: {COLORS['bg']};
        }}
        
        QWidget {{
            background-color: transparent;
        }}
        
        QPushButton {{
            background-color: {COLORS['button']};
            color: {COLORS['text']};
            border: 1px solid {COLORS['border']};
            padding: 10px 20px;
            font-size: 14px;
            font-weight: bold;
            border-radius: 8px;
            font-family: 'Arial';
        }}
        
        QPushButton:hover {{
            background-color: {COLORS['button_hover']};
            border-color: {COLORS['text']};
        }}
        
        QPushButton:pressed {{
            background-color: {COLORS['border']};
        }}
        
        QLabel {{
            color: {COLORS['text']};
            font-size: 16px;
            font-family: 'Arial';
        }}
        
        QLabel#title {{
            font-size: 28px;
            font-weight: bold;
            color: {COLORS['title']};
            letter-spacing: 2px;
        }}
        
        QLabel#score_label {{
            font-size: 20px;
            font-weight: bold;
            color: {COLORS['score']};
        }}
        
        QLabel#game_over_label {{
            font-size: 24px;
            font-weight: bold;
            color: {COLORS['food']};
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
        }}
    """