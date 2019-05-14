from env import *
from turtle import *
import random
from link_check import *
from agent import *

class Controlmodule():
  def __init__(self, env_module, agent_module, algorithm, screen=None):
    self._screen = screen
    self._env = env_module
    self._agentmodule = agent_module
    self.agents = []
    self.sensors = []
    self.actions = []
    self.displays = []
    self.decision = algorithm

  def setup(self):
    if self._screen != None :
      print("Hiển thị giao diện mô phỏng")
    ########## Lưu các agent của hệ thống
    for x in self._agentmodule.agents:
      if x!= "New Agent" :
        self.agents.append(x)
        if x.type == "Display":
          x.setup(self._screen) ##### action và sensor viết hàm setup sau
    exec(self.decision.setup_code)

  # def run_agent(self):
  #   if self.agents:
  #     for x in self.agents:
  #       if x.status == True :
  #         x.move()
  #       else:
  #         self.agents.remove(x)
  #   # self._screen.ontimer(self.run_agent(),5)
  # def check_link(self):
  #   print('check')
  #   for x in self.agents:
  #     i = self.agents.index(x) + 1
  #     j = len(self.agents) -1
  #     for y in self.agents[i:j]:
  #       for z in self._ass.links:
  #         if z.agenttype1 == x.type and z.agenttype2 == y.type:
  #           result = CheckLink(x,y)
  #           result = result.check(z.checklink)
  #           print(result)
  #           if result == True:
  #             if z.type1_action != '' and z.type1_action != None:
  #               x.runmethod(z.type1_action)
  #             if z.type2_action != '' and z.type1_action != None:
  #               y.runmethod(z.type2_action)
  #         elif z.agenttype2 == x.type and z.agenttype1 == y.type:
  #           result = CheckLink(y,x)
  #           result = result.check(z.checklink)
  #           if result == True:
  #             if z.type1_action != '' and z.type1_action != None:
  #               y.runmethod(z.type1_action)
  #             if z.type2_action != '' and z.type1_action != None:
  #               x.runmethod(z.type2_action)
  #   self._screen.ontimer(self.check_link(),10)
  # def run(self):
  #   while 1:
  #     self.run_agent()
