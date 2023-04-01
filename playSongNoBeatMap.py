import pygame
import time
from mutagen.mp3 import MP3
import keyboard

def play(name):
    pygame.mixer.init()
    pygame.mixer.music.load(name)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
