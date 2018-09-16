# 1

class Apple():
    """r(radius)はリンゴの半径(cm)、l(luster)はリンゴの艶(0～100)、
       w(weight)はリンゴの重さ（グラム）"""
    def __init__(self, c, w, l, r):
        self.color = c
        self.weight = w
        self.luster = l
        self.radius = r

app1 = Apple("dark red", 200, 50, 10)

# 2

import math

class Circle():
    def __init__(self, r):
        """ r は円の半径"""
        self.radius = r
        print("Created!")

    def area(self):
        return math.pi*self.radius**2


cir = Circle(10)
print(cir.area())

# 3

class Triangle():
    def __init__(self, base, height):
        """ base 底辺の長さ
        height 底辺に対する三角形の高さ"""

        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.height*self.base

tri = Triangle(5, 6)
print(tri.area())

# 4

class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        """ s1～s6 はそれぞれ六角形の一辺の長さ"""

        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

hex = Hexagon(1, 2, 3, 4, 5, 6)
print(hex.calculate_perimeter())

