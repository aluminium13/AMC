from functools import reduce
from operator import mul
from math import cos, e
import numpy as np


def gxi(n: int):
    """
    Function to generate list of x values \n
    :param n: number of interpolation points 
    """
    return [3 + i * 0.3 for i in range(0, n)]


def multiply(a: list):
    """
    Function to multiply all elements in list \n
    :param a: list of elements to multiply
    """
    return reduce(mul, a, 1)


def lagrange(x: float, x_values: list, y_values: list):
    """
    Lagrange interpolation \n
    :param x: a point fuction to count \n
    :param x_values: list of values of x \n
    :param y_values: list of values of f(x) 
    """
    def Ln(j): return multiply(
        (x - x_values[i]) / (x_values[j] - x_values[i]) for i in range(len(x_values)) if i != j)
    return sum([y_values[i] * Ln(i) for i in range(len(y_values))])


def coef(x: list, y: list):
    """
    Function to count coef of newton interpolation \n
    :param x: list of values of x \n
    :param y: list of values of f(x)
    """
    for j in range(1, len(x)):
        for i in range(len(x) - 1, j - 1, -1):
            y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j])
    return list(np.array(y))


def newton(x: float, x_values: list, y_values: list):
    """
    Newton interpolation \n
    :param x: a point fuction to count \n
    :param x_values: list of values of x \n
    :param y_values: list of values of f(x) 
    """
    a = coef(x_values, y_values)
    n = len(a) - 1
    temp = a[n]
    for i in range(n - 1, -1, -1):
        temp = temp * (x - x_values[i]) + a[i]
    return temp


def neville(x: float, x_values: list, y_values: list):
    """
    Eitken interpolation \n
    :param x: a point fuction to count \n
    :param x_values: list of values of x \n
    :param y_values: list of values of f(x) 
    """
    n = len(x_values)
    p = n * [0]
    for k in range(n):
        for i in range(n - k):
            if k == 0:
                p[i] = y_values[i]
            else:
                p[i] = ((x - x_values[i + k]) * p[i] +
                        (x_values[i] - x) * p[i + 1]) / \
                    (x_values[i] - x_values[i + k])
    return p[0]


def getFunc(xi: list, marker: int):
    """
    Generate values of function to-build by the variant \n
    :param xi: list of x values \n
    :param marker: to define what function should be returned
    """
    if marker == 1:
        return list(np.sin(xi))
    elif marker == 2:
        return [cos(x + e**(cos(x))) for x in xi]


def mistake(x: int or float, n: int, marker: int, interp_f: "function"):
    """
    Count the fluff of interpolation function \n
    :param x: a point fuction to count \n
    :param n: number of interpolation points \n
    :param marker: function to explore \n
    :param interp_f: interpolation function to explore
    """
    # сітка розрядності n
    xp = gxi(n)
    fp = getFunc(xp, marker)
    # n + 1
    xpf = gxi(n + 1)
    fpf = getFunc(xpf, marker)
    # n + 2
    xpff = gxi(n + 2)
    fpff = getFunc(xpff, marker)
    # значення поліному степеня n
    p = interp_f(x, xp, fp)
    # n + 1
    p1 = interp_f(x, xpf, fpf)
    # n + 2
    p2 = interp_f(x, xpff, fpff)
    # оцінка похибки інтерполяції
    fl = p - p1
    # оцінка похибки оцінки похибки
    fl_fl = p1 - p2
    # розмитість оцінки похбки
    blur = abs(fl_fl / fl)
    return fl, fl_fl, blur


