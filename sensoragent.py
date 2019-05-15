from compile import *

class SensorAgent():
  def __init__(self, name,  custom_var):
    self.name = name
    self.type = "Sensor"
    self.displayagent = None
    self.value = None
    self.agents = ['displayagent']
    self.compile = Compile(self.agents)
    self.custom_var = self.compile.trans(custom_var)
    print(self.custom_var)
  def update(self, name, custom_var):
    self.name = name
    self.custom_var = custom_var
  def link(self, displayagent):
    self.displayagent = displayagent
  def getValue(self):
    displayagent = self.displayagent
    self.value = eval(self. custom_var)
    return self.value
