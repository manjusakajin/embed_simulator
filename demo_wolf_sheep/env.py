from turtle import *

class Enviroment():
  def __init__(self):
    self.screen = Screen()

  def setupbgcolor(self, bgcolor=None):
    if bgcolor != None:
      self.bgcolor = bgcolor
      self.screen.bgcolor(bgcolor)

  def setupbgpic(self, bgpic=None):
    if bgpic != None:
      self.bgpic = bgpic
      self.screen.bgpic(bgpic)

  def setupgrid(self, x=None, y=None):
    if x != None and y!= None :
      self.width = x
      self.height = y
      setworldcoordinates(0,0,x+20,y+20)
  def run(self):
    self.screen.mainloop()
