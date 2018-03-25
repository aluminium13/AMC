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
    return t

def getMatrix(text):
    return np.matrix(text)
    

# print(seidel([[1, -2],[0.5, -1]], [1, 1], 0.01)
A = [[6.1, 0.7, -0.05], [-1.3, -2.05, 0.87], [2.5, -3.12, -5.03]]
B = [6.97, 0.1, 2.04]
