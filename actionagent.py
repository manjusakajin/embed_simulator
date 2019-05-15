from compile import *
from turtle import *

class ActiveAgent():
  def __init__(self,name, method):
    self.name = name
    self.type = "Active"
    self.agents = ['displayagent']
    self.compile = Compile(self.agents)
    self.method = self.compile.trans(method)
    print(self.method)
  def update(self, name, method):
    self.name = name
    self.method = method

  def link(self, displayagent):
    self.displayagent = displayagent
  def run(self):
    displayagent = self.displayagent
    exec(self.method)
