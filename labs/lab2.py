from random import randint, shuffle,  choices, sample
import time
from matplotlib import pyplot
from os import getcwd

cwd = getcwd()


def fast_bubble(m):
    t1 = time.time()
    time.sleep(0.00002)
    n = len(m)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if m[i - 1] > m[i]:
                m[i - 1], m[i] = m[i], m[i - 1]
                swapped = True
        n -= 1
    t2 = time.time()
    time.sleep(0.00002)
    with open(cwd + '\\labs\\lab2\\sorted.txt', 'w') as file:
        file.write(str(m))
    return m, t2 - t1


def from_message(message):
    message = message.split()
    m = []
    try:
        for i in message:
            m.append(int(i))
    except ValueError:
        return "Треба вводити цифри, а не букви! Обережніше!"
    t = fast_bubble(m)
    return "Відсортований масив: " + str(t[0]) + "\n Час виконання: " + str(t[1])


def random_generation(n):
    m = sample(range(1, 2 * n), n)
    with open(cwd + '\\labs\\lab2\\notsorted.txt', 'w') as file:
        file.write(str(m))
    return str(m), fast_bubble(m)


def random_time(n):
    m = sample(range(1, 2 * n), n)
    return str(fast_bubble(m)[1])


def get_graph_for_sort():
    t = []
    for i in range(1, 3001, 100):
        t.append(fast_bubble(choices(range(i * 2), k=i))[1])
    pyplot.plot(range(1, 31), t)
    pyplot.savefig(cwd + r"\labs\lab2\Practice2.png")


def get_graph_for_theory():
    t = []
    for i in range(1, 21):
        t.append(i**2)
    pyplot.plot(range(1, 21), t)
    pyplot.savefig(cwd + r"\labs\lab2\Theory.png")
