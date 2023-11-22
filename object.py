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
            if m[i][j].get() > 9 or m[i][j].get() == 0:
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
        # Размещение текстовых полей критерий по вертикали
        crit1h = ttk.Label(text="Критерий 1")
        crit2h = ttk.Label(text="Критерий 2")
        crit3h = ttk.Label(text="Критерий 3")
        # Размещение текстовых полей критерий по горизонтали
        crit1v = ttk.Label(text="Критерий 1")
        crit2v = ttk.Label(text="Критерий 2")
        crit3v = ttk.Label(text="Критерий 3")
        # Размещение текстовых полей критерий по вертикали
        alt11h = ttk.Label(text="Альтернатива 1")
        alt12h = ttk.Label(text="Альтернатива 2")
        alt13h = ttk.Label(text="Альтернатива 3")
        # Размещение текстовых полей критерий по горизонтали
        alt11v = ttk.Label(text="Альтер. 1")
        alt12v = ttk.Label(text="Альтер. 2")
        alt13v = ttk.Label(text="Альтер. 3")
        # Размещение текстовых полей критерий по вертикали
        alt21h = ttk.Label(text="Альтернатива 1")
        alt22h = ttk.Label(text="Альтернатива 2")
        alt23h = ttk.Label(text="Альтернатива 3")
        # Размещение текстовых полей критерий по горизонтали
        alt21v = ttk.Label(text="Альтер. 1")
        alt22v = ttk.Label(text="Альтер. 2")
        alt23v = ttk.Label(text="Альтер. 3")
        # Размещение текстовых полей критерий по вертикали
        alt31h = ttk.Label(text="Альтернатива 1")
        alt32h = ttk.Label(text="Альтернатива 2")
        alt33h = ttk.Label(text="Альтернатива 3")
        # Размещение текстовых полей критерий по горизонтали
        alt31v = ttk.Label(text="Альтер. 1")
        alt32v = ttk.Label(text="Альтер. 2")
        alt33v = ttk.Label(text="Альтер. 3")
        #
        crit1h.place(x=25, y=40)
        crit2h.place(x=25, y=85)
        crit3h.place(x=25, y=130)
        #
        crit1v.place(x=110, y=20)
        crit2v.place(x=190, y=20)
        crit3v.place(x=270, y=20)
        #
        alt11h.place(x=20, y=180)
        alt12h.place(x=20, y=225)
        alt13h.place(x=20, y=270)
        #
        alt11v.place(x=110, y=160)
        alt12v.place(x=190, y=160)
        alt13v.place(x=270, y=160)
        #
        alt21h.place(x=20, y=320)
        alt22h.place(x=20, y=365)
        alt23h.place(x=20, y=410)
        #
        alt21v.place(x=110, y=440)
        alt22v.place(x=190, y=440)
        alt23v.place(x=270, y=440)
        #
        alt31h.place(x=20, y=460)
        alt32h.place(x=20, y=505)
        alt33h.place(x=20, y=550)
        #
        alt31v.place(x=110, y=300)
        alt32v.place(x=190, y=300)
        alt33v.place(x=270, y=300)


class Matrix0(Figure):
    def __init__(self, matrix_1_1, matrix_1_2, matrix_1_3,
                 matrix_2_1, matrix_2_2, matrix_2_3,
                 matrix_3_1, matrix_3_2, matrix_3_3):
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


class Matrix1(Figure):
    def __init__(self, matrix1_1_1, matrix1_1_2, matrix1_1_3,
                 matrix1_2_1, matrix1_2_2, matrix1_2_3,
                 matrix1_3_1, matrix1_3_2, matrix1_3_3):
        self.matrix1_1_1 = matrix1_1_1
        self.matrix1_1_2 = matrix1_1_2
        self.matrix1_1_3 = matrix1_1_3
        self.matrix1_2_1 = matrix1_2_1
        self.matrix1_2_2 = matrix1_2_2
        self.matrix1_2_3 = matrix1_2_3
        self.matrix1_3_1 = matrix1_3_1
        self.matrix1_3_2 = matrix1_3_2
        self.matrix1_3_3 = matrix1_3_3

    def Sozdanie(self, window):
        m111 = ttk.Entry(width=5, textvariable=self.matrix1_1_1, state="readonly")
        m112 = ttk.Entry(width=5, textvariable=self.matrix1_1_2)
        m113 = ttk.Entry(width=5, textvariable=self.matrix1_1_3)
        m121 = ttk.Entry(width=5, textvariable=self.matrix1_2_1, state="readonly")
        m122 = ttk.Entry(width=5, textvariable=self.matrix1_2_2, state="readonly")
        m123 = ttk.Entry(width=5, textvariable=self.matrix1_2_3)
        m131 = ttk.Entry(width=5, textvariable=self.matrix1_3_1, state="readonly")
        m132 = ttk.Entry(width=5, textvariable=self.matrix1_3_2, state="readonly")
        m133 = ttk.Entry(width=5, textvariable=self.matrix1_3_3, state="readonly")
        matrix0 = [m111, m112, m113, m121, m122, m123, m131, m132, m133]
        for i in matrix0:
            i.bind("<Key>", on_key_press)
        m111.place(x=110, y=180)
        m112.place(x=190, y=180)
        m113.place(x=270, y=180)
        m121.place(x=110, y=225)
        m122.place(x=190, y=225)
        m123.place(x=270, y=225)
        m131.place(x=110, y=270)
        m132.place(x=190, y=270)
        m133.place(x=270, y=270)


