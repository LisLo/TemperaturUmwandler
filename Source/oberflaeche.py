import tkinter as tk
from tkinter.constants import COMMAND, LEFT, NONE
from Source.umrechnung import Umwandler

class Oberflaeche(tk.Frame):
    def __init__(self, window = NONE):
        super().__init__(window)
        self.window = window
        self.window.title("Temperatur Umwandler")
        self.window.maxsize(1000, 400)
        self.window.minsize(200, 100)
        self.input_format = "Celsius"
        self.output_format = "Fahrenheit"
        self.input_value = 0.0

        self.create_widgets()

    def button_action(self):
        self.input_value = float(self.num1.get())
        ergebnis = Umwandler(self.input_format, self.output_format, self.input_value)
        message = str(ergebnis.ausfuehren())
        self.ergebnis_label.configure(text = message)

    def eingabe_wahl(self, wert):
        self.input_format = wert

    def ausgabe_wahl(self, wert):
        self.output_format = wert

    def create_widgets(self):
        EinheitenListe = [
            ("Celsius"),
            ("Fahrenheit"),
            ("Kelvin")
        ]
        anweisungs_label1 = tk.Label(
            self.window, text = "Wählen Sie Eingabe- und Ausgabe-Einheit aus.", font = "Times"
        )
        anweisungs_label1.grid(row = 0, column = 0, pady = 20)

        beenden_button = tk.Button(self.master, text = "Beenden", command=self.master.quit)
        beenden_button.grid(row = 0, column = 1)

        text1_label = tk.Label(self.window, text = "Eingabe")
        text1_label.grid(row = 1, column = 0, pady = 20)

        input_format = tk.StringVar(self)
        input_format.set(EinheitenListe[0])

        text2_label = tk.Label(self.window, text = "Ausgabe")
        text2_label.grid(row = 1, column = 1, pady = 20)

        output_format = tk.StringVar(self)
        output_format.set(EinheitenListe[1])
        
        opt1_input = tk.OptionMenu(self.window, input_format, *EinheitenListe, command=self.eingabe_wahl)
        opt1_input.config(width=30, font=("helvetica", 12))
        opt1_input.grid(row = 2, column = 0)
        
        opt2_output = tk.OptionMenu(self.window, output_format, *EinheitenListe, command=self.ausgabe_wahl)
        opt2_output.config(width=30, font=("helvetica", 12))
        opt2_output.grid(row = 2, column = 1)

        anweisungs_label2 = tk.Label(
            self.window, text= "Geben Sie eine Temperatur ein.", font = "Times" 
        )
        anweisungs_label2.grid(row = 3, column = 0, pady = 20)

        self.num1 = tk.Entry(self.master, bd = 5, width = 40)
        self.num1.insert(0, "0")
        self.num1.grid(row = 4, column = 0)

        umrechnung_button = tk.Button(self.master, text = "Umrechnen", command=self.button_action)
        umrechnung_button.grid(row = 4, column = 1)

        anweisungs_label3 = tk.Label(
            self.window, text= "Das Ergebnis ist:", font = "Times" 
        )
        anweisungs_label3.grid(row = 5, column = 0, pady = 20)

        self.ergebnis_label = tk.Label(
            self.window, text = "nichts berechnet", font = "Times"
        )
        self.ergebnis_label.grid(row = 5, column = 1, pady = 20)
