import pygame
from pygame.locals import *
from math import *
from os import remove
from subprocess import run, PIPE
from sys import exit
from time import sleep
from threading import Thread
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

def convertBgFrame(scale1, scale2, filenameIndex):
    run(['convert', tmpbg, '-scale', scale1, '-scale', scale2, bgFrames[filenameIndex]])

convertThreads = []
convertThreads.append(Thread(target=convertBgFrame, args=('5%', '2000%', 0)))
convertThreads.append(Thread(target=convertBgFrame, args=('10%', '1000%', 1)))
convertThreads.append(Thread(target=convertBgFrame, args=('20%', '500%', 2)))
convertThreads.append(Thread(target=convertBgFrame, args=('50%', '200%', 3)))

for thread in convertThreads:
    thread.start()

for thread in convertThreads:
    thread.join()

remove(tmpbg)

def convertOverlayFrame(i):
    run(['convert', bgFrames[i], fgFrames[i], '-gravity', 'center', '-composite', '-matte', overlayFrames[i]])

convertThreads = []

for i in range(len(bgFrames)):
    convertThreads.append(Thread(target=convertOverlayFrame, args=([i])))

for thread in convertThreads:
    thread.start()

for thread in convertThreads:
    thread.join()

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
