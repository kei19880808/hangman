# オブジェクト指向プログラミング


# --------------------------------------
# class の定義
# --------------------------------------


class Orange:
    def __init__(self):    # 特殊method.  selfはこのメソッドを呼び出すときにつかったオブジェクト。
        print("Created!")

# インスタンス変数の定義: self.[変数名] = [値]

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")


or1 = Orange(10, "dark orange")   # クラスのインスタンス化
print(or1)  # オブジェクト自体を画面に出力すると、どのクラスのオブジェクトであるかと、コンピュータのメモリ上の位置を表示する。

# インスタンス変数の取得

print(or1.weight)
print(or1.color)

# インスタンス変数の変更 →[オブジェクト名].[インスタンス名] = [新しい値]

or1.weight = 100
or1.color = "light orange"

print(or1.weight)
print(or1.color)

# 複数のオブジェクトを作成する。

class Orange:
    def __init__(self, w, c ):
        self.weight = w
        self.color = c
        print("Created!")


or1 = Orange(4, "light orange")
or2 = Orange(8, "dark orange")
or3 = Orange(14, "yellow")

# Orange object に腐る性質を追加した例

class Orange:
    def __init__(self, w, c):
        """weight（重さ）はグラム"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")


    def rot(self, days, temp): # オレンジを買ってからの日数と、その間の平均気温
        """temp（温度）は摂氏"""
        self.mold = days*temp


orange = Orange(200, "orange")
print(orange.mold)
orange.rot(10, 37)
print(orange.mold)

# 長方形を表すクラス

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l


    def area(self):
        return self.width*self.len


    def change_size(self,w ,l):
        self.width = w
        self.len = l


rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())