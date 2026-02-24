import json, os

class GameManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.games = []

    def load_games(self):
        if os.path.exists(self.file_path):
            with open(self.file_path,'r') as f:
                try:
                    self.games = json.load(f)
                except:
                    self.games = []
        else:
            self.games = []

    def add_game(self, name, path, cover_path=''):
        self.games.append({'name': name,'path': path,'cover_path':cover_path,'playtime':0,'favorite':False})
        self.save()

    def update_playtime(self, name, minutes):
        for g in self.games:
            if g['name'] == name:
                g['playtime'] += minutes
        self.save()

    def save(self):
        with open(self.file_path,'w') as f:
            json.dump(self.games,f,indent=4)
