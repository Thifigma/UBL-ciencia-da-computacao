import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = ((b**2)-4*a*c)

print("Delta: ", delta)

if delta == 0:
    x1 = ((-b + math.sqrt(delta)) / (2*a))
    print("x: ", x1)
elif delta > 0:
    x1 = ((-b + math.sqrt(delta)) / (2*a))
    x2 = ((-b - math.sqrt(delta)) / (2*a))
    print("x1: ", x1)
    print("x2: ", x2)
else:
    print("Nao há raizes reais!")
