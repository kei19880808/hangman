# tuple : 好きな順番でオブジェクトを保存しておけるコンテナ。変更不可能（イミュータブル）。

my_tuple = tuple()
print(my_tuple)

# 別の作り方

my_tuple = ()
print(my_tuple)

random = ('osaka','tokyo','fukuoka')
print(random)

# 要素を変更しようとすると。。

# random[1] = "nagoya"

# TypeError: 'tuple' object does not support item assignment

# tupleの要素を取りだす

print(random[1]) # indexで位置を指定する。

# tupleに特定の要素が含まれているかを確認するにはin演算子を使う。

print("fukuoka" in random)

# 入っていないことを確認するには not in 演算子を使う

print("nagoya" not in random)

# tupleはイミュータブルなので、プログラムの途中で間違って書き換えられてしまうことを防げる。
# ある都市の経度と緯度など、不変なデータにはtupleを用いるとよい。