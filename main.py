from tkinter import *
from tkinter import ttk

import object

Frame = Tk()
# Значения для первой матрицы
matrix_1_1 = IntVar()
matrix_1_1.set(1)
matrix_1_2 = IntVar()
matrix_1_3 = IntVar()
matrix_2_1 = IntVar()
matrix_2_2 = IntVar()
matrix_2_2.set(1)
matrix_2_3 = IntVar()
matrix_3_1 = IntVar()
matrix_3_2 = IntVar()
matrix_3_3 = IntVar()
matrix_3_3.set(1)
matrix_0 = [[matrix_1_1, matrix_1_2, matrix_1_3],
            [matrix_2_1, matrix_2_2, matrix_2_3],
            [matrix_3_1, matrix_3_2, matrix_3_3]]


def Maths():
    object.Raschet(matrix_0)


def Finish():
    Frame.destroy()
    print("Приложение закрыто")


def MainForm(window):
    window.title("Бакиров Данил, Валеев Марат, Баембитов Гата, Богомолов Валентин. Метод анализа иерархий")
    window.geometry("800x600+400+200")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", Finish)
    label = object.Label()
    label.Sozdanie(window)
    Entry1 = object.Matrix0(matrix_1_1, matrix_1_2, matrix_1_3, matrix_2_1, matrix_2_2, matrix_2_3,
                            matrix_3_1, matrix_3_2, matrix_3_3)
    Entry1.Sozdanie(window)
    window.mainloop()


button = ttk.Button(text="Произвести расчет", command=Maths)
button.place(x=400, y=25)
MainForm(Frame)
