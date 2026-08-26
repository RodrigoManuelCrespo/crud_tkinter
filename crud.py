import tkinter as tk


class CRUDFrame(tk.Toplevel):
    def __init__(self, master, entity_name: str):
        super().__init__(master)
        self.entity_name = entity_name
        self.title(f"CRUD - {entity_name}")
        self.geometry("400x300")