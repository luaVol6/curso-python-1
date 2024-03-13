import pygame
print('Escute agora satellite - Harry styles')
pygame.init()
pygame.mixer.music.load('satellite.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()