import tkinter as tk
from tkinter.constants import LEFT, NONE
# import main

class Oberflaeche(tk.Frame):
    def __init__(self, master = NONE):
        super().__init__(master)
        self.master = master
        master.title("Temperatur Umwandler")
        master.maxsize(1000,400)
        master.minsize(200,100)
        self.pack()
        self.create_widgets()
    


    def create_widgets(self):
        EinheitenListe = [
            ("Celsius", "Celsius"),
            ("Fahrenheit", "Fahrenheit"),
            ("Kelvin", "Kelvin")
        ]
        text1 = tk.Label(
            self.master, text= "Wählen Sie Eingabe- und Ausgabe-Einheit aus", font = "Times" 
        )
        text1.pack(side = "top")

        variable = tk.StringVar(self)
        variable.set(EinheitenListe[0])

        opt = tk.OptionMenu(self, variable, *EinheitenListe)
        opt.config(width=90, font=("helvetica", 12))
        opt.pack()

        self.hi_there = tk.Button(self, text = "Hallo", command=self.say_hi)
        self.hi_there.pack(side="left")

        self.quit = tk.Button(
            self, text="Quit", fg = "red", command = self.master.destroy
            )
        self.quit.pack(side="bottom")
        

    def say_hi(self):
        print("Hallo zusammen")

