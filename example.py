from turtle import *
from PIL import Image
import math
from colormap import rgb2hex
from compile import *

map = []
im = Image.open('Image/map.png')
rgpim = im.convert('RGB')
width, height = im.size
print(width, height)
for y in range(height):
  for x in range(width):
    r,g,p = rgpim.getpixel((x,y))
    map.append(rgb2hex(r, g, p))
    print(rgb2hex(r, g, p),end="")
  print("")
