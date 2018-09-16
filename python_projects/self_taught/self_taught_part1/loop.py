# for loop
# for [変数名] in [イテラブル]:
# [コードブロック]
# の形をとる。ループが回るたびに、変数にはイテラブルから取り出した新しい""要素””が割り当てられる。
# インデックスではないことに注意‼ →インデックス値を受け取るにはenumerate関数を使う


# 文字列を一文字ずつ取りだす。

name = "Hagimoto"
for character in name :
    print(character)

# リストの要素を繰り返し画面出力する。

shows_fruits = ["Pear","Persimmon","watermelon","kumquat"]
for show_fruits in shows_fruits:
    print(show_fruits)

# タプルの要素を繰り返し画面出力する。

shows_str = ("A. Development","Friends","Always Sunny")
for show_str in shows_str:
    print(show_str)

# ループで辞書のキーを要素として繰り返す。

company = {"Apple":"Iphone","Microsoft":"Windows","Sony":"Walkman"}
for com_name in company:
    print(com_name)

# for loopを使ってリストを更新する。

tv = ["AQUOS","VIERA","WOOO","BRAVIA"]

i = 0
for show in tv:
    name = tv[i]
    name = name.lower()
    tv[i] = name
    i += 1

print(tv)

# enumerate 関数を使えば、forの変数として現在のループにおけるインデックス値を受け取るiを追加できる。

for i,name in enumerate(tv):
    name = tv[i]
    name = name.upper()
    tv[i] = name

print(tv)

# for loop の中でデータを加工して別のリストに追加する。
# tv_brand 、tv_brand_2 の2リストの要素を大文字に変えて、all_brands に追加するプログラム。

tv_brand = ["Aquos","Viera","Wooo","Bravia"]
tv_brand_2 = ["Regza"]
all_brands = []

for name in tv_brand:
    name = name.upper()
    all_brands.append(name)

for name in tv_brand_2:
    name = name.upper()
    all_brands.append(name)

print(all_brands)

#  range
#  組み込み関数rangeは整数を順番に生成してくれる。

for i in range(1,11):  # 1から11まで
    print(i)
