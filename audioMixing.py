import pygame
import time
import beatTimer
import beatMaps

global_time = 0

def getGlobalTime():
    return global_time

#song is "fileName.mp3"
#when you want to play music in sync to shooting beans type in code when you want to do that action: audioMixing.playFile("name.mp3"))

def playFile(song):
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    map = beatMaps.getSong(song)
    begin = int(time.time() * 1000)
    length = map[0][-1]
    final = begin + length
    index = 0
    global_time = int(time.time() * 1000)
    for i in range(0, length):
        global_time = int(time.time() * 1000)
        if(begin >= final):
            begin = int(time.time() * 1000)
            final = begin + length
            pygame.mixer.music.play()
            global_time = int(time.time() * 1000)
        print(i)
        if i in map[0]:
            hit = beatTimer.inputBeat(map[1][0], (0.353*3))
            global_time = int(time.time() * 1000)
            if(hit):
                hit = False
                time.sleep(3)
                pass;
            else:
                return False
            index += 1
    return True

