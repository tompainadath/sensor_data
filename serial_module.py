import serial
import serial.tools.list_ports

class SerialConnection():
    def __init__(self):
        self.ser = serial.Serial()
        self.portslist = self.portsList(self.ser)
    
    def portsList(self, ser):
        return [p.name for p in serial.tools.list_ports.comports()]

    def serialConnect(self, comPort, baudRate):
        self.ser = serial.Serial(port = comPort, baudrate = baudRate)
