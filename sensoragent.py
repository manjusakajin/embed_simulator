class SensorAgent():
  def __init__(self, name,  custom_var):
    self.name = name
    self.type = "Sensor"
    self.custom_var = custom_var

  def update(self, name, custom_var):
    self.name = name
    self.custom_var = custom_var
