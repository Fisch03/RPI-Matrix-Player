from time import sleep
import threading
import random

import matrix

pieces = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[1, 0, 0],
     [1, 1, 1]],

    [[0, 0, 1],
     [1, 1, 1]],

    [[1, 1, 1, 1]],

    [[1, 1],
     [1, 1]]
]

background = [
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0]
]

gameoverscreen = [
 [1,1,1,1,1,1,1,1],
 [1,1,0,1,1,1,1,1],
 [1,0,0,1,1,1,1,1],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [1,0,0,1,1,1,1,1],
 [1,1,0,1,1,1,1,1],
 [1,1,1,1,1,1,1,1]
]

piecex = None
piecey = None
pieceid = None
piecerot = None

waitingforstart = False

def leftbutton():
  global piecex
  if(not piecex < 1):
    piecex -= 1

def rightbutton():
  global piecex, piecerot, pieceid
  piece = rotatepiece(pieces[pieceid], piecerot)
  if(not piecex > 8 - len(piece[0])):
    piecex += 1

def functionbutton():
  global piecerot
  piecerot += 1
  if(piecerot > 3):
    piecerot = 0

def mainloop():
  global piecex, piecey, pieceid, piecerot
  newpiece()
  t = threading.currentThread()
  while getattr(t, "running", True):
    drawbackground()
    drawpiece()
    sleep(1)
    update()

def newpiece():
  global piecex, piecey, pieceid, piecerot
  piecex = 2
  piecey = 0
  piecerot = 0
  pieceid = random.randint(0, 6)
  if(checkcollision()):
    gameover()

def update():
  global piecex, piecey, pieceid, piecerot
  piecey += 1
  if(piecey > 8 - len(pieces[pieceid]) or checkcollision()):
    fixpiece(pieces[pieceid], piecex, piecey-1, piecerot)
    newpiece()
  checkandclearrows()

def gameover():
  global background, waitingforstart
  waitingforstart = True
  for i in range(0, 8):
    background[i] = gameoverscreen[i]
    drawbackground()
    sleep(0.1)
  while waitingforstart:
    sleep(0.2)
  restart()

def checkandclearrows():
  global background
  for r in range(0, 8):
    fullpixels = 0
    for c in range(0, 8):
      if(background[r][c]):
        fullpixels += 1
    if(fullpixels == 8):
      for i in range(0, 8):
        background[r] = [0,0,0,0,0,0,0,0]
        drawbackground()
        sleep(0.08)
        background[r] = [1,1,1,1,1,1,1,1]
        drawbackground()
        sleep(0.08)
      del background[r]
      background.insert(0, [0,0,0,0,0,0,0,0])
      drawbackground()
      drawpiece()

def checkcollision():
  try:
    global piecex, piecey, pieceid, piecerot, background
    piece = rotatepiece(pieces[pieceid], piecerot)
    for x in range(0, len(piece[0])):
      for y in range(0, len(piece)):
        if(piece[y][x] and background[y + piecey][x + piecex]):
          return True
    return False
  except IndexError:
    return True

def drawpiece():
  global piecex, piecey, pieceid, piecerot
  piece = pieces[pieceid]
  piece = rotatepiece(piece, piecerot)
  for y in range(0, len(piece)):
    for x in range(0, len(piece[0])):
      if(piece[y][x]):
        matrix.set_pixel(x + piecex, y + piecey)

def rotatepiece(piece, rot):
  for r in range(0, rot):
    piece = list(zip(*piece[::-1]))
  return piece

def fixpiece(piece, posx, posy, rot):
  piece = rotatepiece(piece, rot)
  for y in range(0, len(piece)):
    for x in range(0, len(piece[0])):
      if(piece[y][x]):
        background[y + posy][x + posx] = 1

def drawbackground():
  matrix.clear()
  for r in range(0, 8):
    for c in range(0, 8):
      if (background[r][c]):
        matrix.set_pixel(c, r)

def restart():
  newpiece()
  for r in range(0, 8):
    for c in range(0, 8):
      background[r][c] = 0
