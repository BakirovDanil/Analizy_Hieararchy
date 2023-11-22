from tkinter import ttk
from abc import ABC


class Figure(ABC):
    def Sozdanie(self, window):
        pass


class Label(Figure):
    def Sozdanie(self, window):
        maxCU = ttk.Label(text="Критерий 1")
        minCU = ttk.Label(text="Критерий 2")
        firstCU = ttk.Label(text="Критерий 3")
        maxCU.place(x=25, y=25)
        minCU.place(x=25, y=70)
        firstCU.place(x=25, y=115)
