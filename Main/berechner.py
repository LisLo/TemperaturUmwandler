class Berechner():
    def __init__(self, input):
        self.input_format = input.input_format
        self.output_format = input.output_format
        self.value = input.input_value
    
    def cel_to_fah(self): 
        self.result = self.value * 9/5 + 32

    def cel_to_kel(self):
        self.result = self.value + 273.15
    
    def kel_to_cel(self):
        self.result = self.value - 273.15

    def kel_to_fah(self):
        self.result = (self.value - 273.15) * 9/5 + 32

    def fah_to_cel(self):
        self.result = (self.value - 32) * 5/9

    def fah_to_kel(self):
        self.result = (self.value - 32) * 5/9 + 273.15