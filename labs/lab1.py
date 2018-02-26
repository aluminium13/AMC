from math import sqrt

def linear(message):
    nums = message.split()
    try:
        a = float(nums[0])
        b = float(nums[1])
        c = float(nums[2])
        d = float(nums[3])
    except IndexError:
        return "Ви ввели недостатню кількість цифр"
    except ValueError:
        return "Треба вводити цифри, а не букви! Обережніше!"
    try:
        return "Y1 = " + str((sqrt(a)+b**2)/(sqrt(b)-a**2) + sqrt(a*b/(c*d)))
    except ZeroDivisionError:
        return "Упс. Ділення на нуль. Так не можна! ПЕРЕХРЕСТИСЯ!"
def non_linear(message):
    nums = message.split()
    try:
        a = float(nums[0])
        c = float(nums[1])
        k = float(nums[2])
    except IndexError:
        return "Ви ввели недостатню кількість цифр"
    except ValueError:
        return "Треба вводити цифри, а не букви! Обережніше!"
    if k < 10:
        return  "y = " + str((a + c)**4 + (a - c)**2)
    else:
        return "y =" + str((a - c)**3 + (a + c)**2)
 
def cyclic(message):
    nums = message.split()
    try:
        a = float(nums[0])
        b = float(nums[1])
        p = int(nums[2])
    except IndexError:
        return "Ви ввели недостатню кількість цифр"   
    except ValueError:
        return "Треба вводити цифри, а не букви! Обережніше!"
    s1 = 0
    s2 = 0
    s3 = 0
    for i in range(1, p+1):
        s1 += i**3
        s2 += i**2
        s3 += i
    return "f = " + str(s1*s2*s3*sqrt(a + b))