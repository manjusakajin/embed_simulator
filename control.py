from env import *
from turtle import *
import random
from link_check import *
from agent import *

class Controlmodule():
  def __init__(self, env_module, agent_module, association_module, screen):
    self._screen = screen
    self._env = env_module
    self._ass = association_module
    self._agentmodule = agent_module
    self.agents = []

  def setup(self):
    self._screen.clear()
    object = Enviroment(self._screen)
    if self._env.bgcolor:
      object.setupbgcolor(self._env.bgcolor)
    if self._env.bgpic:
      object.setupbgpic(self._env.bgpic)
    # if self._env.width and self._env.height:
    #   object.setupgrid(self._env.width, self._env.height)
    # else:
    #   object.setupgrid(100, 100)
    self._screen.mode("logo")
    if self._agentmodule:
      for x in self._agentmodule.agents:
        if x != "New Agent":
          for y in range(x.amount):
            agent = Agent(x, self._screen, self._env.width, self._env.height)
            self.agents.append(agent)
            # turtle = RawPen(self._screen)
            # turtle.shape(x.shape[1])
            # if self._env.width != None and self._env.height != None:
            #   self.originXPosion = random.randint(0, self._env.width)
            #   self.originYPosion = random.randint(0, self._env.height)
            # else:
            #   self.originXPosion = random.randint(0, 100)
            #   self.originYPosion = random.randint(0, 100)
            # turtle.penup()
            # turtle.setposition(self.originXPosion,self.originYPosion)
  def run_agent(self):
    if self.agents:
      for x in self.agents:
        if x.status == True :
          x.move()
        else:
          self.agents.remove(x)
    # self._screen.ontimer(self.run_agent(),5)
  def check_link(self):
    print('check')
    for x in self.agents:
      i = self.agents.index(x) + 1
      j = len(self.agents) -1
      for y in self.agents[i:j]:
        for z in self._ass.links:
          if z.agenttype1 == x.type and z.agenttype2 == y.type:
            result = CheckLink(x,y)
            result = result.check(z.checklink)
            print(result)
            if result == True:
              if z.type1_action != '' and z.type1_action != None:
                x.runmethod(z.type1_action)
              if z.type2_action != '' and z.type1_action != None:
                y.runmethod(z.type2_action)
          elif z.agenttype2 == x.type and z.agenttype1 == y.type:
            result = CheckLink(y,x)
            result = result.check(z.checklink)
            if result == True:
              if z.type1_action != '' and z.type1_action != None:
                y.runmethod(z.type1_action)
              if z.type2_action != '' and z.type1_action != None:
                x.runmethod(z.type2_action)
    self._screen.ontimer(self.check_link(),10)
  def run(self):
    while 1:
      self.run_agent()
