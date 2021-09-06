import tkinter
import os
import sys
# find root dir
root_path = os.path.split((os.path.dirname(__file__)))[0]
# set root 
sys.path.append(root_path)
from Source.oberflaeche import Oberflaeche

root = tkinter.Tk()
flaeche = Oberflaeche(root)
flaeche.mainloop()