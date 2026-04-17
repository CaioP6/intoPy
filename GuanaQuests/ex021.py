import pygame # type: ignore

pygame.init()

pygame.mixer.music.load('C:\hahahah.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

'''Não funciona no VSCode, só no terminal nativo'''