import tkinter as tk
from tkinter import messagebox
from turing_machine import TuringMachine

class TuringMachineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Máquina de Turing")

        self.label = tk.Label(master, text="Ingrese la cadena (formato 0^n 1^n):")
        self.label.pack()

        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        self.run_button = tk.Button(master, text="Ejecutar", command=self.run_machine)
        self.run_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def run_machine(self):
        input_string = self.input_entry.get().strip()  # Elimina espacios innecesarios

        # Verifica si la cadena está vacía o contiene caracteres no válidos
        if not input_string or any(char not in '01' for char in input_string):
            messagebox.showerror("Error", "Cadena no válida. Debe contener solo 0s y 1s.")
            return

        # Asegurarse de que la cadena tenga al menos un 0 y un 1
        if input_string.count('0') != input_string.count('1') or input_string.count('0') == 0:
            messagebox.showerror("Error", "La cadena debe tener la misma cantidad de 0s y 1s, y al menos un par (01).")
            return

        # Crear un tape con un espacio en blanco al final
        tape = input_string + ' '
        machine = TuringMachine(tape)
        machine.run()

        if machine.is_accepted():
            result = f"Cadena aceptada: {machine.get_tape().replace(' ', '')}"
        else:
            result = "Cadena no aceptada."
        
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    gui = TuringMachineGUI(root)
    root.mainloop()
