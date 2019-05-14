class DisplayAgent():
  def __init__(self, name, shape, behavior, custom_behavior, x, y,heading):
    self.name = name
    self.shape = shape
    self.behavior = behavior
    self.custom_behavior = custom_behavior
    self.x = x
    self.y = y
    self.heading = heading
    self.type = "Display"

  def update(self, name, shape, behavior, custom_behavior, x, y,heading):
    self.name = name
    self.shape = shape
    self.behavior = behavior
    self.custom_behavior = custom_behavior
    self.x = x
    self.y = y
    self.heading = heading
