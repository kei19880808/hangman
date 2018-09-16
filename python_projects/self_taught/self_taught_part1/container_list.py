# list:好きな順番でオブジェクトを保存しておけるコンテナ

# list 関数

fruit = list() # 空のリスト、 単に[]だけでもよい。
fruit = []

print(fruit)

fruit = ["Apple","Orange","Pear"]

print(fruit)

# リストに要素を追加する。

fruit.append("Banana")  # methodのappendを使う

print(fruit)

# リストは文字列以外も格納できます

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")

print(random)

#インデックス値を使って要素を取り出す

fruit = ["pear","Banana","Persimmon"]
fruit[0] # Pear
fruit[1] # Banana
fruit[2] # Persimmon

# pop_method : リストの末尾から要素を取り除く

colors = ["Blue",'Green',"yellow"]
item = colors.pop()
print(colors)
print(item)

# 二つのリストの連結

colors1 = ["Blue","Green","Red"]
colors2 = ["Purple","Gold","Silver"]
colors3 = colors1 + colors2
print(colors3)

# ある要素がリストに含まれているかどうかを調べるin演算子
# TrueかFalseを返す

colors = ["Blue","Green","Pink"]
a = "Green" in colors # True
b ="Black" not in colors # true
print(a,b)

# リストのサイズを返す関数 len

print(len(colors)) # 3

colors = ["Gold","Pink","Red"]

guess = input("何色でしょう？（入力してください）:")

if guess in colors:
    print("あたり！")
else:
    print("ハズレ！また挑戦してね！")

