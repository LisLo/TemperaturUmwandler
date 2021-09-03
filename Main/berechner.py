class Berechner():
    def __init__(self, input):
        self.input_format = input.input_format
        self.output_format = input.output_format
        self.value = input.input_value
    
    def cel_to_fah(self):
        print(self.value)