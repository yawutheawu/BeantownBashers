import pygame
import time
from mutagen.mp3 import MP3
import keyboard

#to play a song/sound that is not tied to the beats/rythm of the game, type in code: playSongNoBeatMap.play("file.mp3")

def play(name):
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
