# 開いたファイルオブジェクトを確実にクローズする方法

# try~finallyを使ったファイル読み書きのサンプルプログラム

f = open('read3.txt','r')

try:
    text = f.readlines()
    for line in text:
        print(line.strip())
finally:
    f.close

# with構文は明示的にclose()を書かなくても、自動的にクローズされる。

with open('read3.txt','r') as f2:
    text2 = f2.readlines()
    for line in text2:
        print(line.strip())

# close()メソッドはwith構文が終わるタイミングで自動的に呼び出されるので書く必要はありません。

with open('read3.txt','a') as f3:
    f3.write('イルカは特別なのか？\n')
