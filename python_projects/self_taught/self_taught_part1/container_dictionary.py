# 辞書はキーとバリューのペアを格納する。ミュタブル

# 辞書の作り方

my_dict = dict()
print(my_dict)

# or

my_dict = {}
print(my_dict)

fruits = {"Apple":"Red","Banana":"Yellow"}

print(fruits)

# 要素の追加

facts = dict()

facts["code"] = "fun"

print(facts["code"])

facts["founded"] = 1776

print(facts["founded"])

# in演算子であるキーが辞書のキーに使われているかを確認

print("code" in facts)

print("python" not in facts)

# キーバリューペアを辞書から削除する

books = {"Dracula":"Stoker","1984":"Orwell","The Trial":"Kafka"}

del books["The Trial"]

print(books)

# 辞書を使ったプログラムの例
#番号をユーザーに入力させ、曲のタイトルを表示するプログラム

songs = {"1":"津波","2":"Lemon","3":"明日があるさ","4":"僕の背中には羽がある"}

n = input('数字を入力してください（1～5):')
if n in songs:
    song = songs[n]
    print(song)

else:
    print("曲が見つかりません。正しく数字を入力してください。")