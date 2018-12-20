# Program PlayerPiano
# Description: 
# 	A player piano that asks the user if they want the program to play
#   a preset song, or play the piano it self.
#   Some limitations: Pygame itself can be very laggy without lines and lines of code for time events,
#   and relying on the Pygame.time.clock() function for everything is a huge limitation
#   For some reason Pygame isn't handling my music files very well, even though the
#   file itself is spliced correctly, Pygame treats it weirdly
#   When playing any of the three music files, the piano is not animated,
#   though when you play by your self it is.
# Author: Troy Krupinski
# Date: 4/28/17
# Revised: 
# 	5/13/17
# list libraries used

import pygame
import sys
from tkinter import *
import time


# Declare global constants
BACKGROUND = (169,169,169)
DISPLAY_WIDTH = 1600
DISPLAY_HEIGHT = 900


pygame.init()

pygame.mixer.init()
#initializes pygame and the sound mixer (from pygame)


gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT)) #sets resolution for screen

pygame.display.set_caption('PlayerPiano') #sets window title

clock = pygame.time.Clock()

CurrentSong = ''

#impoting all files needed for game

tt = 'TwinkleTwinkleLittleStar.ogg'
hbd = 'HappyBirthdayToYou.ogg'
omd = 'OldMacdonaldHadAFarm.ogg'


key1 = pygame.image.load('BlackKey.png')
key2 = pygame.image.load('WhiteKey.png')
F1 = pygame.image.load('F.PNG')
G1 = pygame.image.load('G.PNG')
A1 = pygame.image.load('A.PNG')
B1 = pygame.image.load('B.PNG')
C1 = pygame.image.load('C.PNG')
D2 = pygame.image.load('D.PNG')
E2 = pygame.image.load('E.PNG')
F2 = pygame.image.load('F2.PNG')
G2 = pygame.image.load('G2.PNG')
F1P = pygame.image.load('Fpress.PNG')
G1P = pygame.image.load('Gpress.PNG')
A1P = pygame.image.load('Apress.PNG')
B1P = pygame.image.load('Bpress.PNG')
C1P = pygame.image.load('Cpress.PNG')
D2P = pygame.image.load('Dpress.PNG')
E2P = pygame.image.load('Epress.PNG')
F2P = pygame.image.load('F2press.PNG')
G2P = pygame.image.load('G2press.PNG')
title = pygame.image.load('Title.PNG')
menu = pygame.image.load('Menu.PNG')
crh = pygame.image.load('crhbd.PNG')
crnone = pygame.image.load('crnone.PNG')
currentsong = pygame.image.load('CurrentSong.PNG')
crt = pygame.image.load('crttls.PNG')
cromd = pygame.image.load('cromd.PNG')
onown = pygame.image.load('onyourown.PNG')

lead_x = 23
lead_y = 23

playingbyyourself = False




def piano():

    gameDisplay.blit(key2, (100, 350))
    gameDisplay.blit(key2, (191, 350))
    gameDisplay.blit(key2, (282, 350))
    gameDisplay.blit(key2, (373, 350))
    gameDisplay.blit(key2, (464, 350))
    gameDisplay.blit(key2, (555, 350))
    gameDisplay.blit(key2, (646, 350))
    gameDisplay.blit(key2, (737, 350))
    gameDisplay.blit(key2, (828, 350))
    gameDisplay.blit(title, (280, 10))
    gameDisplay.blit(menu, (1000,200))
    gameDisplay.blit(key1, (160, 350))
    gameDisplay.blit(key1, (250, 350))
    gameDisplay.blit(key1, (350, 350))
    gameDisplay.blit(key1, (530, 350))
    gameDisplay.blit(key1, (630, 350))
    gameDisplay.blit(key1, (800, 350))
    gameDisplay.blit(onown, (300, 100))



    pygame.display.update()
akeysound = pygame.mixer.Sound('A.ogg')
f2keysound = pygame.mixer.Sound('F2.ogg')
e1keysound = pygame.mixer.Sound('E1.ogg')
g2keysound = pygame.mixer.Sound('G2.ogg')
dkeysound = pygame.mixer.Sound('D.ogg')
bkeysound = pygame.mixer.Sound('B.ogg')
g1keysound = pygame.mixer.Sound('G1.ogg')
c1keysound = pygame.mixer.Sound('C.ogg')

#Variables for image coordinates
key2x = 100
key2y = 350

F1posx = 100
F1posy = 500

G1posx = 191
G1posy = 500

A1posx = 282
A1posy = 500

B1posx = 373
B1posy = 500

C1posx = 464
C1posy = 500

D2posx = 555
D2posy = 500

E2posx = 646
E2posy = 500

F2posx = 737
F2posy = 500

G2posx = 828
G2posy = 500

F1pposx = -100
F1pposy = -100

G1pposx = -100
G1pposy = -100

A1pposx = -100
A1pposy = -100

B1pposx = -100
B1pposy = -100

C1pposx = -100
C1pposy = -100

D2pposx = -100
D2pposy = -100

