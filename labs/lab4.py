def derivative(f, x, h):
      return (f(x+h) - f(x-h)) / (2.0*h)  # might want to return a small non-zero if ==0

def eqation(x):
    return x**3 + 8*x - 6    # just a function to show it works

def solve(f, eps):
    x = set()
    for x0 in range(-1000,1000,10):
        try:
            lastX = x0
            nextX = lastX + 10* eps  # "different than lastX so loop starts OK
            while (abs(lastX - nextX) > eps):  # this is how you terminate the loop - note use of abs()
                lastX = nextX
                nextX = lastX - f(nextX)   / derivative(f, lastX, eps)  # update estimate using N-R
            x.add(round(nextX, len(str(eps))-2))
        except ZeroDivisionError:
            pass
    if len(x) != 0:
        return "Рішення: x = " + str(x)
    else:
        return "Рішень немає"
