import pygame as pg
import sys
from settings import *

class Game:
    def __init(selfself):
        pg.init()
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()

    def new_game(self):
        pass

    def draw(self):
        self.screen.fill('black')

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()