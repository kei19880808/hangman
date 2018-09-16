# --------------------------------------------------
# クラス変数
# --------------------------------------------------

# クラス変数は、各クラス定義時にパイソンが作成したクラスオブジェクトに属する。
# この変数はクラスオブジェクトから参照でき、且このクラスから作られたインスタンスオブジェクトからも参照できる。


class Rectangle:
    recs = []  # クラス変数の定義は__init__メソッドの外側で行う。

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)  # [(10, 24), (20, 40), (100, 200)]

# クラス変数を使うと、グローバル変数を使わずに、クラスのインスタンス間でデータを共有できます。