class Matrix2(Figure):
    def __init__(self, matrix2_1_1, matrix2_1_2, matrix2_1_3,
                 matrix2_2_1, matrix2_2_2, matrix2_2_3,
                 matrix2_3_1, matrix2_3_2, matrix2_3_3):
        self.matrix2_1_1 = matrix2_1_1
        self.matrix2_1_2 = matrix2_1_2
        self.matrix2_1_3 = matrix2_1_3
        self.matrix2_2_1 = matrix2_2_1
        self.matrix2_2_2 = matrix2_2_2
        self.matrix2_2_3 = matrix2_2_3
        self.matrix2_3_1 = matrix2_3_1
        self.matrix2_3_2 = matrix2_3_2
        self.matrix2_3_3 = matrix2_3_3

    def Sozdanie(self, window):
        m211 = ttk.Entry(width=5, textvariable=self.matrix2_1_1, state="readonly")
        m212 = ttk.Entry(width=5, textvariable=self.matrix2_1_2)
        m213 = ttk.Entry(width=5, textvariable=self.matrix2_1_3)
        m221 = ttk.Entry(width=5, textvariable=self.matrix2_2_1, state="readonly")
        m222 = ttk.Entry(width=5, textvariable=self.matrix2_2_2, state="readonly")
        m223 = ttk.Entry(width=5, textvariable=self.matrix2_2_3)
        m231 = ttk.Entry(width=5, textvariable=self.matrix2_3_1, state="readonly")
        m232 = ttk.Entry(width=5, textvariable=self.matrix2_3_2, state="readonly")
        m233 = ttk.Entry(width=5, textvariable=self.matrix2_3_3, state="readonly")
        matrix0 = [m211, m212, m213, m221, m222, m223, m231, m232, m233]
        for i in matrix0:
            i.bind("<Key>", on_key_press)
        m211.place(x=110, y=320)
        m212.place(x=190, y=320)
        m213.place(x=270, y=320)
        m221.place(x=110, y=365)
        m222.place(x=190, y=365)
        m223.place(x=270, y=365)
        m231.place(x=110, y=410)
        m232.place(x=190, y=410)
        m233.place(x=270, y=410)


class Matrix3(Figure):
    def __init__(self, matrix3_1_1, matrix3_1_2, matrix3_1_3,
                 matrix3_2_1, matrix3_2_2, matrix3_2_3,
                 matrix3_3_1, matrix3_3_2, matrix3_3_3):
        self.matrix3_1_1 = matrix3_1_1
        self.matrix3_1_2 = matrix3_1_2
        self.matrix3_1_3 = matrix3_1_3
        self.matrix3_2_1 = matrix3_2_1
        self.matrix3_2_2 = matrix3_2_2
        self.matrix3_2_3 = matrix3_2_3
        self.matrix3_3_1 = matrix3_3_1
        self.matrix3_3_2 = matrix3_3_2
        self.matrix3_3_3 = matrix3_3_3

    def Sozdanie(self, window):
        m311 = ttk.Entry(width=5, textvariable=self.matrix3_1_1, state="readonly")
        m312 = ttk.Entry(width=5, textvariable=self.matrix3_1_2)
        m313 = ttk.Entry(width=5, textvariable=self.matrix3_1_3)
        m321 = ttk.Entry(width=5, textvariable=self.matrix3_2_1, state="readonly")
        m322 = ttk.Entry(width=5, textvariable=self.matrix3_2_2, state="readonly")
        m323 = ttk.Entry(width=5, textvariable=self.matrix3_2_3)
        m331 = ttk.Entry(width=5, textvariable=self.matrix3_3_1, state="readonly")
        m332 = ttk.Entry(width=5, textvariable=self.matrix3_3_2, state="readonly")
        m333 = ttk.Entry(width=5, textvariable=self.matrix3_3_3, state="readonly")
        matrix0 = [m311, m312, m313, m321, m322, m323, m331, m332, m333]
        for i in matrix0:
            i.bind("<Key>", on_key_press)
        m311.place(x=110, y=460)
        m312.place(x=190, y=460)
        m313.place(x=270, y=460)
        m321.place(x=110, y=505)
        m322.place(x=190, y=505)
        m323.place(x=270, y=505)
        m331.place(x=110, y=550)
        m332.place(x=190, y=550)
        m333.place(x=270, y=550)
