import pygame
pygame.init()

pygame.mixer.music.load('desatocar.mp3')

pygame.mixer.music.play()
pygame.event.wait()
