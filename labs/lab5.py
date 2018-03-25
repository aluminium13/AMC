from math import sqrt
import numpy as np
from numpy.linalg import solve
from functools import wraps

def solver(func):
    @wraps(func)
    def changer(A, b, eps):
        return solve(A, b)
    return changer

@solver
def seidel(A, b, eps):
    n = len(A)
    x = [.0 for i in range(n)]

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new

    return x

def outputResult(x):
    t = ""
    v = []
    for i in x:
        v.append(str(i))
    cut = len(min(v, key=len))
    for i in range(len(x)):
        t += "x" + str(i+1) + " = " + str(x[i])[:cut] + "\n"
    return "Розв'язки системи: \n" + t

def getMatrix(text):
    A = np.matrix(text)
    return A.tolist()

def outputMatrix(A, B):
    #a = '\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in A])
    a = ""
    for i in range(len(B)):
        for j in range(len(B)):
            a += ''.join([ '{:4}'.format(str(A[i][j])) + '*x' + str(j+1) + " + "])
        a = a[:-3] + " = " + str(B[i]) + "\n"
    return "Задана система рівнянь: \n" + a

    
# print(seidel([[1, -2],[0.5, -1]], [1, 1], 0.01)
A = [[6.1, 0.7, -0.05], [-1.3, -2.05, 0.87], [2.5, -3.12, -5.03]]
B = [6.97, 0.1, 2.04]