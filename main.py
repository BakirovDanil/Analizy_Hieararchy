from tkinter import *
from tkinter import ttk

import object

Frame = Tk()
# Значения для первой матрицы (по критериям)
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

# значения для второй матрицы (по альтернативам и первому критерию)
matrix1_1_1 = IntVar()
matrix1_1_1.set(1)
matrix1_1_2 = IntVar()
matrix1_1_3 = IntVar()
matrix1_2_1 = IntVar()
matrix1_2_2 = IntVar()
matrix1_2_2.set(1)
matrix1_2_3 = IntVar()
matrix1_3_1 = IntVar()
matrix1_3_2 = IntVar()
matrix1_3_3 = IntVar()
matrix1_3_3.set(1)
matrix_1 = [[matrix1_1_1, matrix1_1_2, matrix1_1_3],
            [matrix1_2_1, matrix1_2_2, matrix1_2_3],
            [matrix1_3_1, matrix1_3_2, matrix1_3_3]]

# значения для третьей матрицы (по альтернативам и второму критерию)
matrix2_1_1 = IntVar()
matrix2_1_1.set(1)
matrix2_1_2 = IntVar()
matrix2_1_3 = IntVar()
matrix2_2_1 = IntVar()
matrix2_2_2 = IntVar()
matrix2_2_2.set(1)
matrix2_2_3 = IntVar()
matrix2_3_1 = IntVar()
matrix2_3_2 = IntVar()
matrix2_3_3 = IntVar()
matrix2_3_3.set(1)
matrix_2 = [[matrix2_1_1, matrix2_1_2, matrix2_1_3],
            [matrix2_2_1, matrix2_2_2, matrix2_2_3],
            [matrix2_3_1, matrix2_3_2, matrix2_3_3]]

# значения для четвертой матрицы (по альтернативам и третьему критерию)
matrix3_1_1 = IntVar()
matrix3_1_1.set(1)
matrix3_1_2 = IntVar()
matrix3_1_3 = IntVar()
matrix3_2_1 = IntVar()
matrix3_2_2 = IntVar()
matrix3_2_2.set(1)
matrix3_2_3 = IntVar()
matrix3_3_1 = IntVar()
matrix3_3_2 = IntVar()
matrix3_3_3 = IntVar()
matrix3_3_3.set(1)
matrix_3 = [[matrix3_1_1, matrix3_1_2, matrix3_1_3],
            [matrix3_2_1, matrix3_2_2, matrix3_2_3],
            [matrix3_3_1, matrix3_3_2, matrix3_3_3]]


def Maths():
    object.Raschet(matrix_0)


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
button1 = ttk.Button(text="Заполнить матрицы", command=Maths)
button1.place(x=570, y=25)
MainForm(Frame)
