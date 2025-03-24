import numpy as np
import matplotlib.pyplot as plt

class DataManager:
    def __init__(self, serial_com):
        self.serial_mod = serial_com
        pass
    
    def startDataCollection(self):
        while True:
            print(self.serial_mod.ser.readline())