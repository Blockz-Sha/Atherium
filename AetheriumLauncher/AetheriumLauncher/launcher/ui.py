import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QScrollArea, QGridLayout
from PySide6.QtGui import QPixmap
from launcher.game_manager import GameManager
from launcher.launcher_core import launch_game
from launcher.themes import ThemeManager

class LauncherUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Aetherium Launcher')
        self.setGeometry(200,200,800,600)

        self.theme=ThemeManager('dark')
        self.game_manager=GameManager('data/games.json')
        self.game_manager.load_games()

        self.layout=QVBoxLayout()
        self.setLayout(self.layout)

        self.search_bar=QLineEdit()
        self.search_bar.setPlaceholderText('Search games...')
        self.search_bar.textChanged.connect(self.populate_games)
        self.layout.addWidget(self.search_bar)

        self.scroll=QScrollArea()
        self.scroll_widget=QWidget()
        self.grid=QGridLayout()
        self.scroll_widget.setLayout(self.grid)
        self.scroll.setWidget(self.scroll_widget)
        self.scroll.setWidgetResizable(True)
        self.layout.addWidget(self.scroll)

        self.populate_games()

    def populate_games(self):
        for i in reversed(range(self.grid.count())):
            w=self.grid.itemAt(i).widget()
            if w: w.setParent(None)
        games=self.filter_games()
        for i, g in enumerate(games):
            w=self.create_grid_item(g)
            self.grid.addWidget(w,i//3,i%3)

    def filter_games(self):
        t=self.search_bar.text().lower()
        return [g for g in self.game_manager.games if t in g['name'].lower()]

    def create_grid_item(self, game):
        w=QWidget()
        l=QVBoxLayout()
        w.setLayout(l)
        pix=QPixmap(game['cover_path']) if game['cover_path'] and os.path.exists(game['cover_path']) else QPixmap()
        img=QLabel()
        img.setPixmap(pix.scaled(150,150))
        l.addWidget(img)
        text=QLabel(f\"{game['name']}\\nPlaytime: {game['playtime']}m\")
        text.setStyleSheet(f'color:{self.theme.text_color}; background-color:{self.theme.item_bg}')
        l.addWidget(text)
        btn=QPushButton('Play')
        btn.clicked.connect(lambda _,p=game['path']: launch_game(p))
        l.addWidget(btn)
        return w
