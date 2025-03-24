from time import sleep
import threading
import tkinter as tk
from tkinter import ttk
import serial
import time
import matplotlib.pyplot as plt
import numpy as np


serialData = ""





ser = serial.Serial(port="COM5", baudrate= 9600)
root = tk.Tk()
dataString = tk.StringVar()
dataString.set(serialData)
dataLabel = ttk.Label(root, text="")

dataLabel.pack()


    

def sensor_data():
    global serialData
    while True:
        serialData = ser.readline()
        print(serialData)
        """
        fig, ax = plt.subplots()             # Create a figure containing a single Axes.
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
        plt.show() "
        """
        dataLabel.config(text = serialData)

thread = threading.Thread(target = sensor_data)
thread.start()
    
root.mainloop()
