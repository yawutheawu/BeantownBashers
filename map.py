import pygame as pg
import random as rand

_ = False
mini_map = [
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [4,4,_,_,_,_,_,_,_,_,_,_,_,_,4,4],
    [4,_,_,rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),_,_,_,_,_,_,_,4],
    [4,_,_,_,_,_,rand.randrange(0,5),_,_,rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),_,_,_,4],
    [4,_,_,_,_,_,_,_,_,_,_,_,_,_,_,4],
    [4,_,rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),_,_,rand.randrange(0,5),_,_,_,_,_,4],
    [4,_,_,rand.randrange(0,5),_,_,_,_,_,rand.randrange(0,5),_,_,_,_,_,4],
    [4,4,_,rand.randrange(0,5),_,_,_,_,_,rand.randrange(0,5),_,_,_,_,4,4],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]