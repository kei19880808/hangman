# ---------------------------------------------
# 継承
# ---------------------------------------------

# クラスを作るときに、ほかのクラスからメソッドや変数を受け継ぐ。
# 継承元となるクラスを親クラス、継承先のクラスを子クラスという。

# 継承をつかって図形をモデル化する。


class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


my_shape = Shape(20, 25)
my_shape.print_size()

# Shapeを継承した子クラス Square の作成


class Square(Shape):
    pass    # Python に何もしなくていいことを伝える。


a_square = Square(20, 20)
a_square.print_size()  # 20 by 20

# 子クラス独自のメソッドや変数を定義できる、これらは親クラスに影響を与えない。


class Square(Shape):
    def area(self):
        return self.width*self.len


s_square = Square(20,20)
print(s_square.area())  # 400

# メソッドオーバーライド
# → 子クラスが親クラスのメソッドを別の実装で置き換えること。


class Square(Shape):
    def area(self):
        return self.width*self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))


a_square = Square(20, 20)
a_square.print_size()
