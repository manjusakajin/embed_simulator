from tkinter import *

class Algorithm():
  def __init__(self, frame):
    self.frame = frame
    self.loop_code = None
    self.setup_code = None
    self.initUI()
  def initUI(self):
    Label(self.frame, text = "Setup:").pack()
    self.setup_entry = Text(self.frame, width = 100, height = 10).pack()
    Label(self.frame, text = "Loop:").pack()
    self.loop_entry = Text(self.frame, width = 100, height = 20).pack()
    Button(self.frame, text="save", command=self.save).pack()
  def save(self):
    self.setup_code = self.setup_entry
    self.loop_code = self.loop_entry
