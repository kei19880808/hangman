# オプション引数

def f(x=2):
    return x**x

print(f()) # デフォルトの引数2が適応される。
print(f(4)) # xに渡された4が利用される。

# 必須引数とオプション引数両方を持つ関数

def add_it(x,y=10):
    return x + y
result = add_it(2)  # yにはデフォルト引数の10が渡される
print(result)

# スコープ =  変数を読み書きできる範囲

# グローバルスコープ　=　関数の外で変数を定義した場合の変数を読み書きできる範囲

x = 1 # グローバル変数
y = 2 # グローバル変数
z = 3 # グローバル変数

def f():
    print(x)
    print(y)
    print(z)
f()

# ローカルスコープ　=　関数の内部で変数を定義した場合の変数を読み書きできる範囲

def f():
    a = 1  # ローカル変数
    b = 2  # ローカル変数
    c = 3  # ローカル変数

print(a) # a is not defined!!!
print(b)
print(c)

# 関数内からグローバル変数に書き込みするには

x = 100

def f():
    global x  # global keyword
    x += 1
    print(x)
f()