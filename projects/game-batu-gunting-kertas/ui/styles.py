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
            border: 2px solid {COLORS['border']};
            padding: 15px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 12px;
            font-family: 'Arial';
        }}
        
        QPushButton:hover {{
            background-color: {COLORS['button_hover']};
            border-color: {COLORS['primary']};
        }}
        
        QPushButton:pressed {{
            background-color: {COLORS['primary']};
        }}
        
        QPushButton#choice_btn {{
            font-size: 32px;
            padding: 30px;
            min-width: 120px;
            max-width: 120px;
            min-height: 150px;
            max-height: 150px;
        }}
        
        QPushButton#choice_btn:hover {{
            transform: scale(1.05);
            background-color: {COLORS['button_hover']};
        }}
        
        QPushButton#reset_btn {{
            background-color: {COLORS['danger']};
            color: {COLORS['bg']};
            font-size: 14px;
            padding: 10px 20px;
        }}
        
        QPushButton#reset_btn:hover {{
            background-color: {COLORS['lose']};
        }}
        
        QLabel {{
            color: {COLORS['text']};
            font-size: 14px;
            font-family: 'Arial';
        }}
        
        QLabel#title {{
            font-size: 36px;
            font-weight: bold;
            color: {COLORS['primary']};
            letter-spacing: 3px;
        }}
        
        QLabel#score_title {{
            font-size: 18px;
            font-weight: bold;
            color: {COLORS['text_secondary']};
        }}
        
        QLabel#score_value {{
            font-size: 32px;
            font-weight: bold;
            color: {COLORS['primary']};
        }}
        
        QLabel#vs_label {{
            font-size: 24px;
            font-weight: bold;
            color: {COLORS['accent']};
        }}
        
        QLabel#choice_display {{
            font-size: 64px;
            background-color: {COLORS['surface']};
            border: 2px solid {COLORS['border']};
            border-radius: 20px;
            padding: 30px;
            min-width: 150px;
            min-height: 150px;
            alignment: center;
        }}
        
        QLabel#result_label {{
            font-size: 24px;
            font-weight: bold;
        }}
        
        QFrame {{
            background-color: {COLORS['surface']};
            border: 1px solid {COLORS['border']};
            border-radius: 15px;
        }}
    """