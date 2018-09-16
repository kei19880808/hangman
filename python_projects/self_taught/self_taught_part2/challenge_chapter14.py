# 1

class Square:
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1*4


sq1 = Square(10)
sq2 = Square(20)
print(Square.square_list)

# 2


class Square:
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1*4

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)


a_square = Square(29)
print(a_square)

# 3

def true_or_false(a, b):
    return a is b


print(true_or_false(2, "a"))  # False

