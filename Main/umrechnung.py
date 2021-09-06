from berechner import Berechner

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