import tkinter as tk
import turtle
# import compile
import algorithm as al
from simulation_frame import *
from setup_env import *
from setup_agent import *
from control import *

class Application(tk.Frame):
    def __init__(self, master=None):
      super().__init__(master)
      self.tk = master
      self.pack()
      self.create_sub_frame()
      self.create_widgets()

    def create_sub_frame(self):
      self.sub_frame1 = tk.Frame(self.master, width=1000, height=550, borderwidth=5, relief="groove")
      self.sub_frame3 = tk.Frame(self.master, width=1000, height=550, borderwidth=5, relief="groove")
      self.sub_frame4 = tk.Frame(self.master, width=1000, height=550, borderwidth=5, relief="groove")
      self.sub_frame2 = tk.Frame(self.master, width=1000, height=550, borderwidth=5, relief="groove")

      self.simulation_module = SimulationModule(self.sub_frame1)
      self.sub_frame1.pack(fill="both", expand=True)
      self.current_frame = self.sub_frame1
      # self.turtle_screen = self.simulation_module.turtle_screen
      # self.setup_env = SetupENV(self.sub_frame3)
      self.setup_agent = SetupAgent(self.sub_frame4)
      self.setup_algorithm = al.Algorithm(self.sub_frame2, self.setup_agent)
      # self.setup_association = SetupAssociation(self.sub_frame3, self.setup_agent)
      self.control = Controlmodule(self.simulation_module, self.setup_agent, self.setup_algorithm )

    def create_widgets(self):
    #############################simulation frame #################################
      # if self.control:
      #   tk.Button(self.sub_frame1, text="Setup", command=self.control.setup).place(x=50, y=50)
        # tk.Button(self.sub_frame1, text="Run", command=self.control.run).place(x=50, y=150)
 ##################################setup code frame################################
      # self.sub_frame2 = tk.Frame(self.master, width=1000, height=550, borderwidth=5, relief="groove")
      # self.create_code_frame()
########################################setup enviroment##################################
########################################setup agent#########################################
########################################create button#########################################
      self.interface_button = tk.Button(self, text="Simulation", command=self.display_s_frame)
      self.interface_button.pack(side="left")

      # self.code_button = tk.Button(self, text="Enviroment", command=self.display_e_frame)
      # self.code_button.pack(side="left")

      self.code_button = tk.Button(self, text="Agent", command=self.display_a_frame)
      self.code_button.pack(side="left")

      self.code_button = tk.Button(self, text="Algorithm", command=self.display_l_frame)
      self.code_button.pack(side="left")
      # self.code_button = tk.Button(self, text="Code", command=self.display_c_frame)
      # self.code_button.pack(side="left")
      tk.Button(self.sub_frame1, text="Setup", command= self.control.setup).pack(side="left")
      tk.Button(self.sub_frame1, text="Run", command= self.control.run).pack(side="left")
      tk.Button(self.sub_frame1, text="Run Loop", command= lambda: self.control.run_loop(True)).pack(side="left")
    def create_code_frame(self):
      self.read_code = tk.Button(self.sub_frame2, text="read", command=self.get_code)
      self.read_code.pack(side="top")
      self.code = tk.Text(self.sub_frame2,width=685, height=500)
      self.code.pack(side="bottom")

    def display_s_frame(self):
      self.current_frame.pack_forget()
      self.sub_frame1.pack(fill="both", expand=True)
      print(self.simulation_module.turtle_screen.getshapes())
      self.current_frame = self.sub_frame1
    def display_a_frame(self):
      self.current_frame.pack_forget()
      self.sub_frame4.pack(fill="both", expand=True)
      self.setup_agent.updateScreen(self.simulation_module.turtle_screen)
      self.current_frame = self.sub_frame4
    def display_e_frame(self):
      self.current_frame.pack_forget()
      self.sub_frame3.pack(fill="both", expand=True)
      self.current_frame = self.sub_frame3
    def display_l_frame(self):
      self.setup_algorithm.updateUI()
      self.current_frame.pack_forget()
      self.sub_frame2.pack(fill="both", expand=True)
      self.current_frame = self.sub_frame2

    def get_code(self):
      code = self.code.get("1.0","end")
      compl = compile.Compile()
      compl.setSrc(code)

root = tk.Tk()
app = Application(master=root)
app.master.title("AgentSimulationTool")
app.master.geometry('1000x650')
app.mainloop()
