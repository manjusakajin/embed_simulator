from turtle import *

class Enviroment():
  def __init__(self, screen=None):
    self.screen = screen

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
      self.screen.setworldcoordinates(-20,-20,x+20,y+20)
