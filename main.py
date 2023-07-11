import math
import sys
import pygame

pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
screen.fill(white)
pygame.display.flip()

# Crea la planilla sobre la que se buscaran los triangulos

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    w = int(input("width: "))
    h = int(input("height: "))
    grid = []

    for i in range(h):
        grid.append([])

    for i in range(w):
        for j in range(h):
            grid[j].append(".")

    # Clase punto


    class Punto:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

        def __hash__(self):
            return hash((self.x, self.y))

    # Clase triangulo


    class Triangulo:
        def __init__(self, _p1, p2, p3):
            self.puntos = set()
            self.puntos.add(_p1)
            self.puntos.add(p2)
            self.puntos.add(p3)


    # Muestra la planilla

    for i in range(h):
        print("{}  {}".format(h - i - 1, grid[i]))


    def puntos_similares(_p1: Punto, _p2: Punto):
        if _p1.x == _p2.x:
            if _p1.y == _p2.y:
                return True
            else:
                return False
        else:
            return False


    def calcular_pendiente(_p1, _p2):
        if (_p2.x - _p1.x) == 0:
            return "Pendiente indefinida"
        return (_p2.y - _p1.y) / (_p2.x - _p1.x)


    def verificar_angulos(_listaAngulos):
        if _listaAngulos[0] == 0 and _listaAngulos[1] != 0 and _listaAngulos[2] != 0:
            _listaAngulos[0] = 180 - (_listaAngulos[1] + _listaAngulos[2])
        elif _listaAngulos[1] == 0 and _listaAngulos[0] != 0 and _listaAngulos[2] != 0:
            _listaAngulos[1] = 180 - (_listaAngulos[0] + _listaAngulos[2])
        elif _listaAngulos[2] == 0 and _listaAngulos[1] != 0 and _listaAngulos[0] != 0:
            _listaAngulos[2] = 180 - (_listaAngulos[0] + _listaAngulos[1])
        return _listaAngulos


    def calcular_angulos(m1, m2):
        if type(m1) == str and m2 == 0 or -0:
            return 90
        elif type(m2) == str and m1 == 0 or -0:
            return 90
        elif type(m1) == str or type(m2) == str:
            return 0
        elif (m1 == 1 and m2 == -1) or (m1 == -1 and m2 == 1):
            return 90
        else:
            ang = math.degrees(math.atan((m2 - m1) / (1 + m2 * m1)))
            if ang < 0:
                ang += 180
            return ang


    def mostrar_triangulos(_p1, _p2, _p3):
        print("Triangulo", _p1.x, _p1.y, _p2.x, _p2.y, _p3.x, _p3.y)
        grid[h - _p3.y - 1][_p3.x] = "X"
        grid[h - _p2.y - 1][_p2.x] = "X"
        for u in range(h):
            print(grid[u])
        grid[h - _p3.y - 1][_p3.x] = "."
        grid[h - _p2.y - 1][_p2.x] = "."


    def buscar_todos_los_triangulos(_p1, _h, _w, _setTriangulos):
        for y2 in range(_h):
            for x2 in range(_w):
                for y3 in range(_h):
                    for x3 in range(_w):

                        p2 = Punto(x2, y2)
                        p3 = Punto(x3, y3)

                        print(p2.x, p2.y, p3.x, p3.y)

                        mAB = calcular_pendiente(_p1, p3)
                        mAC = calcular_pendiente(_p1, p2)
                        mBC = calcular_pendiente(p2, p3)

                        aX = calcular_angulos(mAB, mAC)
                        aY = calcular_angulos(mBC, mAB)
                        aZ = calcular_angulos(mAC, mBC)

                        listaAngulos = [aX, aY, aZ]
                        listaAngulos = verificar_angulos(listaAngulos)

                        if listaAngulos.count(90) == 1 and listaAngulos.count(0) == 0:
                            t = Triangulo(_p1, p2, p3)
                            flag = triangulos_repetidos(_setTriangulos, t)
                            if flag:
                                del t
                            else:
                                mostrar_triangulos(_p1, p2, p3)
                                _setTriangulos.add(t)


                        del p2
                        del p3


    p7 = Punto(0, 5)
    p8 = Punto(0, 5)

    print(puntos_similares(p7, p8))

    setTriangulos = set()


    def triangulos_repetidos(_setTriangulos: set, t: Triangulo):
        for _t in _setTriangulos:
            if _t.puntos == t.puntos:
                return True
        return False


    p1 = Punto(int(input("coordenada x del punto ")), int(input("coordenada y del punto ")))

    grid[h - p1.y - 1][p1.x] = "X"

    for _u in range(h):
        print(grid[_u])

    buscar_todos_los_triangulos(p1, h, w, setTriangulos)
