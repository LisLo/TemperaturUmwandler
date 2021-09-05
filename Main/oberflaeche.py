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
        # self.pack()
        self.create_widgets()
    


    def create_widgets(self):
        EinheitenListe = [
            ("Celsius"),
            ("Fahrenheit"),
            ("Kelvin")
        ]
        anweisungs_label = tk.Label(
            self.master, text= "Wählen Sie Eingabe- und Ausgabe-Einheit aus", font = "Times" 
        )
        # anweisungs_label.pack()
        anweisungs_label.grid(row = 0, column = 0, pady = 20)

        text1_label = tk.Label(self.master, text = "Eingabe")
        text1_label.grid(row = 1, column = 0, pady = 20)

        variable1 = tk.StringVar(self)
        variable1.set(EinheitenListe[0])

        text2_label = tk.Label(self.master, text = "Ausgabe")
        text2_label.grid(row = 1, column = 1, pady = 20)

        variable2 = tk.StringVar(self)
        variable2.set(EinheitenListe[0])
        
        opt1 = tk.OptionMenu(self, variable1, *EinheitenListe)
        opt1.config(width=90, font=("helvetica", 12))
        # opt1.pack()
        opt1.grid(row = 2, column = 0)

        opt2 = tk.OptionMenu(self, variable2, *EinheitenListe)
        opt2.config(width=90, font=("helvetica", 12))
        # opt2.pack()
        opt2.grid(row = 2, column = 1)

        self.hi_there = tk.Button(self, text = "Hallo", command=self.say_hi)
        # self.hi_there.pack(side="left")

        self.quit = tk.Button(
            self, text="Quit", fg = "red", command = self.master.destroy
            )
        # self.quit.pack(side="bottom")
        

    def say_hi(self):
        print("Hallo zusammen")



