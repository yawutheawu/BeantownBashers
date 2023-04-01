import pygame
import time
import beatTimer
import beatMaps

#song is "fileName.mp3"
def playFile(song):
    pygame.mixer.init()
    map = beatMaps.getSong(song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    begin = int(time.time() * 1000)
    length = map[0][-1]
    final = begin + length
    index = 0
    for i in range(0, length):
        if(begin >= final):
            begin = int(time.time() * 1000)
            final = begin + length
            pygame.mixer.music.play()
        print(i)
        if i in map[0]:
            hit = beatTimer.inputBeat(map[1][0], (0.353*3))
            if(hit):
                hit = False
                time.sleep(3)
                pass;
            else:
                return False
            index += 1
    return True

x = playFile("reg_enemy.mp3")

