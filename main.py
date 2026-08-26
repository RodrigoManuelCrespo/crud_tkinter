import tkinter as tk
from crud import CRUDFrame


def main():
    root = tk.Tk()
    root.withdraw()  # ocultamos la ventana raíz, usamos solo la del CRUD

    CRUDFrame(root, "Vehículos")

    root.mainloop()


if __name__ == "__main__":
    main()