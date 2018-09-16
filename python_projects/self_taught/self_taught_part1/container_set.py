# セットは要素の重複がないコンテナで、要素の順序もない。set関数にリストを渡して生成する。

programing_language = ["Python","Java","C","PHP"]

program_lan = set(programing_language)

print(program_lan)  # 実行ごとに順序が変わる。

# セットどうしの演算

program_lan_2 = set(["Javascript","Ruby","Python"])

print(program_lan - program_lan_2) # {"Java","C","PHP"]
print(program_lan & program_lan_2) # {"Python"}
print(program_lan ^ program_lan_2) # {"Java","C","PHP","Javascript","Ruby"} 片方だけにある要素

# add method 要素を加える。

program_lan.add("Swift")
print(program_lan)

# remove method 要素を削除する。

program_lan_2.remove("Ruby")
print(program_lan_2)

# ある要素がセットに含まれているかを調べるin演算子

print("Ruby" in program_lan)  # False