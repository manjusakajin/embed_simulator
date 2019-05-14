import tkinter as tk
from turtle import *
import random
import behavior

class Agent():
  def __init__(self, agenttype, screen, width, height):
    self.turtle = RawPen(screen)
    self.turtle.shape(agenttype.shape[1])
    self.type = agenttype
    self.move_behavior = agenttype.move_behavior
    self.screen_width = width
    self.screen_height = height
    self.behavior_module = behavior.Behavior(self)
    self.status = True
    self.setupPosition()
  def setupPosition(self):
    if self.screen_width != None and self.screen_height != None:
      self.originXPosition = random.randint(0, self.screen_width)
      self.originYPosition = random.randint(0, self.screen_height)
    else:
      self.originXPosition = random.randint(0, 100)
      self.originYPosition = random.randint(0, 100)
    self.turtle.penup()
    self.turtle.setposition(self.originXPosition,self.originYPosition)
  def move(self):
    exec('self.behavior_module.' + self.move_behavior + '()')
  def runmethod(self, name):
    print("runmethod")
    exec('self.behavior_module.' + name + '()')
