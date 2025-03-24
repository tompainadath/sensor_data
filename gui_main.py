import tkinter as tk
from tkinter import ttk
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RootGUI:
    def __init__(self):
        self.root = tk.Tk()
        
        self.root.title("Ambient Light Sensor")
        self.root.geometry("500x500")
        
        self.bg = "#1dad91"
        self.fg = 'white'
        self.root.config(bg = self.bg)
    
class ComGUI():
    def __init__(self, main_root, serial_com):
        self.root = main_root.root
        self.serial_mod = serial_com
        self.bg = main_root.bg
        self.fg = main_root.fg

        self.com_frame = tk.LabelFrame(self.root, text = "COM manager", background = self.bg, foreground = self.fg,  padx = 5, pady = 5)
        self.com_label = ttk.Label(self.com_frame, text = "Available Port(s): ", background = self.bg, foreground = self.fg, anchor = "w")
        self.baud_label = ttk.Label(self.com_frame, text = "Baud Rate: ", background = self.bg, foreground = self.fg, anchor = "w")
        self.connectbutton = ttk.Button(self.com_frame, text= 'Connect', command = self.connectClicked, state = "disabled")

        
        self.comOptionsMenu()
        self.baudOptionsMenu()
        self.publish()
        
    
    def comOptionsMenu(self):
        self.com_optionsList = self.serial_mod.portslist
        self.comport_selected = tk.StringVar(self.root)
        self.comport_selected.set("-")
        self.comport_menu = ttk.OptionMenu(self.com_frame, self.comport_selected, "-",  *self.com_optionsList, command = self.optionsSelected)
    
    def baudOptionsMenu(self):
        self.baud_optionsList = ["-", "9600", "115200"]
        self.baudrate_selected = tk.StringVar(self.root)
        self.baudrate_selected.set(self.baud_optionsList[0])
        self.baudrate_menu = ttk.OptionMenu(self.com_frame, self.baudrate_selected, self.baud_optionsList[0],  *self.baud_optionsList, command = self.optionsSelected)
        
    
    def optionsSelected(self, choice):
        print(self.comport_selected.get())
        print(self.baudrate_selected.get())
        if (self.comport_selected.get() or self.baudrate_selected.get()) == "-":
            self.connectbutton.config(state = 'disabled')
            
        else:
            self.connectbutton.config(state = 'normal')
            self.connectbutton.config(text = 'Connect')

    def connectClicked(self):
        if self.connectbutton["text"] == "Connect":
            self.connectbutton.config(text = 'Disconnect')
            try:
                self.serial_mod.serialConnect(self.comport_selected.get(), self.baudrate_selected.get())
            except:
                print(Exception)
        
        else:
            self.connectbutton.config(text = 'Connect')

    def publish(self):
        self.com_frame.grid(row = 0, column = 0, sticky='w', padx = 5, pady = 5)
        self.com_label.grid(row = 0, column = 0, sticky='w', pady= 5)
        self.comport_menu.grid(row = 0, column= 1)
        self.baud_label.grid(row = 0, column = 2, sticky='w')
        self.baudrate_menu.grid(row = 0, column= 3)
        self.connectbutton.grid(row = 0, column  = 4, padx = 5)

        

class DataGUI:
    def __init__(self, main_root, serial_com, data_module):
        self.root = main_root.root
        self.serial_mod = serial_com
        self.data_mod = data_module
        self.bg = main_root.bg
        self.fg = main_root.fg
        self.data_frame = tk.LabelFrame(self.root, text = "Data manager", background = self.bg, foreground = self.fg,  padx = 5, pady = 5)
        self.startStopbutton = ttk.Button(self.data_frame, text= "Start", command = self.startStopClicked)
        self.clearbutton = ttk.Button(self.data_frame, text= "Clear", command = self.clearClicked)

        x_values = [1, 2, 3, 4, 5]
        y_values = [2, 4, 1, 3, 5]

        fig, ax = plt.subplots()
        ax.plot(x_values, y_values)
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title("Sample Line Graph")
        self.canvas = FigureCanvasTkAgg(fig, master=self.data_frame)
        self.canvas_widget = self.canvas.get_tk_widget()


        self.publish()
    def startStopClicked(self):
        if self.startStopbutton["text"] == "Start":
            self.startStopbutton["text"] = "Stop"
            self.thread = threading.Thread(target = self.data_mod.startDataCollection)
            self.thread.start()
            
        else:
            self.startStopbutton["text"] = "Start"

    def clearClicked(self):
        pass

    def publish(self):
        self.data_frame.grid(row = 1, column = 0, sticky = 'w', padx = 5, pady = 5)
        self.startStopbutton.grid(row = 0, column = 0, sticky='w', pady= 5, padx = 5)
        self.clearbutton.grid(row = 0, column = 1, sticky='w', pady= 5, padx = 5)
        self.canvas_widget.grid(row = 1, column = 0, sticky='w', pady= 5, padx = 5)
        self.canvas.draw()

        

if __name__ == 'main':
    RootGUI()
    ComGUI()
    