# 文字列操作

# 三重クオート文字列→文字列を複数行書きたいとき

print('''三重クートを使うと、
文字列が複数行になっても
エラーを吐きません
''')

# 文字列のインデックス

author = "Kafka"

print(author[3])  # k （0から数える。）

# マイナスインデックス→インデックスを右から数える。

print(author[-3])  # f （マイナスインデックスの場合、0からではなく1から数える。）

# 文字列はイミュータブル

ff = "F. Fitzgerald"
ff = "F. Scott Fizgerald"
print(ff)  # "F. Fizgerald"

# 文字列の足し算

print("cat" + " in" + " hat.")  # cat in hat.

# 文字列の掛け算

print("persimmon"*4)  # persimmonpersimmonpersimmonpersimmon

# 大文字小文字変換

print("My favorite fruits are persimmons and pears.".upper())  # すべて大文字に

print("MY NAME IS KEI HAGIMOTO.".lower())  # すべて小文字に

print("it is good to be healthy.".capitalize())  # 文字列の最初の文字を大文字、残りは小文字

# 書式化(フォーマット)→文字列の一部{}を、あとで穴埋めして新しい文字列を返す。

print("こんにちわ、{}".format("赤ちゃん"))

name = "コーリー・アルソフ"
print("こんにちわ、{}".format(name))  # formatメソッドは変数も渡せる。

# {}は文字列中に何個も書ける

author = "Agatha Christie"
year_born = "1890"

print("{} は {} 年に生まれました。".format(author,year_born))

who = input("誰が:")
when = input("いつ:")
where = input("何処で:")
what = input("何をした:")

print("{}が{}、{}で{}をした。".format(who,when,where,what))

# 分割

# split method → 1つの文字列を、どの文字で分割したいのかを渡すと、その文字を境に、複数の文字列に
# 分割した結果がリストで返される。

print("古池や、蛙飛び込む、水の音".split("、"))

# 結合
# join method → すべての文字列の間に新しい文字を追加する。

first_three = "abc"
result = "+".join(first_three)
print(result)

# join の引数には文字列のリストを持ってこれる。

words = ["The","fox","jumped","over","the","fence","."]
result = " ".join(words)
print(result)
