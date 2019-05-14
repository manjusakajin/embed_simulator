from turtle import *
from agent import *
from env import *
from control import *
from shape import *

class Simulation():
  def __init__(self):
    self.env = Enviroment()
    self.agents = []
    self.control = Control(self.env, self.agents)

  def setupENV(self, bgcolor=None, bgpic=None):
    self.env.setupgrid(200,200)
    if bgcolor != None:
      self.env.setupbgcolor(bgcolor)
    if bgpic != None:
      self.env.setupbgpic(bgpic)

  def setupAgent(self): # cần viết tổng quát lênange
    wolfShape = CustomShape("wolf")
    wolfShape.paintShape("image", "wolf.png")
    sheepShape = CustomShape("sheep")
    sheepShape.paintShape("image", "sheep.png")
    self._create_agent('wolf',"wolf",10)
    self._create_agent('sheep', "sheep",10)

  def setup(self):
    self.setupENV("green") #xem nên nhập các thứ vào ntn
    self.setupAgent()

  def run(self):
    print(self.control.agents)
    self.control.run()

############################private#############################################
  def _addAgent(self, agent=None):
    if agent != None:
      for x in self.agents:
        if x[0] == agent.type:
          x.append(agent)
          return
      self.agents.append([agent.type,agent])

  def _create_agent(self, agentType=None, shape=None, amount=1):
    for x in range(amount):
      if agentType != None:
        agent = Agent(agentType, shape, self.env)
        self._addAgent(agent)

##########################Main comand##################################################
simulation = Simulation()
simulation.setup()
simulation.run()
