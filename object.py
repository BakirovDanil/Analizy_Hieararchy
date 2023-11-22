from tkinter import ttk
from abc import ABC
from tkinter.messagebox import showerror


def on_key_press(event):
    if event.char.lower() not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                                  '\x08']:
        return "break"


def proverka(m):
    found_invalid_value = False
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i != j and m[i][j].get() > 9:
                found_invalid_value = True
                m[i][j].set(0)

    if found_invalid_value:
        showerror(title="Ошибка", message="Введенные данные некорректны. Одно из значений превышает 9")
        for i in range(len(m)):
            for j in range(len(m[i])):
                if i != j:
                    m[i][j].set(0)
        return False
    else:
        return True


def Raschet(m):
    y = 0
    summa = 0
    if proverka(m):
        for i in range(len(m)):
            print()


class Figure(ABC):
    def Sozdanie(self, window):
        pass


class Label(Figure):
    def Sozdanie(self, window):
        crit1h = ttk.Label(text="Критерий 1")
        crit2h = ttk.Label(text="Критерий 2")
        crit3h = ttk.Label(text="Критерий 3")
        crit1v = ttk.Label(text="Критерий 1")
        crit2v = ttk.Label(text="Критерий 2")
        crit3v = ttk.Label(text="Критерий 3")
        crit1h.place(x=25, y=40)
        crit2h.place(x=25, y=85)
        crit3h.place(x=25, y=130)
        crit1v.place(x=110, y=20)
        crit2v.place(x=190, y=20)
        crit3v.place(x=270, y=20)


class Matrix0(Figure):
    def __init__(self, matrix_1_1, matrix_1_2, matrix_1_3, matrix_2_1, matrix_2_2, matrix_2_3, matrix_3_1, matrix_3_2,
                 matrix_3_3):
        self.matrix_1_1 = matrix_1_1
        self.matrix_1_2 = matrix_1_2
        self.matrix_1_3 = matrix_1_3
        self.matrix_2_1 = matrix_2_1
        self.matrix_2_2 = matrix_2_2
        self.matrix_2_3 = matrix_2_3
        self.matrix_3_1 = matrix_3_1
        self.matrix_3_2 = matrix_3_2
        self.matrix_3_3 = matrix_3_3

    def Sozdanie(self, window):
        m11 = ttk.Entry(width=5, textvariable=self.matrix_1_1, state="readonly")
        m12 = ttk.Entry(width=5, textvariable=self.matrix_1_2)
        m13 = ttk.Entry(width=5, textvariable=self.matrix_1_3)
        m21 = ttk.Entry(width=5, textvariable=self.matrix_2_1, state="readonly")
        m22 = ttk.Entry(width=5, textvariable=self.matrix_2_2, state="readonly")
        m23 = ttk.Entry(width=5, textvariable=self.matrix_2_3)
        m31 = ttk.Entry(width=5, textvariable=self.matrix_3_1, state="readonly")
        m32 = ttk.Entry(width=5, textvariable=self.matrix_3_2, state="readonly")
        m33 = ttk.Entry(width=5, textvariable=self.matrix_3_3, state="readonly")
        matrix0 = [m11, m12, m13, m21, m22, m23, m31, m32, m33]
        for i in matrix0:
            i.bind("<Key>", on_key_press)
        m11.place(x=110, y=40)
        m12.place(x=190, y=40)
        m13.place(x=270, y=40)
        m21.place(x=110, y=85)
        m22.place(x=190, y=85)
        m23.place(x=270, y=85)
        m31.place(x=110, y=130)
        m32.place(x=190, y=130)
        m33.place(x=270, y=130)
