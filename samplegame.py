import threading

def leftbutton(): #On left button press
  pass

def rightbutton(): #On right button press
  pass

def functionbutton(): # On Function Button Press
  pass

def mainloop():
  #Put init stuff here
  t = threading.currentThread()
  while getattr(t, "running", True): #Put Looped Code here
    pass
