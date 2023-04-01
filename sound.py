import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.mp3')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.mp3')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.mp3')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.mp3')
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.mp3')
        self.Reg = pg.mixer.music.load(self.path + 'Reg.mp3')
        self.Boss = pg.mixer.music.load(self.path + 'Boss.mp3')
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.4)