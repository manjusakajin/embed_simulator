import tkinter as tk
from turtle import *
import random

class Agent():
  def __init__(self, type=None, shape='arrow', env=None):
    self.type = type
    self.shape = shape
    self.env = env
    self.originXPosion = random.randint(0, env.width)
    self.originYPosion = random.randint(0, env.height)
    self.simulation = Turtle()
    self.simulation.shape(shape)
    self.simulation.penup()
    self.simulation.setposition(self.originXPosion,self.originYPosion)

  def randomRun(self):
    x = self.simulation.xcor()
    y = self.simulation.ycor()
    moveX = -1
    moveY = -1
    while moveX<0 or moveX>self.env.width and moveY<0 and moveY>self.env.height:
      moveX = x + random.randint(-5,5)
      moveY = y + random.randint(-5,5)
    self.simulation.goto(moveX, moveY)
    print("ramdomRun")

  def die(self):
    self.simulation.ht()
    print("die")
