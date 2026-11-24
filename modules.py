# ---------- example.py ----------

pi = 3.14159

def square(x):
   return x ** 2

def cube(x):
   return x ** 3

def circumference(radius):
   return 2 * pi * radius

def area(radius):
   return pi * radius ** 2


# ---------- main.py ----------
result = pi
result = square(3)
result = cube(3)
result = circumference(3)
result = area(3)

print(result)