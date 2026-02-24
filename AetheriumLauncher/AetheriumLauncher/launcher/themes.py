class ThemeManager:
    def __init__(self, theme_name='dark'):
        if theme_name=='dark':
            self.item_bg='#1e1e1e'
            self.text_color='#ffffff'
        else:
            self.item_bg='#ffffff'
            self.text_color='#000000'
