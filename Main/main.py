"""
(1) Umrechnung von Celsius nach Fahrenheit
(2) Umrechnung von Celsius nach Kelvin
(3) Umrechnung von Kelvin nach Celsius
(4) Umrechnung von Kelvin nach Fahrenheit
(5) Umrechnung von Fahrenheit nach Celsius
(6) Umrechnung von Fahrenheit nach Kelvin """

import tkinter
from berechner import Berechner
from oberflaeche import Oberflaeche

class Umwandler():
    def __init__(self):
        self.input_format = "Celsius"
        self.output_format = "Fahrenheit"
        self.input_value = 30
        
    
    def ausgabe(self):
        print(self.result)

    def manager(self):
        temp = Berechner(self)
        if self.input_format == "Celsius" and self.output_format == "Fahrenheit":
            temp.cel_to_fah()    
        elif self.input_format == "Celsius" and self.output_format == "Kelvin":
            temp.cel_to_kel()
        elif self.input_format == "Kelvin" and self.output_format == "Celsius":
            temp.kel_to_cel()
        elif self.input_format == "Kelvin" and self.output_format == "Fahrenheit":
            temp.kel_to_fah() 
        elif self.input_format == "Fahrenheit" and self.output_format == "Celsius":
            temp.fah_to_cel()
        elif self.input_format == "Fahrenheit" and self.output_format == "Kelvin":  
            temp.fah_to_kel()
        else:
            print("Fehler bei der Auswahl der Einheiten")
            exit()
        self.result = temp.result

    def ausfuehren(self):
        umwandler.manager()
        umwandler.ausgabe()

umwandler = Umwandler()
# umwandler.ausfuehren()

root = tkinter.Tk()
flaeche = Oberflaeche(master=root)
flaeche.mainloop()