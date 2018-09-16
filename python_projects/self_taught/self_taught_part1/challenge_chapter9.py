# 1

with open(r"C:\Users\chopin\Desktop\self_taught_python\hello_world.py", "r", encoding="utf-8") as f:
    print(f.read())

# --------------------------------------------------------------------------------
# 'r'を使うことで、raw文字列として扱われ、"\U"がエスケープシーケンスとして処理されなくなります。
# --------------------------------------------------------------------------------

# 2

while True:
    age = input('何歳ですか？数字を入力してください。:')

    try:
        age_int = int(age)
        with open("age.txt", "w", encoding="utf-8") as f :
            f.write(age)

        break

    except:
        print('数字を入力してください')

# 3

import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on fire", "Flight"]]

with open("movies.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter =",")
    for i in movies:
        w.writerow(i)

# 4

movies_japanese = [["トップガン", "マイノリティーリポート", "ミッションインポッシブル"],
                   ["ザ・ビーチ", "タイタニック", "インセプション"],
                   ["ボーンコレクター","トレーニングデイ","フライト"]]

with open("movies_japanese.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter =",")
    for i in movies_japanese:
        w.writerow(i)