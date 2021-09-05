import tkinter as tk

class OptionMenu(tk.Frame): # <-- with Frame

    def __init__(self, container, variable, *options):
        super().__init__(container) # <-- with super()

        var = tk.StringVar()
        var.set(variable)

        # use `self` as parent for widgets inside
        dropdown = tk.OptionMenu(self, var, *options)
        dropdown.pack()


def main():

    EinheitenListe = [
        ("Celsius"),
        ("Fahrenheit"),
        ("Kelvin")
        ]

    root = tk.Tk()

    text1_label = tk.Label(root, text = "Eingabe")
    text1_label.grid(row = 0, column = 0, pady = 20)

    opt1 = OptionMenu(root, EinheitenListe, *EinheitenListe)
    opt1.grid(row = 1, column = 0, pady = 20)

    root.mainloop()

if __name__ == '__main__':
    main()