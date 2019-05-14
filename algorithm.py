from tkinter import *

class Algorithm():
  def __init__(self, frame):
    self.frame = frame
    self.initUI()
  def initUI(self):
    Label(self.frame, text = "Setup:").pack()
    Text(self.frame, width = 40, height = 5).pack()
    Label(self.frame, text = "Loop:").pack()
    Text(self.frame, width = 40, height = 5).pack()
