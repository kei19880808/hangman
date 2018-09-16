#　順序付きデータの集まりをリストという

baseball = ['ピッチャー','キャッチャー','内野手','外野手']  #　一つ一つのオブジェクトは要素と呼ばれる

print(baseball)

empty_list = list()           #　空のリスト

#文字列のリスト化

s = list('johntoravolta')
print(s)

#リストから要素を取り出す

print(baseball[0])           #　ピッチャーを取り出す

#リストはリストを要素に持てる

list_of_list = [['野球','サッカー'],['水泳','陸上']]

print(list_of_list[0])    #　球技のリストである[野球、サッカー]を取り出す

print(list_of_list[0][0])   #　球技のリストの中の一番目の野球を取り出す

# リストの要素の変更

list = ['JAL','ANA','PEACH']
list[0] = 'SKY'              # JALをSKYに変更
print(list)

# リストのスライス

list = ['楽天','ホークス','オリックス','近鉄','西武','日ハム']

print(list[0:2])

print(list[0:5:2])

print(list[::-1])            # リストの順序を反転

# リストの追加、合体

break_fast = ['白米','卵焼き','サバの塩焼き','みそ汁','サラダ']

break_fast.append('ヨーグルト')

print(break_fast)

lunch = ['グリーンカレー','フルーツ']
dinner = ['親子丼','野菜スープ']

break_fast.extend(lunch)
break_fast.extend(dinner)

print(break_fast)

# リストの要素を削除

del break_fast[1]
print(break_fast)