E2pposx = -100
E2pposy = -100

F2pposx = -100
F2pposy = -100

G2pposx = -100
G2pposy = -100

ccomdx = -100
ccomdy = -100

ccttx = -100
cctty = -100

cchbdx = -100
cchbdy = -100

crx = 200
cry = 200

#passing back coordinate variables that are changed in the main game loop
def currentsongs(crx, cry):
    gameDisplay.blit(currentsong, (crx, cry))

def currentsongtt(ccttx, cctty):
    gameDisplay.blit(crt, (ccttx, cctty))

def currentsongomd(ccomdx, ccomdy):
    gameDisplay.blit(cromd, (ccomdx, ccomdy))

def currentsonghbd(cchbdx, cchbdy):
    gameDisplay.blit(crh, (cchbdx, cchbdy))

def key2pos(key2x,key2y):
    gameDisplay.blit(key2, (key2x,key2y))

def f1key(F1posx,F1posy):
    gameDisplay.blit(F1, (F1posx,F1posy))

def g1key(G1posx,G1posy):
    gameDisplay.blit(G1, (G1posx,G1posy))
    
def a1key(A1posx,A1posy):
    gameDisplay.blit(A1, (A1posx,A1posy))

def b1key(B1posx,B1posy):
    gameDisplay.blit(B1, (B1posx,B1posy))
    
def c1key(C1posx,C1posy):
    gameDisplay.blit(C1, (C1posx,C1posy))
    
def d2key(D2posx,D2posy):
    gameDisplay.blit(D2, (D2posx,D2posy))
    
def e2key(E2posx,E2posy):
    gameDisplay.blit(E2, (E2posx,E2posy))

def f2key(F2posx,F1posy):
    gameDisplay.blit(F2, (F2posx,F1posy))
    
def g2key(G2posx,G2posy):
    gameDisplay.blit(G2, (G2posx,G2posy))

def f1pkeyp(F1pposx, F1pposy):
    gameDisplay.blit(F1P, (F1pposx, F1pposy))

def g1pkeyp(G1pposx, G1pposy):
    gameDisplay.blit(G1P, (G1pposx, G1pposy))

def a1pkeyp(A1pposx, A1pposy):
    gameDisplay.blit(A1P, (A1pposx, A1pposy))

def b1pkeyp(B1pposx, B1pposy):
    gameDisplay.blit(B1P, (B1pposx, B1pposy))

def c1pkeyp(C1pposx, C1pposy):
    gameDisplay.blit(C1P, (C1pposx, C1pposy))

def d2pkeyp(D2pposx, D2pposy):
    gameDisplay.blit(D2P, (D2pposx, D2pposy))

def e2pkeyp(E2pposx, E2pposy):
    gameDisplay.blit(E2P, (E2pposx, E2pposy))

def f2pkeyp(F2pposx, F1pposy):
    gameDisplay.blit(F2P, (F2pposx, F1pposy))

def g2pkeyp(G2pposx, G2pposy):
    gameDisplay.blit(G2P, (G2pposx, G2pposy))


gameExit = False


