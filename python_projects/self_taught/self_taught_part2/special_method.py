# =========================================================
# 特殊メソッド
# =========================================================

# Python のすべてのクラスは object クラスを継承する。


class Person(object):
    pass


print(dir(Person))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__', '__weakref__'] .........（※）


class Lion:
    def __init__(self, name):
        self.name = name


lion = Lion("Robert")
print(lion)  # <__main__.Lion object at 0x000001AB623A97F0> ....... ①

# この時Pythonはobjectクラスから継承した__repr__という特殊メソッドを呼び出している。
# この特殊メソッドをオーバーライドすれば、挙動が変わる。


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


lion = Lion("Robert")
print(lion)     # Robert  ①と挙動が違う。__repr__メソッドがLionオブジェクトの名前を返すように変更したため。

# 被演算子としてのオブジェクト → 演算子が式を評価するのに使用する特殊メソッドを持つ必要がある。
# 例えば整数値は特殊メソッド __add__を持っていて、足し算を評価するときにはこのメソッドを呼んでいる。
# つまり、__add__メソッドをクラスに持たせれば、そのオブジェクトを足し算の演算子で計算できる。
# 上記の※を見て分かるように、__add__ メソッドはobjectクラスからは継承されてない。


class Alwayspositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)


x = Alwayspositive(-20)
y = Alwayspositive(10)

print(x + y)






