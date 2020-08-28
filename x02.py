from math import sqrt, pow
print("ax^2 + bx + c = 0")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
D = pow(b, 2) - 4 * a * c
def get_x(a, b, c):
    if D > 0:
        if "{:g}".format(sqrt(D)).isdecimal():
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            return "x = {:g}, {:g}".format(x1, x2)
        else:
            x1 = "({:g} + √{:g}) / {:g}".format(-b, D, 2 * a)
            x2 = "({:g} - √{:g}) / {:g}".format(-b, D, 2 * a)
            return f"x = {x1}, {x2}"
    elif D == 0:
        x = -b / (2 * a)
        return "x = {:g} (중근)".format(x)
    else:
        if "{:g}".format(sqrt(-D)).isdecimal():
            x1 = "({:g} + {:g}i) / {:g}".format(-b, sqrt(-D), 2 * a)
            x2 = "({:g} - {:g}i) / {:g}".format(-b, sqrt(-D), 2 * a)
            return f"x = {x1}, {x2}"
        else:
            x1 = "({:g} + √{:g}i) / {:g}".format(-b, -D, 2 * a)
            x2 = "({:g} - √{:g}i) / {:g}".format(-b, -D, 2 * a)
            return f"x = {x1}, {x2}"
print("D = {:g}".format(D))
print(get_x(a, b, c))