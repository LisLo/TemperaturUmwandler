"""
(1) Umrechnung von Celsius nach Kelvin
(2) Umrechnung von Celsius nach Fahrenheit
(3) Umrechnung von Kelvin nach Celsius
(4) Umrechnung von Kelvin nach Fahrenheit
(5) Umrechnung von Fahrenheit nach Celsius
(6) Umrechnung von Fahrenheit nach Kelvin """

""" Celsius = 5/9 * (Fahrenheit - 32).
Celsius = Kelvin - 273.15.
Die tiefste mögliche Temperatur ist den absoluten Nullpunkt 0K.
"""

from berechner import Berechner

class Umwandler():
    def __init__(self):
        self.input_format = "Fahrenheit"
        self.output_format = "Kelvin"
        self.input_value = 86
        
    
    def ausgabe(self):
        print(self.result)

    def manager(self):
        temp = Berechner(self)
        if self.input_format == "Celsius" and self.output_format == "Fahrenheit":
            # result = temp.cel_to_fah()
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
        self.result = temp.result

umwandler = Umwandler()
umwandler.manager()
umwandler.ausgabe()