while not gameExit: #main game loop

    for event in pygame.event.get(): #getting the inputs / events
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP1: #twinkle twinkle little star
                CurrentSong = tt
                pygame.mixer.music.stop()
                pygame.mixer.music.load(CurrentSong)
                pygame.mixer.music.play(0)
                ccomdx = -100
                ccomdy = -100
                ccttx = 550
                cctty = 200
                cchbdx = -100
                cchbdy = -100
                playanimation = 1
                playingbyyourself = False
            elif event.key == pygame.K_2 or event.key == pygame.K_KP2: #happy birthday to you
                #sound = pygame.mixer.music.load((music[1]))
                CurrentSong = hbd
                pygame.mixer.music.stop()
                pygame.mixer.music.load(CurrentSong)
                pygame.mixer.music.play(0)
                ccomdx = -100
                ccomdy = -100
                ccttx = -100
                cctty = -100
                cchbdx = 550
                cchbdy = 200
                playanimation = 2
                playingbyyourself = False
            elif event.key == pygame.K_3 or event.key == pygame.K_KP3: #old macdonald had a farm
                #sound = pygame.mixer.music.load((music[1]))
                CurrentSong = omd
                pygame.mixer.music.stop()
                pygame.mixer.music.load(CurrentSong)
                ccomdx = 550
                ccomdy = 200
                ccttx = -100
                cctty = -100
                cchbdx = -100
                cchbdy = -100
                playingbyyourself = False
                pygame.mixer.music.play(0)
            elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                pygame.mixer.music.stop()
                ccomdx = -100
                ccomdy = -100
                ccttx = -100
                cctty = -100
                cchbdx = -100
                cchbdy = -100
                print('')
                playingbyyourself = True
                #Playing by yourself input logic
            elif event.key == pygame.K_a:
                if playingbyyourself == True:
                    pygame.mixer.music.stop()
                    g1keysound.play(0)
            elif event.key == pygame.K_s:
                if playingbyyourself == True:
                    pygame.mixer.music.stop()
                    G1posx = -100
                    G1posy = -100
                    G1pposx = 191
                    G1pposy = 500
                    g1pkeyp(G1pposx, G1pposy)
                    pygame.display.update()
                    g1keysound.play(0)
                    time.sleep(.3)
                    G1posx = 191
                    G1posy = 500
                    G1pposx = -100
                    G1pposy = -100
                    g1pkeyp(G1pposx, G1pposy)
                    pygame.display.update()
            elif event.key == pygame.K_d:
                if playingbyyourself == True:
                    pygame.mixer.music.stop()
                    Apposx = 282
                    Apposy = 500
                    a1pkeyp(Apposx, Apposy)
                    pygame.display.update()
                    akeysound.play(0)
                    time.sleep(.3)
                    Apposx = -100
                    Apposy = -100
                    a1pkeyp(Apposx, Apposy)
                    pygame.display.update()
            elif event.key == pygame.K_f:
                if playingbyyourself == True:
                    pygame.mixer.music.stop()
                    B1pposx = 373
                    B1pposy = 500
                    b1pkeyp(B1pposx, B1pposy)
                    pygame.display.update()
                    bkeysound.play(0)
                    time.sleep(.3)
                    B1pposx = -100
                    B1pposy = -100
                    b1pkeyp(B1pposx, B1pposy)
                    pygame.display.update()

            elif event.key == pygame.K_g:
                if playingbyyourself == True:
                    pygame.mixer.music.stop()
                    C1pposx = 464
                    C1pposy = 500
                    c1pkeyp(C1pposx, C1pposy)
                    pygame.display.update()
                    c1keysound.play(0)
                    time.sleep(.3)
                    C1pposx = -100
                    C1pposy = -100
                    c1pkeyp(C1pposx, C1pposy)
                    pygame.display.update()
            elif event.key == pygame.K_h:
                if playingbyyourself == True:
                    pygame.mixer.music.stop()
                    Dposy = -100
                    Dpposx = 555
                    Dpposy = 500
                    d2pkeyp(Dpposx, Dpposy)
                    pygame.display.update()
                    dkeysound.play(0)
                    time.sleep(.3)
                    Dposx = 555
                    Dposy = 500
                    Dpposx = -100
                    Dpposy = -100
                    d2pkeyp(Dpposx, Dpposy)
                    pygame.display.update()
            elif event.key == pygame.K_j:
                if playingbyyourself == True:
                    pygame.mixer.music.stop()
                    E2pposx = 646
                    E2pposy = 500
                    e2pkeyp(E2pposx, E2pposy)
                    pygame.display.update()
                    e1keysound.play(0)
                    time.sleep(.3)
                    E2pposx = -100
                    E2pposy = -100
                    e2pkeyp(E2pposx, E2pposy)
                    pygame.display.update()
            elif event.key == pygame.K_k:
                if playingbyyourself == True:
                    pygame.mixer.music.stop()
                    Fpposx = 737
                    Fpposy = 500
                    f2pkeyp(Fpposx, Fpposy)
                    pygame.display.update()
                    f2keysound.play(0)
                    time.sleep(.3)
                    Fpposx = -100
                    Fpposy = -100
                    f2pkeyp(Fpposx, Fpposy)
                    pygame.display.update()
            elif event.key == pygame.K_l:
                if playingbyyourself == True:
                    pygame.mixer.music.stop()
                    G2pposx = 828
                    G2pposy = 500
                    g2pkeyp(G2pposx, G2pposy)
                    pygame.display.update()
                    g2keysound.play(0)
                    time.sleep(.3)
                    G2pposx = -100
                    G2pposy = -100
                    g2pkeyp(G2pposx, G2pposy)
                    pygame.display.update()

    gameDisplay.fill(BACKGROUND)

    piano()

    #calling functions, then updating the screen
    f1key(F1posx, F1posy)
    g1key(G1posx, G1posy)
    a1key(A1posx, A1posy)
    b1key(B1posx, B1posy)
    c1key(C1posx, C1posy)
    d2key(D2posx, D2posy)
    e2key(E2posx, E2posy)
    f2key(F2posx, F1posy)
    g2key(G2posx, G2posy)
    f1pkeyp(F1pposx, F1pposy)
    g1pkeyp(G1pposx, G1pposy)
    a1pkeyp(A1pposx, A1pposy)
    b1pkeyp(B1pposx, B1pposy)
    c1pkeyp(C1pposx, C1pposy)
    d2pkeyp(D2pposx, D2pposy)
    e2pkeyp(E2pposx, E2pposy)
    f2pkeyp(F2pposx, F1pposy)
    g2pkeyp(G2pposx, G2pposy)
    currentsongs(crx, cry)
    currentsongtt(ccttx, cctty)
    currentsonghbd(cchbdx, cchbdy)
    currentsongomd(ccomdx, ccomdy)


    pygame.display.update()

    clock.tick(20) #Frames Per Second

pygame.quit()
quit()


