from tkinter import *
from tkinter import ttk

import numpy as np

import calculation
import object

Frame = Tk()
# Значения для первой матрицы (по критериям)
matrix_1_1 = DoubleVar()
matrix_1_1.set(1)
matrix_1_2 = DoubleVar()
matrix_1_3 = DoubleVar()
matrix_2_1 = DoubleVar()
matrix_2_2 = DoubleVar()
matrix_2_2.set(1)
matrix_2_3 = DoubleVar()
matrix_3_1 = DoubleVar()
matrix_3_2 = DoubleVar()
matrix_3_3 = DoubleVar()
matrix_3_3.set(1)
matrix_0 = [[matrix_1_1, matrix_1_2, matrix_1_3],
            [matrix_2_1, matrix_2_2, matrix_2_3],
            [matrix_3_1, matrix_3_2, matrix_3_3]]

# значения для второй матрицы (по альтернативам и первому критерию)
matrix1_1_1 = DoubleVar()
matrix1_1_1.set(1)
matrix1_1_2 = DoubleVar()
matrix1_1_3 = DoubleVar()
matrix1_2_1 = DoubleVar()
matrix1_2_2 = DoubleVar()
matrix1_2_2.set(1)
matrix1_2_3 = DoubleVar()
matrix1_3_1 = DoubleVar()
matrix1_3_2 = DoubleVar()
matrix1_3_3 = DoubleVar()
matrix1_3_3.set(1)
matrix_1 = [[matrix1_1_1, matrix1_1_2, matrix1_1_3],
            [matrix1_2_1, matrix1_2_2, matrix1_2_3],
            [matrix1_3_1, matrix1_3_2, matrix1_3_3]]

# значения для третьей матрицы (по альтернативам и второму критерию)
matrix2_1_1 = DoubleVar()
matrix2_1_1.set(1)
matrix2_1_2 = DoubleVar()
matrix2_1_3 = DoubleVar()
matrix2_2_1 = DoubleVar()
matrix2_2_2 = DoubleVar()
matrix2_2_2.set(1)
matrix2_2_3 = IntVar()
matrix2_3_1 = DoubleVar()
matrix2_3_2 = DoubleVar()
matrix2_3_3 = DoubleVar()
matrix2_3_3.set(1)
matrix_2 = [[matrix2_1_1, matrix2_1_2, matrix2_1_3],
            [matrix2_2_1, matrix2_2_2, matrix2_2_3],
            [matrix2_3_1, matrix2_3_2, matrix2_3_3]]

# значения для четвертой матрицы (по альтернативам и третьему критерию)
matrix3_1_1 = DoubleVar()
matrix3_1_1.set(1)
matrix3_1_2 = DoubleVar()
matrix3_1_3 = DoubleVar()
matrix3_2_1 = DoubleVar()
matrix3_2_2 = DoubleVar()
matrix3_2_2.set(1)
matrix3_2_3 = DoubleVar()
matrix3_3_1 = DoubleVar()
matrix3_3_2 = DoubleVar()
matrix3_3_3 = DoubleVar()
matrix3_3_3.set(1)
matrix_3 = [[matrix3_1_1, matrix3_1_2, matrix3_1_3],
            [matrix3_2_1, matrix3_2_2, matrix3_2_3],
            [matrix3_3_1, matrix3_3_2, matrix3_3_3]]


def Zapolnenie():
    matrix_2_1.set(1 / matrix_1_2.get())
    matrix_3_1.set(1 / matrix_1_3.get())
    matrix_3_2.set(1 / matrix_2_3.get())
    #
    matrix1_2_1.set(1 / matrix1_1_2.get())
    matrix1_3_1.set(1 / matrix1_1_3.get())
    matrix1_3_2.set(1 / matrix1_2_3.get())
    #
    matrix2_2_1.set(1 / matrix2_1_2.get())
    matrix2_3_1.set(1 / matrix2_1_3.get())
    matrix2_3_2.set(1 / matrix2_2_3.get())
    #
    matrix3_2_1.set(1 / matrix3_1_2.get())
    matrix3_3_1.set(1 / matrix3_1_3.get())
    matrix3_3_2.set(1 / matrix3_2_3.get())


def Maths():
    massiv1 = calculation.sum_of_rows(matrix_0)
    massiv2 = calculation.sum_of_rows(matrix_1)
    massiv3 = calculation.sum_of_rows(matrix_2)
    massiv4 = calculation.sum_of_rows(matrix_3)
    massiv_xx = np.hstack((massiv2, massiv3, massiv4))
    massiv_xx = np.dot(massiv_xx, massiv1)
    print("Матрица приоритетов это: ")
    print(massiv_xx)



def Finish():
    Frame.destroy()
    print("Приложение закрыто")


def MainForm(window):
    window.title("Бакиров Данил, Валеев Марат, Баембитов Гата, Богомолов Валентин. Метод анализа иерархий")
    window.geometry("800x750+400+200")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", Finish)
    label = object.Label()
    label.Sozdanie(window)
    #
    Entry1 = object.Matrix0(matrix_1_1, matrix_1_2, matrix_1_3,
                            matrix_2_1, matrix_2_2, matrix_2_3,
                            matrix_3_1, matrix_3_2, matrix_3_3)
    Entry1.Sozdanie(window)
    #
    Entry2 = object.Matrix1(matrix1_1_1, matrix1_1_2, matrix1_1_3,
                            matrix1_2_1, matrix1_2_2, matrix1_2_3,
                            matrix1_3_1, matrix1_3_2, matrix1_3_3)
    Entry2.Sozdanie(window)
    #
    Entry3 = object.Matrix2(matrix2_1_1, matrix2_1_2, matrix2_1_3,
                            matrix2_2_1, matrix2_2_2, matrix2_2_3,
                            matrix2_3_1, matrix2_3_2, matrix2_3_3)
    Entry3.Sozdanie(window)
    #
    Entry4 = object.Matrix3(matrix3_1_1, matrix3_1_2, matrix3_1_3,
                            matrix3_2_1, matrix3_2_2, matrix3_2_3,
                            matrix3_3_1, matrix3_3_2, matrix3_3_3)
    Entry4.Sozdanie(window)
    window.mainloop()


button = ttk.Button(text="Произвести расчет", command=Maths)
button.place(x=400, y=25)
button1 = ttk.Button(text="Заполнить матрицы", command=Zapolnenie)
button1.place(x=570, y=25)
MainForm(Frame)
