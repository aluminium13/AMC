def F(x):
    return x**3 + 8*x-6
 
#производная
def F1(x):
    return 3*(x**2) + 8
 
def Method(a,b,eps):
    try:
        x0=(a+b)/2
        xn=F(x0)
        xn1=xn-F(xn)/F1(xn)
        while abs(xn1-xn)>eps:
            xn=xn1 
            xn1=xn-F(xn)/F1(xn)
        return xn1
    except ValueError:
        return "Value not invalidate"

print(Method(0,1,10**(-8)))