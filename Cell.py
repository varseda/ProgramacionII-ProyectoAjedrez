import tkinter as tk
from tkinter import PhotoImage


class Cell:

    # Atributos
    label = None
    position = []  # Posicion 0 = x, 1 = y
    empty = None

    def __init__(self, frame=None, row=None, column=None):

        self.position.append(row)
        self.position.append(column)

        self.label = tk.Label(frame, borderwidth=0)
        self.label.grid(row=row, column=column)
