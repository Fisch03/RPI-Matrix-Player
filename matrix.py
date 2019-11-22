matrix = [
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0]
]

def get_matrix():
  return matrix
def set_matrix(newMatrix):
  global matrix
  matrix = newMatrix

def get_pixel(x, y):
  return matrix[y][x]
def set_pixel(x, y):
  global matrix
  matrix[y][x] = 1

def clear():
  for r in range(0, 8):
    for c in range(0, 8):
      matrix[r][c] = 0
