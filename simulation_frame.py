import tkinter as tk
import turtle

class SimulationModule():
  def __init__(self, master = None):
    self.sub_frame = tk.Frame(master, width=685, height=535)
    self.sub_frame.place(x=300, y=5)
    self.turtle_display = tk.Canvas(self.sub_frame, width=670, height=520, background='white')
    self.turtle_display.pack()
    self.turtle_screen = turtle.TurtleScreen(self.turtle_display)
