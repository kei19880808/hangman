#float(浮動少数型)の3.14を整数に変換
e1 = int(3.14)
print(e1)

#ブール値型のTrueを整数に変換
e2 = int(True)
print(e2)

#文字列の55を整数の55に変換
e3 = int('55')
print(e3)

#int()を使わずに文脈で型変換する例
e4 = True + 2
print(e4)