import gpio_proxy as GPIO
from time import sleep
import time
import threading
import sys

import matrix_emulator as vMatrix
import matrix

print("")
print("____________________RPI_MATRIX_PLAYER_BY_FISCH03____________________")
from importlib import import_module
try:
  gamemodule = input("Please input the game Module you want to load: ")
  game = import_module(gamemodule)
except ModuleNotFoundError:
  print("Game Module not found, make sure its in the same Folder as this file.")
  print("Exiting Program.")
  sys.exit()

print("Found Module {}".format(gamemodule))
print("Setting up GPIO...", end="")

GPIO.setmode(GPIO.BCM)

datapin = 2
GPIO.setup(datapin, GPIO.OUT)
clkpin = 3
GPIO.setup(clkpin, GPIO.OUT)
showpin = 4
GPIO.setup(showpin, GPIO.OUT)

lbtn = 17
lbtnlast = False
GPIO.setup(lbtn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
rbtn = 27
rbtnlast = False
GPIO.setup(rbtn, GPIO.IN)
fnbtn = 22
fnbtnlast = False
GPIO.setup(fnbtn, GPIO.IN)

GPIO.output(datapin, True)
GPIO.output(clkpin, False)
GPIO.output(showpin, False)

print("done")

emulateMatrix = True
matrixHTime = 1
print("Horizontal Time for Matrix is set to {}ms".format(matrixHTime))
btnups = 50
print("Buttons will be checked {} times per second".format(btnups))


def output_int(number, invert=False):
    binary = format(number, 'b').zfill(8)
    for bit in reversed(binary):
      if (bit == '1'):
        GPIO.output(datapin, True != invert)
        #print(True != invert)
      else:
        GPIO.output(datapin, False != invert)
        #print(False != invert)
      GPIO.output(clkpin, True)
      GPIO.output(clkpin, False)

def show_matrix():
  for r in range(0, 8):
    output_int(2**r)
    for c in range(0, 8):
      GPIO.output(datapin, matrix.get_pixel(c, r)==0)
      GPIO.output(clkpin, True)
      GPIO.output(clkpin, False)
    GPIO.output(showpin, True)
    GPIO.output(showpin, False)
  sleep(matrixHTime / 1000)

def matrixloop():
  t = threading.currentThread()
  while getattr(t, "running", True):
    show_matrix()

def buttonmanager():
  global lbtn, lbtnlast, rbtn, rbtnlast, fnbtn, fnbtnlast
  t = threading.currentThread()
  while getattr(t, "running", True):
    global lbtn, lbtnlast, rbtn, rbtnlast, fnbtn, fnbtnlast
    lbtncurr = GPIO.input(lbtn)
    if(not lbtnlast and lbtncurr):
      game.leftbutton()
      lbtnlast = True
    elif(not lbtncurr):
      lbtnlast = False

    rbtncurr = GPIO.input(rbtn)
    if(not rbtnlast and rbtncurr):
      game.rightbutton()
      rbtnlast = True
    elif(not rbtncurr):
      rbtnlast = False

    fnbtncurr = GPIO.input(fnbtn)
    if(not fnbtnlast and fnbtncurr):
      game.functionbutton()
      fnbtnlast = True
    elif(not fnbtncurr):
      fnbtnlast = False

    sleep(1/btnups)

try:
  print("Setup finished, starting up...")
  print("Starting GPIO-Matrix, Button listener and Game Thread...", end="")
  matrixThr = threading.Thread(target=matrixloop)
  matrixThr.start()
  gameThr = threading.Thread(target=game.mainloop)
  gameThr.start()
  buttonThr = threading.Thread(target=buttonmanager)
  buttonThr.start()
  print("done")
  if(emulateMatrix):
    print("Starting Virtual Matrix...")
    print("Please press ctrl+c instead of closing the window, otherwise the program wont stop.")
    vMatrix.start(matrixHTime*8)
except KeyboardInterrupt:
  print("Stopping...")
  print("Stopping Threads and cleaning up...", end="")
  GPIO.cleanup()
  matrixThr.running = False
  gameThr.running = False
  buttonThr.running = False
  if(emulateMatrix):
    vMatrix.close()
  print("done")
  print("Exiting Program.")
