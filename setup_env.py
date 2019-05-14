from PIL import Image
from turtle import *
from env import *
from tkinter import Entry, Canvas, Button, Label, Listbox, Scrollbar
from tkinter.colorchooser import *
from tkinter.filedialog import Open

class SetupENV():
  def __init__(self, master=None, screen = None):
    ###########################Public ##################################
    self.variable = {}
    self.bgcolor = None
    self.bgpic = None
    self.width = None
    self.height = None
    ###########################################################
    self._pixel_width = 1
    self._pixel_height = 1
    self._width_entry = Entry(master)
    self._width_entry.insert(0,"width")
    self._height_entry = Entry(master)
    self._height_entry.insert(0,"height")
    self._master = master
    # self.screen = screen
    # self.object = Enviroment(screen)
    self.chance_bgcolor(frame=master)
    demo_screen = Canvas(master, width=670, height=520, background='white')
    demo_screen.pack(side="right")
    self._demo_turtle_screen = TurtleScreen(demo_screen)

  def chance_bgcolor(self, frame=None):
    Button(frame, text='Select Background Color', command=self._getColor).place(x=10,y=50)
    Button(frame, text='Select Background Picture', command=self._getPicture).place(x=10,y=100)
    Label(frame, text='Setup Grid: ').place(x=10,y=150)
    self._width_entry.place(x=50, y=180)
    self._height_entry.place(x=50, y=210)
    # Button(frame, text='Setup Map', command=self._getPicture).place(x=10,y=250)
    Label(frame, text='Setup Variable:').place(x=10,y=300)
    Button(frame, text='Set Up', command=self._setup).pack(side="bottom")
    Label(frame, text='Name:').place(x=20,y=330)
    var_name = Entry(self._master, width = 20)
    var_name.place(x=100,y=330)
    Label(frame, text='Default:').place(x=20,y=360)
    default = Entry(self._master, width = 20)
    default.place(x=100,y=360)
    Button(frame, text='Add', command=lambda: self._add_variable(var_name.get(), default.get())).place(x=140,y=390)

  def _getColor(self):
    color = askcolor()
    self._demo_turtle_screen.bgcolor(color[1])
    self.bgpic = None
    self.bgcolor = color[1]
    print(color[1])

  def _getPicture(self):
    self.bgcolor = None
    ftypes = [('Image files', '*.gif *.png *.jpeg'), ('All files', '*')]
    dlg = Open(self._master, filetypes = ftypes)
    fl = dlg.show()
    print(fl)
    if fl != '':
      img = Image.open(fl)
      img = img.resize((670,520), Image.ANTIALIAS)
      img.save(fl)
      self.bgpic = fl
      self._demo_turtle_screen.bgpic(self.bgpic)

  def _setup(self):
    width = self._width_entry.get()
    height = self._height_entry.get()
    # if self.bgcolor:
    #   self.object.setupbgcolor(self.bgcolor)
    # if self.bgpic:
    #   self.object.setupbgpic(self.bgpic)
    if self._is_int(width) and self._is_int(height):
      self.width = int(width)
      self.height = int(height)
    else :
      self.width = 100
      self.height = 100
      # self.object.setupgrid(self.width, self.height)
    self._demo_turtle_screen.mode(mode="world")
    self._demo_turtle_screen.setworldcoordinates(0,0, self.width, self.height)
    self._pixel_width = 670/self.width
    self._pixel_height = 520/self.height
    self._show_grid()
  def _is_int(self, x):
    try:
        x = int(x)
        return True
    except:
        return False

  def _show_grid(self):
    canvas = self._demo_turtle_screen.getcanvas()
    for x in range(self.width):
      canvas.create_line(x*self._pixel_width,-520,x*self._pixel_width,0)
    for y in range(self.height):
      canvas.create_line(0,-y*self._pixel_height,670,-y*self._pixel_height)
    lowx= self._convert_coodinate(0,0)["lowx"]
    lowy= self._convert_coodinate(0,0)["lowy"]
    upx= self._convert_coodinate(self.width,self.height)["upx"]
    upy= self._convert_coodinate(self.width,self.height)["upy"]
    canvas.create_line(lowx, lowy, upx, upy)

  def _convert_coodinate(self, turtlex, turtley):
    canvas_coor = {"lowx": 0, "lowy": 0, "upx":0, "upy": 0}
    canvas_coor["lowx"] = turtlex*self._pixel_width
    canvas_coor["lowy"] = - turtley*self._pixel_height
    canvas_coor["upx"] = (turtlex+1)*self._pixel_width
    canvas_coor["upy"] =  - (turtley+1)*self._pixel_height
    return canvas_coor
  def _add_variable(self, name, default):
    if name != "":
      self.variable[name] = default
    print(self.variable)
    variablelist = Listbox(self._master, width =15, height=5)
    variablelist.place(x=20,y=420)
    scrollbar = Scrollbar(self._master)
    scrollbar.config(command=variablelist.yview)
    scrollbar.place(x=145,y=421, height=90)

    variablelist.config(yscrollcommand=scrollbar.set)
    for x in self.variable:
      variablelist.insert("end", x+" : "+self.variable[x])
