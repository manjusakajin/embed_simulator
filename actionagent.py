class ActiveAgent():
  def __init__(self,name, methods):
    self.name = name
    self.methods = methods
    self.type = "Active"

  def update(self, name, methods):
    self.name = name
    self.methods = methods
