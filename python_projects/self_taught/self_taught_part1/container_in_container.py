# コンテナ中のコンテナ

#リストにリストを入れる

lists = []

rap = ["Dragon Ash",'Jay-Z','Naz']
pop = ["Chemistry",'Kinki Kids','Hikaru Utada']
rock = ["One Ok Rock","THE Beatles","GRAY"]

lists.append(rap)
lists.append(pop)
lists.append(rock)

print(lists)

rap_group = lists[0]
print(rap_group)

rap.append("Eminem")
print(rap)
print(lists)

# リストの中に、タプルや辞書を持たせることもできる。その逆も可能。

lists = []

chicago = (41.8781,87.6298) # シカゴの経度と緯度
bday = {"kei":"8.8.1988","masashi":"12.28.1957"}

lists.append(chicago)
lists.append(bday)
print(lists)

# 辞書のバリューにリスト、タプル、辞書を持つことができる。

ny = {"座標":(40.7128,74.0059),
      "セレブ":["デヴィ夫人","叶姉妹","ハリスヒルトン"],
      "事実":{"州":"ニューヨーク","国":'"アメリカ'}}

print(ny)