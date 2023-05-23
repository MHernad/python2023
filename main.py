import math

w = int(input("width: "))
h = int(input("height: "))
grid = []

for i in range(h):
    grid.append([])

for i in range(w):
    for j in range(h):
        grid[j].append(".")

for i in range(h):
    print("{}  {}".format(h - i, grid[i]))


def calcular_pendiente(px1, py1, px2, py2):
    if (px2 - px1) == 0:
        return "Pendiente indefinida"
    return (py2 - py1) / (px2 - px1)


pxA = int(input("coordenada x del punto ")) - 1
pyA = int(input("coordenada y del punto "))

pxB = int(input("coordenada x del punto ")) - 1
pyB = int(input("coordenada y del punto "))

pxC = int(input("coordenada x del punto ")) - 1
pyC = int(input("coordenada y del punto "))

grid[h - pyA][pxA] = "A"
grid[h - pyB][pxB] = "B"
grid[h - pyC][pxC] = "C"

mAB = calcular_pendiente(pxA, pyA, pxB, pyB)
mAC = calcular_pendiente(pxA, pyA, pxC, pyC)
mBC = calcular_pendiente(pxB, pyB, pxC, pyC)


def calcular_angulos(m1, m2):
    if type(m1) == str and m2 == 0 or -0:
        return 90
    elif type(m2) == str and m1 == 0 or -0:
        return 90
    elif type(m1) == str or type(m2) == str:
        return 0
    else:
        return math.degrees(math.atan((m2 - m1) / (1 + m2 * m1)))


def verificar_angulos(a1, a2, a3):
    if a1 == 0:
        a1 = 180 - (a2 + a3)
    elif a2 == 0:
        a2 = 180 - (a1 + a3)
    elif a3 == 0:
        a3 = 180 - (a2 + a1)


for i in range(h):
    print(grid[i])

print(mAB, mAC, mBC)

print()
