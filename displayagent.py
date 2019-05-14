from turtle import *

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
    self.type = "Display"

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
