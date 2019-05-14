from turtle import *
from agent import *
from env import *

class Control():
  def __init__(self, env=None, agents=[]):
    print("bộ điều khiển")
    self.env = env
    self.agents = agents

  def timerbehave(self):
    for x in self.agents:
      for y in range(len(x)):
        if y > 0:
          x[y].randomRun()
    for sheep in self.agents[1]:
      for wolf in self.agents[0]:
        if sheep == "sheep" or wolf == "wolf":
          continue
        if sheep.simulation.distance(wolf.simulation) <= 5:
          sheep.die()
    self.env.screen.ontimer(self.timerbehave())

  def run(self):
    self.env.screen.ontimer(self.timerbehave())
    self.env.run()
