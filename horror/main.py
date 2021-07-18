import pygame # you need to install this first
from time import sleep
pygame.init()
window= pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('audio.wav')
pygame.mixer.music.play()
sleep(4)
image = pygame.image.load('w.jpg')
window.blit(image,(0,0))
pygame.display.update()
sleep(3)

