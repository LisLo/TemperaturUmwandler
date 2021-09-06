class Berechner():
    def __init__(self, input):
        self.input_format = input.input_format
        self.output_format = input.output_format
        self.value = input.input_value
        print(input.input_value)
    
    def cel_to_fah(self): 
        if self.value >= -273.15:
            self.result = self.value * 9/5 + 32
        else:
            print("Fehler bei der Temperatureingabe")
            exit()

    def cel_to_kel(self):
        if self.value >= -273.15:
            self.result = self.value + 273.15
        else:
            print("Fehler bei der Temperatureingabe")
            exit()
    
    def kel_to_cel(self):
        if self.value >= 0.0:
            self.result = self.value - 273.15
        else:
            print("Fehler bei der Temperatureingabe")
            exit()

    def kel_to_fah(self):
        if self.value >= 0.0:
            self.result = (self.value - 273.15) * 9/5 + 32
        else:
            print("Fehler bei der Temperatureingabe")
            exit()

    def fah_to_cel(self):
        if self.value >= -459.67:
            self.result = (self.value - 32) * 5/9
        else:
            print("Fehler bei der Temperatureingabe")
            exit()

    def fah_to_kel(self):
        if self.value >= -459.67:
            self.result = (self.value - 32) * 5/9 + 273.15
        else:
            print("Fehler bei der Temperatureingabe")
            exit()