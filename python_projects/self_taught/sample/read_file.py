# ファイルを新規作成し、そのファイルを読み込み、その結果を出力。
f = open('read.txt','w')
f.write('今日は眠い。')
f.flush()
f.close()

# ----------------------------------------------------
# 次に先ほど作成したread.txtを読み込み、printする
# ----------------------------------------------------

r = open('read.txt','r')

# readline()はファイルの先頭から１行だけ読み込みその結果を返す

readme = r.readline()

r.close()

print(readme)

# 複数行を読み込む場合

f = open('read2.txt','w')
f.write('今日は眠い。\nそういえば昨日も眠かった。\n最近睡眠不足だ。')
f.flush()
f.close()

# readlines()は、複数行を読み込み、リスト型で返す

r2 = open('read2.txt','r')

readme2 = r2.readlines()

r2.close()

print(readme2)

# strip()メソッドを使えば、改行コードや、文字列の前後の空白を取り除いてくれる。

f2 = open('read3.txt','w')

f2.write('人間と動物との違いは何か。\n言葉があるかないかだという。\nしかしイルカ等は言葉を話すともいう。\n')
f2.flush()
f2.close()

r3 = open('read3.txt','r')
sentence_list = r3.readlines()
r3.close()

for sentence in sentence_list:
    print(sentence.strip())

# readlines()を使わなくても簡単なコードで同じことができる。
r3 = open('read3.txt','r')

for line in r3:
    print(line.strip())
r.close()