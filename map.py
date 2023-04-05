import pygame as pg
import random as rand

_ = False
map_x = rand.randrange(10,25)
max_y = rand.randrange(10,25)
'''

    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [4,4,_,_,_,_,_,_,_,_,_,_,_,_,4,4],
    [4,_,_,rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),_,_,_,_,_,_,_,4],
    [4,_,_,_,_,_,rand.randrange(0,5),_,_,rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),_,_,_,4],
    [4,_,_,_,_,_,_,_,_,_,_,_,_,_,_,4],
    [4,_,rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),rand.randrange(0,5),_,_,rand.randrange(0,5),_,_,_,_,_,4],
    [4,_,_,rand.randrange(0,5),_,_,_,_,_,rand.randrange(0,5),_,_,_,_,_,4],
    [4,4,_,rand.randrange(0,5),_,_,_,_,_,rand.randrange(0,5),_,_,_,_,4,4],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],

'''


mini_map = []
x=[]
for i in range(0,map_x):
    x = x.append(4)
mini_map = mini_map.append(x)
for i in range(6,map_y-1):
    x=[]
    for i in range(5,map_x):
        if i ==5 or i == map_x:
            x = x.append(4)
        else:
            randNum = rand.randrange(0,6)
            if randNum == 6:
                x = x.append(_)
            else:
                x = x.append(randNum)
    mini_map = mini_map.append(x)
x=[]
for i in range(0,map_x):
    x = x.append(4)
mini_map = mini_map.append(x)
print(mini_map)


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
