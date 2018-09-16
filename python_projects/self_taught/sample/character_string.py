#http://docs.python.jp/3/library/stdtypes.html#string-methods
#パイソン公式の文字列操作のドキュメント



#エスケープ文字

print('こんにちわ！\n元気ですか？')   #改行

print('こんにちわ！\t元気ですか？')   #タブ

print('こんにちわ！\'元気ですか？')

#文字列の連結

s1 = 'abc'
s2 = 'def'
print(s1,s2)

#文字列の繰り返し

s = 'sos'
print(s*5)

#文字列の中の１つの文字列を取り出す

k = "john"
print(k[0]*4)                 #jを4回繰り返す

#文字列をスライスする

sl = 'abcdefghijklmn'

print(sl[:])                  #文字列すべてを取得

print(sl[4:])                 #eからnまでを取得

print(sl[:3])                 #先頭から3文字目マイナス1字目までをスライス

print(sl[3:5])

print(sl[0:5:2])              #先頭から5文字目までをステップ(一文字ずつ抜かす）

print(sl[-1::-1])             #文字の順序が逆になる

#文字列の長さを取得

s = 'パイソン先輩'
print(len(s))

#文字列の分割

s = 'この野郎!俺のささ身を食べやがったな!楽しみだったのに。'
print(s.split("!"))           #半角！をセパレーターに指定

#文字列の置き換え

s = '豚野郎！'
print(s.replace('豚','くそ'))