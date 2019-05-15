# from tkinter import *
# from tkinter import ttk
# from behavior import *
# from link import *
# from link_check import *
#
# class SetupAssociation():
#   def __init__(self, frame, agentmodule):
#     self.links = []
#     self._subframe = frame
#     self.agent_module = agentmodule
#     self.agents = []
#     for x in self.agent_module.agents:
#       if x != "New Agent":
#         self.agents.append(x.name)
#     self.initUI(frame)
#   def initUI(self, frame):
#     frame.columnconfigure(0,weight=14)
#     frame.columnconfigure(1,weight=1)
#     frame.columnconfigure(2,weight=7)
#     frame.columnconfigure(3,weight=14)
#     frame.columnconfigure(4,weight=7)
#     frame.rowconfigure(0,weight=3)
#     frame.rowconfigure(1,weight=1)
#     frame.rowconfigure(2,weight=1)
#     frame.rowconfigure(3,weight=1)
#     frame.rowconfigure(4,weight=1)
#     frame.rowconfigure(5,weight=1)
#     frame.rowconfigure(6,weight=10)
#     scrollbar = Scrollbar(frame)
#     scrollbar.grid(row=0,column=1,rowspan=7, sticky="nws")
#     self.list = Listbox(self._subframe, yscrollcommand=scrollbar.set, selectmode = "single")
#     self.list.grid(row=0, column=0, rowspan=7, sticky="nwse")
#     for x in self.links:
#       self.list.insert("end", x.agenttype1.name + ' - ' + x.agenttype2.name)
#     Label(self._subframe, text="Create Association", font=("Arial", 20)).grid(row=0,column=3)
#     Label(self._subframe, text="Type 1:").grid(row=1,column=2)
#     self.type1_box = ttk.Combobox(self._subframe, values=self.agents)
#     self.type1_box.grid(row=1, column=3,sticky="ew")
#     self.type1_box.bind("<<ComboboxSelected>>", self.update)
#     Label(self._subframe, text="Type 2:").grid(row=2,column=2)
#     self.type2_box = ttk.Combobox(self._subframe, values=self.agents)
#     self.type2_box.grid(row=2, column=3, sticky="ew")
#     self.type2_box.bind("<<ComboboxSelected>>", self.update)
#     Label(self._subframe, text="Check :").grid(row=3,column=2)
#     self.checkbox = ttk.Combobox(self._subframe, values=CheckLink.methods)
#     self.checkbox.grid(row=3, column=3, sticky="ew")
#     self.checkbox.bind("<<ComboboxSelected>>", self.update)
#     Button(self._subframe, text="Create New").grid(row=3, column=4)
#     Label(self._subframe, text="Type 1 Action :").grid(row=4,column=2)
#     self.action_box_1 = ttk.Combobox(self._subframe, values = Behavior.methods)
#     self.action_box_1.grid(row=4, column=3, sticky="ew")
#     self.action_box_1.bind("<<ComboboxSelected>>", self.update)
#     Button(self._subframe, text="Create New").grid(row=4, column=4)
#     Label(self._subframe, text="Type 2 Action :").grid(row=5,column=2)
#     self.action_box_2 = ttk.Combobox(self._subframe, values = Behavior.methods)
#     self.action_box_2.grid(row=5, column=3,sticky="ew")
#     self.action_box_2.bind("<<ComboboxSelected>>", self.update)
#     Button(self._subframe, text="Create New").grid(row=5, column=4)
#     Button(self._subframe, text="Create", command=self.create).grid(row=6, column=3)
#
#   def add_agenttype(self):
#     self.agents = []
#     for x in self.agent_module.agents:
#       if x != "New Agent":
#         self.agents.append(x.name)
#     self.type1_box.configure(values=self.agents)
#     self.type2_box.configure(values=self.agents)
#   def update(self, event):
#     self.type1 = self.find_agent(self.type1_box.get())
#     self.type2 = self.find_agent(self.type2_box.get())
#     self.checkmethod = self.checkbox.get()
#     self.action1 = self.action_box_1.get()
#     self.action2 = self.action_box_2.get()
#   def create(self):
#     link = Link(self.type1, self.type2, self.checkmethod, self.action1, self.action2)
#     self.list.insert("end", link.agenttype1.name + ' - ' + link.agenttype2.name)
#     self.links.append(link)
#     self.type1_box.set('')
#     self.type2_box.set('')
#     self.checkbox.set('')
#     self.action_box_1.set('')
#     self.action_box_2.set('')
#     print(self.links)
#   def find_agent(self, name):
#     for x in self.agent_module.agents:
#       if x != "New Agent":
#         if x.name == name:
#           return x
#     return None
