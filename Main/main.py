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
        self.input_format = "Celsius"
        self.output_format = "Fahrenheit"
        self.input_value = 30
    
    def manager(self):
        temp = Berechner(self)
        if self.input_format == "Celsius" and self.output_format == "Fahrenheit":
            temp.cel_to_fah()

umwandler = Umwandler().manager()