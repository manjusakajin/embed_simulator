from env import *
from turtle import *
import random
from link_check import *
from agent import *
from compile import *

class Controlmodule():
  def __init__(self, simulation, agent_module, algorithm):
    self.simulation = simulation
    self._agentmodule = agent_module
    self.agents = []
    self.algorithm = algorithm
  def setup(self):
    if self.simulation.turtle_display != None :
      bgpic = self.simulation.turtle_screen.bgpic()
      self.simulation.turtle_screen.clear()
      if bgpic != 'nopic':
        self.simulation.turtle_screen.bgpic(bgpic)
    ########## Lưu các agent của hệ thống
    for x in self._agentmodule.agents:
      if x!= "New Agent" :
        self.agents.append(x)
    for x in self._agentmodule.agents:
      if x!= "New Agent" :
        if x.type == "Display":
          x.setup(self.simulation.turtle_screen) ##### action và sensor viết hàm setup sau
          print("new turtle")
          self.run_code_setup(x)
          x.agents = x.sensors + x.actuators
          x.compile = Compile(x.agents)
  def run_code_setup(self, displayagent):
    src = displayagent.setup_code.split('\n')
    src.pop()
    for x in src:
      splited = x.split(' ')
      print(splited)
      if splited[0] != 'link' or len(splited) < 2:
        print('syntax error')
      else:
        for y in self.agents:
          if y.name == splited[1]:
            if y.type == "Sensor":
              displayagent.sensors.append(y)
              y.link(displayagent)
            elif y.type == "Active":
              displayagent.actuators.append(y)
              y.link(displayagent)
            else :
              print("Cannot connect " + y.name + " agent")
  def run(self):
    for x in self._agentmodule.agents:
      if x!= "New Agent" :
        if x.type == "Display":
          x.run_loop()
  def run_loop(self):
    while 1:
      self.run()
