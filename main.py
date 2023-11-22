from tkinter import *
from tkinter import ttk

import object

Frame = Tk()
# Значения для первой матрицы
matrix_1_1 = IntVar().set(1)
matrix_1_2 = IntVar()
matrix_1_3 = IntVar()
matrix_2_1 = IntVar().set(matrix_1_2.get())
matrix_2_2 = IntVar().set(1)
matrix_2_3 = IntVar()
matrix_3_1 = IntVar().set(matrix_1_3.get())
matrix_3_2 = IntVar().set(matrix_2_3.get())
matrix_3_3 = IntVar().set(1)
matrix_0 = [[matrix_1_1, matrix_1_2, matrix_1_3], [matrix_2_1, matrix_2_2, matrix_2_3],
            [matrix_3_1, matrix_3_2, matrix_3_3]]


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
    window.mainloop()


MainForm(Frame)
