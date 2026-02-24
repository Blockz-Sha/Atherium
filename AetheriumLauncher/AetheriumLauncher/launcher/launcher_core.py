import os

def launch_game(path):
    if os.path.exists(path):
        os.startfile(path)
    else:
        print(f'Game not found: {path}')
