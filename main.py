import tkinter as tk
from gui import TuringMachineGUI

def main():
    root = tk.Tk()
    app = TuringMachineGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
