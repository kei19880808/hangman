# ----------------------------------------------
# ファイルに書き出す。
# ----------------------------------------------


st = open("st.txt","w")
st.write("Hi from Python!")  # st.txtに Hi from Python! と書き込む。
st.close()

# 日本語を書き込む場合 → 文字コードに気を付ける。

st = open("st.txt", "w", encoding="utf-8")
st.write("Pythonからこんにちわ！")
st.close()

# ----------------------------------------------
# ファイルを自動的に閉じる
# ----------------------------------------------


# with 構文

with open("st.txt", "w") as f :
    f.write("Hi from Python!")


# -----------------------------------------------
# ファイルから読み込む
# -----------------------------------------------


with open("st.txt", "r") as f :
    print(f.read())   # Hi from Python!

# read method はファイルを開いた後一回だけ使える。
# ファイルのコンテンツを読み込んで、リストに入れておく

my_list = []

with open("st.txt", "r") as f :
    my_list.append(f.read())

print(my_list)

# ------------------------------------------------
# csvファイルを扱う
# ------------------------------------------------

# csv module

import csv

with open("st.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter =",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

# csv ファイルの読み込み

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
