import tkinter as tk
import matrix

canvasWidth = 500
canvasHeight = 500

leds = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

def close():
  master.destroy()

def update(hTime):
  try:
    for r in range(0, 8):
      for c in range(0, 8):
          if(matrix.get_pixel(r, c)):
            canvas.itemconfigure(leds[c][r], fill="red")
          else:
            canvas.itemconfigure(leds[c][r], fill="white")
    canvas.after(hTime, lambda: update(hTime))
  except KeyboardInterrupt:
    pass

def start(hTime):
  for r in range(0, 8):
      for c in range(0, 8):
          leds[c][r] = canvas.create_oval(r*(canvasWidth/8), c*(canvasHeight/8), (r+1)*(canvasWidth/8), (c+1)*(canvasHeight/8), fill="white")
  master.title("Virtual Matrix Emulator")
  master.after(hTime, lambda: update(hTime))
  master.mainloop()

master = tk.Tk()
canvas = tk.Canvas(master, width=canvasWidth, height=canvasHeight)
canvas.pack()
