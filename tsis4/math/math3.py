import math

n = int(input("number of sides: "))
s = int(input("length of each side: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", area)
