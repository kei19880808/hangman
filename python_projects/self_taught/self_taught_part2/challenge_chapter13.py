# -------------------------------------------
# 1
# -------------------------------------------

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return 2*(self.width + self.len)


class Square:
    def __init__(self, a):
        self.length = a

    def calculate_perimer(self):
        return 4*self.length


rec = Rectangle(5, 10)
print(rec.calculate_perimeter())
squ = Square(10)
print(squ.calculate_perimer())

# ---------------------------------------------
# 2
# ---------------------------------------------

class Square:
    def __init__(self, a):
        self.length = a

    def calculate_perimer(self):
        return 4*self.length

    def change_size(self, x):
        self.length += x

squ2= Square(10)
print(squ2.calculate_perimer())  # 40

squ2.change_size(1)    # length  → length + 1
print(squ2.calculate_perimer())  # 44

# ------------------------------------------------
# 3
# ------------------------------------------------

class Shape:
    def what_am_i(self):
        print("I am a shape")


class Square(Shape):
    def __init__(self, a):
        self.length = a

    def calculate_perimer(self):
        return 4*self.length

    def change_size(self, x):
        self.length += x


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return 2*(self.width + self.len)


rec_shape = Rectangle(10, 10)
rec_shape.what_am_i()  # I am a shape
squ_shape = Square(10)
squ_shape.what_am_i()  # I am a shape

# ---------------------------------------------
# 4
# ---------------------------------------------

class Rider:
    def __init__(self, name):
        self.name = name


class Horse:
    def __init__(self, name, hair_color, weight, owner):
        """weight(kg)"""
        self.name = name
        self.hair_color = hair_color
        self.weight = weight
        self.owner = owner


harry = Rider("Harry Hurry")
ashy =  Horse("ashelly", "ash_brown", 490, harry)
print(ashy.owner.name)  # Harry Hurry → ashy のオーナーの名前
