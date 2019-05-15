from tkinter import *
from tkinter import ttk

class Algorithm():
  def __init__(self, frame, setup_agent):
    self.frame = frame
    self.loop_code = None
    self.setup_code = None
    self.displayagent = None
    self.setup_agent = setup_agent
    self.initUI()
  def initUI(self):
    agents = []
    for x in self.setup_agent.agents:
      if x != "New Agent" and x.type == 'Display':
          agents.append(x.name)
    self.agent_box = ttk.Combobox(self.frame, values = agents)
    self.agent_box.bind("<<ComboboxSelected>>", self.selectAgent)
    self.agent_box.pack()
    Label(self.frame, text = "Setup:").pack()
    self.setup_entry = Text(self.frame, width = 100, height = 10)
    self.setup_entry.pack()
    Label(self.frame, text = "Loop:").pack()
    self.loop_entry = Text(self.frame, width = 100, height = 20)
    self.loop_entry.pack()
    Button(self.frame, text="save", command=self.save).pack()
  def updateUI(self):
    agents = []
    for x in self.setup_agent.agents:
      if x != "New Agent" and x.type == 'Display':
          agents.append(x.name)
    print(agents)
    self.agent_box.configure(values = agents)
    self.setup_entry.delete('1.0','end')
    self.loop_entry.delete('1.0','end')
  def selectAgent(self, event):
    for x in self.setup_agent.agents:
      print(x)
      if x != "New Agent" and x.name == self.agent_box.get():
        self.displayagent = x
        self.setup_entry.delete('1.0','end')
        self.loop_entry.delete('1.0','end')
        self.setup_entry.insert('end', x.setup_code)
        self.loop_entry.insert('end', x.loop_code)
  def save(self):
    if self.displayagent != None:
      self.displayagent.setup_code = self.setup_entry.get('1.0','end')
      self.displayagent.loop_code = self.loop_entry.get('1.0','end')
