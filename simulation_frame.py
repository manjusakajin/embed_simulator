import tkinter as tk
import turtle
from setup_env import *

class SimulationModule():
  def __init__(self, master = None):
    self._master = master
    self.initUI()
    self.simulation_screen = None
    self.turtle_screen = None
    self.turtle_display = None
  def initUI(self):
    # tk.Button(self._master, text="Add").pack()
    options = {' ', 'Simulation Screen'}
    self.option = tk.StringVar(self._master.master)
    self.option.set(' ')
    self.option.trace('w', self.change_dropdown)
    popupMenu = tk.OptionMenu(self._master, self.option, *options)
    popupMenu.pack()

  def change_dropdown(self, *args):
    option = self.option.get()
    if option == 'Simulation Screen':
      print(option)
      if self.simulation_screen == None:
        self.simulation_screen = tk.Frame(self._master, width=685, height=535)
        self.simulation_screen.place(x=300, y=50)
        self.turtle_display = tk.Canvas(self._master, width=670, height=520, background='white')
        self.turtle_display.pack()
        self.turtle_screen = turtle.TurtleScreen(self.turtle_display)
        self.screen_edit_button = tk.Button(self._master, text="Edit", command=self.edit_screen)
        self.screen_edit_button.place(x=300, y=570)
        self.screen_delete_button = tk.Button(self._master, text="Delete", command=self.delete_screen)
        self.screen_delete_button.place(x=350, y=570)
  def delete_screen(self):
    self.simulation_screen.place_forget()
    self.simulation_screen = None
    self.turtle_display = None
    self.turtle_screen = None
    self.screen_edit_button.place_forget()
    self.screen_delete_button.place_forget()
  def edit_screen(self):
    top = tk.Toplevel()
    top.title("Setup screen")
    top.geometry('1000x550')
    SetupENV(top, self.turtle_screen)
