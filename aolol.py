import pygame
from pygame.locals import *
from math import *
from os import remove
from subprocess import run, PIPE
from sys import exit
from time import sleep

pygame.init()

xrandr = run(['xrandr', '-q', '-d', ':0'], stdout=PIPE)
screen = xrandr.stdout.decode("utf-8").split('\n')[0]
WIDTH = int(screen.split()[7])
HEIGHT = int(screen.split()[9][:-1])

tmpbg = '/tmp/screen.png'
run(['scrot', tmpbg])

fgFrames=[
  "/usr/share/aolol/aol-frame-1.gif",
  "/usr/share/aolol/aol-frame-2.gif",
  "/usr/share/aolol/aol-frame-2.gif",
  "/usr/share/aolol/aol-frame-3.gif"
]
bgFrames=[
  "/tmp/bg-1.png",
  "/tmp/bg-2.png",
  "/tmp/bg-3.png",
  "/tmp/bg-4.png",
]
overlayFrames=[
  "/tmp/overlay-1.png",
  "/tmp/overlay-2.png",
  "/tmp/overlay-3.png",
  "/tmp/overlay-4.png",
]

run(['convert', tmpbg, '-scale', '5%', '-scale', '2000%', bgFrames[0]])
run(['convert', tmpbg, '-scale', '10%', '-scale', '1000%', bgFrames[1]])
run(['convert', tmpbg, '-scale', '20%', '-scale', '500%', bgFrames[2]])
run(['convert', tmpbg, '-scale', '50%', '-scale', '200%', bgFrames[3]])

remove(tmpbg)

for i in range(len(bgFrames)):
    run(['convert', bgFrames[i], fgFrames[i], '-gravity', 'center', '-composite', '-matte', overlayFrames[i]])

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

def showFrame(num):
    img = pygame.image.load(overlayFrames[num])
    windowSurface.blit(img, (0, 0))
    pygame.display.flip()

for frame in range(len(bgFrames)):
    events = pygame.event.get()
    for event in events:
        if event.type == KEYUP or event.type == MOUSEBUTTONUP:
            pygame.quit()
            exit()
    showFrame(frame)
    sleep(1)

pygame.quit()
exit()
