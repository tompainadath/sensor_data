from gui_main import RootGUI, ComGUI, DataGUI
from serial_module import SerialConnection
from data_module import DataManager

main_root = RootGUI()
serialCom = SerialConnection()
dataMod = DataManager(serialCom)
com_gui = ComGUI(main_root, serialCom)
data_gui = DataGUI(main_root, serialCom, dataMod)


main_root.root.mainloop()