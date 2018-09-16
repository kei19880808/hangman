# for文による繰り返し処理

for i in range(3):
    print("3回繰り返します。")
    print(i)

str = 'あいうえお'
for i in str:
    print(i)

# リスト型とfor文

foods = ['apple','orange','banana','grape']
for s in foods :
    print(s + "が食べたい。")

# 辞書型とfor文

number = {'one':'一','two':'二','three':'三'}
for k in number:
    print(k + 'を日本語訳すると、' + number[k])