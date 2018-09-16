# =============================================
# 正規表現
# =============================================


# ---------------------------------------------
# シンプルな一致
# ---------------------------------------------

import re

li = "Beautiful is better than ugly."
matches = re.findall("Beautiful", li)  # findall関数→正規表現パターンと検索対象のテキストを渡すと、一致したすべての部分をリストで返す


print(matches)    # ['Beautiful']

# 大文字、小文字を無視して検索したい場合、findall関数の3つ目の引数に re.IGNORECASE を渡す。

li = "Beautiful is better than ugly."
matches = re.findall("beautiful", li, re.IGNORECASE)

# -----------------------------------------------
# 前方一致と後方一致
# -----------------------------------------------

# キャレット記号→行の先頭に一致する正規表現パターンを作れる。

zen = '''Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

m = re.findall("^If", zen, re.MULTILINE)
print(m)  # ['If', 'If']

# re.MULTILINE は複数行のテキストを複数行として扱うためのフラグ。

# -----------------------------------------------------
# 複数文字との一致
# -----------------------------------------------------

string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)  # ['Two', 'too']

# ----------------------------------------------------
# 数値との一致
# ----------------------------------------------------

# \d

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)  # ['1', '2', '3', '3', '4']

# ------------------------------------------------------
#  繰り返し
# ------------------------------------------------------

# .（ピリオド）はどんな文字にも一致。
# *（アスタリスク）は直前のパターンが０回以上一致。

# 貪欲な正規表現→できるだけ長い文字列に一致。

t = "__hi__bye__hi__there__"
found = re.findall("__.*__", t)
print(t)  # __hi__bye__hi__there__  一番長い文字列を検索。

# 非貪欲な正規表現→できるだけ少ない文字列に一致。
t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)

# --------------------------------------------------------
# エスケープ
# --------------------------------------------------------

# 特別な文字をエスケープして本来の文字に一致させたい場合、その文字の前にバックスラッシュ\をつける

# $記号は通常、文字列の終端に一致するが、バックスラッシュでエスケープすると、ドル記号そのものに一致する。

line = " I love $."
m = re.findall("\\$", line, re.IGNORECASE)
print(m)  # ['$']




