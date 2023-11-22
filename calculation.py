import math
from tkinter.messagebox import showerror

import numpy as np
import object


def sum_of_rows(matrix):
    result_vector = [[0], [0], [0]]
    if object.proverka(matrix):
        row_sum1 = 1
        row_sum2 = 1
        row_sum3 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0:
                    row_sum1 *= matrix[i][j].get()
                elif i == 1:
                    row_sum2 *= matrix[i][j].get()
                elif i == 2:
                    row_sum3 *= matrix[i][j].get()
        float_matrix = np.array([[float(matrix[i][j].get()) for j in range(len(matrix[0]))] for i in
                                 range(len(matrix))])
        row_sum1 = math.pow(row_sum1, 1 / 3)
        row_sum2 = math.pow(row_sum2, 1 / 3)
        row_sum3 = math.pow(row_sum3, 1 / 3)
        summa = row_sum1 + row_sum2 + row_sum3
        vector1 = row_sum1 / summa
        vector2 = row_sum2 / summa
        vector3 = row_sum3 / summa
        massiv = np.array([[vector1], [vector2], [vector3]])
        for i in range(len(matrix)):
            for j in range(len(massiv[0])):
                for k in range(len(massiv)):
                    result_vector = np.dot(float_matrix, massiv).tolist()
        z1 = 0
        z2 = 0
        z3 = 0
        for i in range(len(result_vector)):
            for j in range(len(result_vector[i])):
                if i == 0:
                    z1 = result_vector[i][j]/ vector1
                elif i == 1:
                    z2 = result_vector[i][j] / vector2
                elif i == 2:
                    z3 = result_vector[i][j] / vector3
        summa2 = 1/3*(z1+z2+z3)
        IS = (summa2 - 3) / (3 - 1)
        print(IS)
        OS = IS/0.58
        print(OS)
        if OS > 0.1:
            showerror(title="Ошибка", message="ОС одной из матриц выше нормативного")
        else:
            print("Значение ОС: "+str(OS))
            return massiv

