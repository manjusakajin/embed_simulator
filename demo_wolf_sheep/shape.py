from turtle import *
import tkinter as tk

class CustomShape():
  def __init__(self, keyword):
    self.name = keyword

  def paintShape(self, type, data):
    self.type = type
    if type == "image":
      self.shapeImage = tk.PhotoImage(file=data)
      self.shape = Shape(type, self.shapeImage)
    else:
      self.shape = Shape(type,data)
    register_shape(self.name,self.shape)
