# 空白除去

s = "   the    "
s = s.strip()
print(s)

# 置換

equ = "All animals are equal"

equ = equ.replace("a","@")
print(equ)  # All @nim@ls @re equ@l

# 文字を探す → ある文字が文字列内で最初に現れる位置を探す。

print("animals".index("m"))  # 3

# 含まれている変わらない文字を探すときは例外処理をする。

try:
    result = "persimmon".index("z")
    print(result)
except:
    print("Not Found")

# 包含

print("to" in "Needless to say")  # True
print("ancle" not in " Please excuse my dear aunt Sally ?") # True

# エスケープ文字

# 文字列中にクオート文字を含めるにはバックスラッシュを使う。

print("彼女は \"そうだね\" と言った。")  # 彼女は "そうだね" と言った。

# ダブルクオートないではシングルクオートはエスケープなしで使える。その逆も可

print("彼女は 'そうだね' と言った。")  # 彼女は 'そうだね' と言った。

# 改行 \n

print("line1\nline2\nline3")

# スライス → 繰り返し可能なオブジェクトの一部分を取り出して、
# 新しく生成した繰り返し可能なオブジェクトを返す。

# リストをスライスする。

fict = ["トルストイ","カミュ","オーウェル","カフカ","ドストエフスキー"]

print(fict[0:3])  # ['トルストイ', 'カミュ', 'オーウェル']

# ---------------------------------------------------------------
# 終了インデックスはそこに達したらスライスの取り出しを終了するインデックス。
# ---------------------------------------------------------------

# 文字列をスライスする。

ivan = "死の代わりにひとつの光があった。"
print(ivan[0:6])    # '死の代わりに'
print(ivan[6:16])   # 'ひとつの光があった。'

# インデックス0から始めるときは開始インデックスは省略可能。

print(ivan[:6])    # 死の代わりに

# 最後の要素までを含めて終了インデックスを指定したいとき、終了インデックスを省略可能。

print(ivan[6:])   # ひとつの光があった。

# 開始、終了共に空にした場合、元のイテラブルのコピーが作られる

print(ivan[:])  # "死の代わりにひとつの光があった。"


