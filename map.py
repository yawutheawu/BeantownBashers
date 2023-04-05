import pygame as pg
import random as rand

_ = False
map_x = rand.randrange(10,25)
map_y = rand.randrange(10,25)

def isPath(arr):
    # directions
    Dir = [ [0, 1], [0, -1], [1, 0], [-1, 0]]
    # queue
    q = []
    # insert the top right corner.
    q.append((0, 0))
    # until queue is empty
    while(len(q) > 0) :
        p = q[0]
        q.pop(0)
        # mark as visited
        arr[p[0]][p[1]] = -1
        # destination is reached.
        if(p == (len(arr) - 1, len(arr[0]) - 1)) :
            return True 
        # check all four directions
        for i in range(4) :
            # using the direction array
            a = p[0] + Dir[i][0]
            b = p[1] + Dir[i][1]
            # not blocked and valid
            if(a >= 0 and b >= 0 and a < len(arr) and b < len(arr[0]) and arr[a][b] != -1) :           
                q.append((a, b))
    return False


pos_map = []
x = []
for i in range(6,map_y-1):
    x=[]
    for i in range(5,map_x):
        if i ==5 or i == map_x:
            x.append(4)
        else:
            randNum = rand.randrange(0,2)
            x.append(randNum)
    pos_map.append(x)

while not isPath(pos_map):
    pos_map = []
    x = []
    for i in range(6,map_y-1):
        x=[]
        for i in range(5,map_x):
            if i ==5 or i == map_x:
                x.append(4)
            else:
                randNum = rand.randrange(0,2)
                x.append(randNum)
        pos_map.append(x)

mini_map = []
for i in pos_map:
    x = []
    for j in i:
        if j == 0:
            x.append(_)
        elif j == 1:
            x.append(rand.randrange(0,6))
        else:
            x.append(j)
    mini_map.append(x)

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
