from tkinter import *
from displayagent import *
from actionagent import *
from sensoragent import *
from tkinter import ttk
from tkinter.filedialog import Open
from PIL import Image, ImageTk
from turtle import *
from behavior import *
import variable as var

class SetupAgent():
  def __init__(self, master=None, screen=None):
    self._currenttype = None
    self.custom_behavior = None
    self._screen = screen
    self._master = master
    self.behavior = "randomRun"
    self.agents = ["New Agent"]
    self.initUI(master)
  def initUI(self, frame):
    frame.columnconfigure(0,weight=4)
    frame.columnconfigure(1,weight=1)
    frame.columnconfigure(2,weight=45)
    frame.rowconfigure(0,weight=1)
    scrollbar = Scrollbar(frame)
    scrollbar.grid(row=0,column=1, sticky="nws")
    self._list = Listbox(frame, width = 30, yscrollcommand=scrollbar.set, selectmode = "single")
    self._list.bind('<<ListboxSelect>>', self.AgentForm)
    self._list.grid(row=0,column=0, sticky="nwse")
    for x in self.agents:
      if x == "New Agent":
        self._list.insert("end", x)
      else :
        self._list.insert("end", x.name)
    self.createform()

  def AgentForm(self, event):
    select_index = self._list.curselection()
    if select_index:
      self._select_index = select_index[0]
      if self._select_index == 0:
        self.showcreateform()
      else :
        agent = self.agents[self._select_index]
        self.showeditform(agent)


  def createform(self):
    self._subframe = Frame(self._master, width=900, height=500)
    ###########################Title#######################################
    self._subframe.title = StringVar()
    Label(self._subframe, textvariable=self._subframe.title, font=("Arial", 20)).place(x=200,y=10)
    self._subframe.title.set("Create Agent")
    ##########################Name Input##################################
    Label(self._subframe, text="Name:").place(x=50, y=80)
    self._subframe.name_input = Entry(self._subframe, width=50)
    self._subframe.name_input.place(x=150, y=80)
    ##########################Type Input##################################
    Label(self._subframe, text="Type:").place(x=50, y=120)
    self._subframe.type_input = ttk.Combobox(self._subframe, values= var.types)
    self._subframe.type_input.place(x=150, y=130)
    self._subframe.type_input.bind("<<ComboboxSelected>>", self.selectType)
    ##########################Shape Input##################################
    shapes = self._screen.getshapes()
    shapes.insert(0, "New Shape")
    self._subframe.shape_label = Label(self._subframe, text="Shape:")
    self._subframe.shape_box = ttk.Combobox(self._subframe, values=shapes)
    self._subframe.shape_box.bind("<<ComboboxSelected>>", self.selectShape)
    self._subframe.shape_width = Entry(self._subframe, width = 10)
    self._subframe.shape_width.insert(0,"width")
    self._subframe.shape_height = Entry(self._subframe, width = 10)
    self._subframe.shape_height.insert(0,"height")
    #############################Behavior Input############################
    self._subframe.behavior_label = Label(self._subframe, text="Behavior:")
    self._subframe.behavior_box = ttk.Combobox(self._subframe, values=Behavior.methods)
    self._subframe.behavior_box.bind("<<ComboboxSelected>>", self.selectbehavior)
    self._subframe.behavior_button = Button(self._subframe, text="Create New Method", command=self.create_custom_behavior)
    ############################# Begin Position ##########################
    self._subframe.begin_pos_label = Label(self._subframe, text="Begin Postition:")
    self._subframe.begin_pos_x = Entry(self._subframe, width = 10)
    self._subframe.begin_pos_x.insert(0,"x")
    self._subframe.begin_pos_y = Entry(self._subframe, width = 10)
    self._subframe.begin_pos_y.insert(0,"y")
    ############################# behin heading ###########################
    self._subframe.begin_heading_label = Label(self._subframe, text="Begin Heading:")
    self._subframe.begin_heading = Entry(self._subframe, width = 20)
    ############################ add method button ##########################
    self.active_methods = ["New Method"]
    self.active_scrollbar = Scrollbar(self._subframe)
    self.active_list = Listbox(self._subframe, width = 60,
      yscrollcommand=self.active_scrollbar.set, selectmode = "single")
    self.active_list.bind('<<ListboxSelect>>', self.select_method)
    for x in self.active_methods:
      if x == "New Method":
        self.active_list.insert("end", x)
      else :
        self.active_list.insert("end", x['name'])
    ###########################custom env input####################################
    self.sensor_label = Label(self._subframe, text="Custom Variable:")
    self.sensor_textbox = Text(self._subframe, width = 40, height=10)
    ##########################Apply button##################################
    self._subframe.button_title = StringVar()
    Button(self._subframe, textvariable=self._subframe.button_title,
      command= self.createNewAgent).place(x=250,y=480)
    self._subframe.button_title.set("Create")

  def showcreateform(self):
    self._subframe.grid(row=0, column = 2)
    self._subframe.name_input.delete(0, "end")
    self._subframe.type_input.configure(state='normal')
    self._subframe.type_input.set('')
    self._subframe.title.set("Create Agent")
    self._subframe.button_title.set("Create")
    self.hideForm()
    print("showcreate")

  def showeditform(self, object):
    self._subframe.title.set(object.name)
    self._subframe.name_input.delete(0, "end")
    self._subframe.name_input.insert(0, object.name)
    self._subframe.type_input.delete(0, "end")
    self._subframe.type_input.insert(0, object.type)
    self._subframe.type_input.configure(state='disabled')
    self.hideForm()
    if object.type == "Display" :
      self.createDisplayAgentForm()
      self._subframe.shape_box.set(object.shape)
      self._subframe.behavior_box.set(object.behavior)
      self._subframe.begin_pos_x.delete(0, "end")
      self._subframe.begin_pos_x.insert(0, object.x)
      self._subframe.begin_pos_y.delete(0, "end")
      self._subframe.begin_pos_y.insert(0, object.y)
      self._subframe.begin_heading.delete(0, "end")
      self._subframe.begin_heading.insert(0, object.heading)
      self.custom_behavior = object.custom_behavior
    elif object.type == "Active" :
      self.showActiveAgentForm()
      self.active_list.delete(0, "end")
      for x in self.active_methods:
        if x == "New Method":
          self.active_list.insert("end", x)
        else :
          self.active_list.insert("end", x['name'])
    elif object.type == "Sensor" :
      self.showSensorAgentForm()
      self.sensor_textbox.delete("1.0", "end")
      self.sensor_textbox.insert("end", object.custom_var)
    print("showedit")
    self._subframe.button_title.set("Update")
    self._subframe.grid(row=0, column = 2)

  def createNewAgent(self):
    name = self._subframe.name_input.get()
    type = self._subframe.type_input.get()
    if type == "Display":
      shape = self._subframe.shape_box.get()
      behavior = self._subframe.behavior_box.get()
      custom_behavior = self.custom_behavior
      x = self._subframe.begin_pos_x.get()
      y = self._subframe.begin_pos_y.get()
      heading = self._subframe.begin_heading.get()
      if name in self._list.get(0, len(self.agents)-1):
        for i in self.agents:
          if i!= "New Agent" and name == i.name  :
            i.update(name, shape, behavior, custom_behavior, x, y,heading)
      else:
        new = DisplayAgent(name, shape, behavior, custom_behavior, x, y,heading)
        self.agents.append(new)
        self._list.insert("end", new.name)
    elif type == "Active":
      if name in self._list.get(0, len(self.agents)-1):
        for i in self.agents:
          if i!= "New Agent" and name == i.name  :
            i.update(name, self.active_methods)
      else:
        new = ActiveAgent(name, self.active_methods)
        self.agents.append(new)
        self._list.insert("end", new.name)
    elif type == "Sensor":
      if name in self._list.get(0, len(self.agents)-1):
        for i in self.agents:
          if i!= "New Agent" and name == i.name  :
            i.update(name, self.sensor_textbox.get("1.0","end"))
      else:
        new = SensorAgent(name, self.sensor_textbox.get("1.0","end"))
        self.agents.append(new)
        self._list.insert("end", new.name)
    self._list.activate(0)
    self.showcreateform()
  def _is_int(self, x):
    try:
        x = int(x)
        return True
    except:
        return False

  def selectShape(self, event):
    shape_name = self._subframe.shape_box.get()
    shape_index = self._subframe.shape_box.current()
    if shape_name == "New Shape":
      self._subframe.behavior_label.place(x=50, y=330)
      self._subframe.behavior_box.place(x=150, y=330)
      self._subframe.behavior_button.place(x=350, y=330)
      self._subframe.begin_pos_label.place(x=50, y=380 )
      self._subframe.begin_pos_x.place(x=150, y=380)
      self._subframe.begin_pos_y.place(x=250, y=380)
      self._subframe.begin_heading_label.place(x=50, y=430)
      self._subframe.begin_heading.place(x=150, y=430)
      Label(self._subframe, text="Shape Name:").place(x=80, y=200)
      self._subframe.shape_name_entry = Entry(self._subframe)
      self._subframe.shape_name_entry.place(x=180, y=200)
      Button(self._subframe, text="Shape Image", command=self.inputImage).place(x=150, y=250)
      self._subframe.shape_image = Label(self._subframe)
      self._subframe.shape_width.place(x=300 ,y=250)
      self._subframe.shape_height.place(x=370 ,y=250)
      Button(self._subframe, text="Add", command= lambda: self.createShape(self._subframe.shape_name_entry.get(), self._shape_image)).place(x=150, y=280)
  def inputImage(self):
    ftypes = [('Image files', '*.gif *.png *.jpeg'), ('All files', '*')]
    dlg = Open(self._master, filetypes = ftypes)
    fl = dlg.show()
    if fl != '':
      photo = Image.open(fl)
      if self._is_int(self._subframe.shape_width.get()) == True:
        photo = photo.resize((int(self._subframe.shape_width.get()),photo.height), Image.ANTIALIAS)
      if self._is_int(self._subframe.shape_height.get()) == True:
        photo = photo.resize((photo.width, int(self._subframe.shape_height.get())), Image.ANTIALIAS)
      photo = ImageTk.PhotoImage(photo)
      self._shape_image = photo
      self._subframe.shape_image.configure(image=photo)
      self._subframe.shape_image.photo = photo

      self._subframe.shape_image.place(x=500, y=250)
  def createShape(self, name, img):
    if name != '':
      new = Shape("image", img)
      self._screen.register_shape(name, new)
      shapes = self._screen.getshapes()
      shapes.insert(0, "New Shape")
      self._subframe.shape_name_entry.delete(0,"end")
      self._subframe.shape_width.delete(0,"end")
      self._subframe.shape_width.insert(0,"width")
      self._subframe.shape_height.delete(0,"end")
      self._subframe.shape_height.insert(0,"height")
      self._subframe.shape_box.configure(values = shapes)
      print(self._screen.getshapes())
  def selectbehavior(self, event):
    self.behavior = self._subframe.behavior_box.get()
  def selectType(self, event):
    type = self._subframe.type_input.get()
    if type == "Display":
      self.hideForm()
      self.createDisplayAgentForm()
    if type == "Active":
      self.hideForm()
      self.showActiveAgentForm()
    if type == "Sensor":
      self.hideForm()
      self.showSensorAgentForm()
  def createDisplayAgentForm(self):
    self._subframe.shape_label.place(x=50, y=160)
    self._subframe.shape_box.place(x=150, y=160)
    self._subframe.behavior_box.place(x=150, y=200)
    self._subframe.behavior_label.place(x=50, y=200)
    self._subframe.behavior_button.place(x=350,y=200)
    self._subframe.begin_pos_label.place(x=50, y=250 )
    self._subframe.begin_pos_x.place(x=150, y=250)
    self._subframe.begin_pos_y.place(x=250, y=250)
    self._subframe.begin_heading_label.place(x=50, y=300)
    self._subframe.begin_heading.place(x=150, y=300)
  def hideForm(self):
    self._subframe.shape_label.place_forget()
    self._subframe.shape_box.place_forget()
    self._subframe.behavior_box.place_forget()
    self._subframe.behavior_label.place_forget()
    self._subframe.behavior_button.place_forget()
    self._subframe.begin_pos_label.place_forget()
    self._subframe.begin_pos_x.place_forget()
    self._subframe.begin_pos_y.place_forget()
    self._subframe.begin_heading_label.place_forget()
    self._subframe.begin_heading.place_forget()
    self.active_scrollbar.place_forget()
    self.active_list.place_forget()
    self.sensor_label.place_forget()
    self.sensor_textbox.place_forget()

  def showActiveAgentForm(self):
    self.active_scrollbar.place(x=550, y=160)
    self.active_list.place(x=50, y=160)

  def showSensorAgentForm(self):
    self.sensor_label.place(x=50, y= 160)
    self.sensor_textbox.place(x=200,y=160)
  def _is_int(self, x):
    try:
        x = int(x)
        return True
    except:
        return False

  def create_custom_behavior(self):
    top = Toplevel()
    top.title("Create Custom Behavior")
    text_box = Text(top, height = 20, width =60)
    if self.custom_behavior != None :
      text_box.insert("end", self.custom_behavior)
    text_box.pack()
    Button(top, text= "Save", command= lambda: self.save_custom_behavior(text_box.get("1.0","end"), top)).pack()

  def save_custom_behavior(self, code, toplevel):
    self.custom_behavior = code
    print(code)
    toplevel.destroy()
  def select_method(self,event):
    selected = self.active_list.curselection()
    if selected :
      index = selected[0]
      if index == 0:
        name = ''
        code = ''
      else:
        name = self.active_methods[index]['name']
        code = self.active_methods[index]['code']
      top = Toplevel()
      top.title("Create Method")
      Label(top, text="Name:").grid(row=0, column=0)
      name_box = Entry(top, width = 60)
      name_box.grid(row=0, column=1)
      name_box.insert("end",name)
      code_box = Text(top, height = 20, width =60)
      code_box.grid(row=1, column =0, columnspan=2)
      code_box.insert("end",code)
      Button(top, text = "Save", command= lambda: self.save_method(name_box.get(),
        code_box.get("1.0","end"), top)).grid(row=2, column = 1)
  def save_method(self, name, code, top):
    new = {'name': name, 'code': code}
    self.active_methods.append(new)
    self.active_list.insert("end", new['name'])
    top.destroy()
