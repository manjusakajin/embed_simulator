import agent
from turtle import *
import random

class Behavior():
  methods = ['randomRun', 'die']
  def __init__(self, agent):
      self.agent = agent
      self.turtle = agent.turtle
      self.width = agent.screen_width
      self.height = agent.screen_height
      self.type = agent.type
  def randomRun(self):
    x = self.turtle.xcor()
    y = self.turtle.ycor()
    moveX = -268
    moveY = -343
    while moveX< - 267 or moveX>267 or moveY<-342 or moveY>342:
      moveX = x + random.randint(-5,5)
      moveY = y + random.randint(-5,5)
    self.turtle.goto(moveX, moveY)
    print(self.turtle.pos())
    print(self.turtle.turtlesize())
  def die(self):
    print('die')
    self.turtle.ht()
    self.type.current_amount -= 1
    self.status = False
