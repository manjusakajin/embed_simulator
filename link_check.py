from tkinter import *
from turtle import *

class CheckLink():
  methods = ['distance']
  def __init__(self, agent1, agent2):
    self.agent1=agent1
    self.agent2=agent2
    self.params = []
  def check(self,method):
    return eval('self.' + method + '()')
  def distance(self):
    if self.agent1.turtle.distance(self.agent2.turtle) <=5 :
      return True
    else:
      return False
