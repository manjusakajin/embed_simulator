from turtle import *
from PIL import Image
import math
from colormap import rgb2hex
from compile import *

class DisplayAgent():
  def __init__(self, name, shape, x, y,heading):
    self.name = name
    self.shape = shape
    if self._is_int(x) == True :
      self.x = int(x)
    else :
      self.x = 0
    if self._is_int(y) == True :
      self.y = int(y)
    else :
      self.y = 0
    if self._is_int(heading) == True :
      self.heading = int(heading)
    else :
      self.heading = 0
    print(self.x, self.y)
    self.type = "Display"
    self.setup_code = ''
    self.loop_code = ''
    self.sensors = []
    self.actuators = []
    self.agents = []

  def update(self, name, shape, x, y,heading):
    self.name = name
    self.shape = shape
    if self._is_int(x) == True :
      self.x = int(x)
    else :
      self.x = 0
    if self._is_int(y) == True :
      self.y = int(y)
    else :
      self.y = 0
    if self._is_int(heading) == True :
      self.heading = int(heading)
    else :
      self.heading = 0
  def _is_int(self,x):
    try:
        x = int(x)
        return True
    except:
        return False
  def setup(self, screen):
    self.turtle = RawPen(screen)
    self.turtle.penup()
    if self.shape != None :
      self.turtle.shape(self.shape)
    else :
      self.turtle.shape("blank")
    self.turtle.setpos(self.x, self.y)
    self.turtle.setheading(self.heading)
    print(self.turtle.turtlesize())
    self.map = self.getMap()
  def getpgpic(self):
    if self.turtle.getscreen().bgpic() != 'nopic':
      print(self.turtle.getscreen().bgpic())
      return self.turtle.getscreen().bgpic()
  def getMap(self):
    map = []
    if self.getpgpic() != None:
      im = Image.open(self.getpgpic())
      rgpim = im.convert('RGB')
      width, height = im.size
      print(width, height)
      for y in range(height):
        for x in range(width):
          r,g,p = rgpim.getpixel((x,y))
          map.append(rgb2hex(r, g, p))
      return map
  def askColor(self, x, y): ### Tọa độ ảnh tính từ trái sang phải trên xuống dưới
    return self.map[int(y)*670+int(x)]

  def screencorToPicturecor(self, x,y):
    print([abs(x+335), abs(y-260)])
    return [abs(x+335), abs(y-260)]

  def leftColor(self):
    x,y = self.getLeft(30)
    print('left:' +str(x) +','+str(y) )
    x,y = self.screencorToPicturecor(x,y)
    print(self.askColor(x,y))
    return self.askColor(x,y)

  def rightColor(self):
    x,y = self.getRight(30)
    print('right:' +str(x) +','+str(y) )
    x,y = self.screencorToPicturecor(x,y)
    print(self.askColor(x,y))
    return self.askColor(x,y)
  def getRight(self, h):
    heading = self.turtle.heading()
    xcor = self.turtle.xcor()
    ycor = self.turtle.ycor()
    print(str(xcor), str(ycor))
    print(heading)
    if  heading < 90 :
      y = ycor - h* math.sin(math.radians(90-heading))
      x = xcor + h* math.cos(math.radians(90-heading))
    elif heading < 180:
      y = ycor + h* math.cos(math.radians(180-heading))
      x = xcor + h* math.sin(math.radians(180-heading))
    elif heading < 270 :
      y = ycor + h* math.sin(math.radians(270-heading))
      x = xcor - h* math.cos(math.radians(270-heading))
    elif heading < 360 :
      y = ycor - h* math.cos(math.radians(360-heading))
      x = xcor - h* math.sin(math.radians(360-heading))
    # self.turtle.getscreen().getcanvas().create_line(x,-y, xcor, -ycor)
    return [x,y]
  def getLeft(self, h):
    heading = self.turtle.heading()
    xcor = self.turtle.xcor()
    ycor = self.turtle.ycor()
    print(str(xcor), str(ycor))
    if  heading < 90 :
      y = ycor + h* math.sin(math.radians(90-heading))
      x = xcor - h* math.cos(math.radians(90-heading))
    elif heading < 180:
      y = ycor - h* math.cos(math.radians(180-heading))
      x = xcor - h* math.sin(math.radians(180-heading))
    elif heading < 270 :
      y = ycor - h* math.sin(math.radians(270-heading))
      x = xcor + h* math.cos(math.radians(270-heading))
    elif heading < 360 :
      y = ycor + h* math.cos(math.radians(360-heading))
      x = xcor + h* math.sin(math.radians(360-heading))
    # self.turtle.getscreen().getcanvas().create_line(x,-y, xcor, -ycor)
    return [x,y]

  def run_loop(self):
    for x in self.agents:
      exec(x.name +'= x')
      print(x.name)
    print(self.compile.trans(self.loop_code))
    exec(self.compile.trans(self.loop_code))

  def turnleft(self):
    self.turtle.left(1)
  def turnright(self):
    self.turtle.right(1)
  def forward(self):
    self.turtle.forward(1)
  def undo(self):
    self.turtle.undo()
