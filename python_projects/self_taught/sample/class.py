# もっとも単純なクラスのサンプルコード

class Person:
    # age プロパティに22をセット
    age = 22

#Personクラスのインスタンスを作成
psn = Person()

# Personクラスのインスタンスpsnからageプロパティを参照し画面に出力
print(psn.age) #22

# 少し複雑なクラスのサンプルコード

class Person:
    age = 22
    # greet メソッドを定義
    def greet(self):  # クラスの中で関数（正確にはメソッド）を定義するとき、第１引数に必ずselfを指定しなければならない
        print('こんにちわ！')

psn = Person()

# Personクラスのインスタンスpsnからageプロパティを参照し画面に出力
print(psn.age) #22

# Personクラスのインスタンスpsnからgreet()メソッドを呼び出す
psn.greet()

# selfとはクラスのインスタンスを受け取る特別な引数のことです。
# メソッドはクラスの自分自身のインスタンスを必ず第１引数にとるのです。

#初期化メソッドを含むクラスのサンプルコード

class Smart_phone:

    os = 'Android'

    def __init__(self):
        print(self.os)

    def call(self):
        print("電話をかけています。")

sp = Smart_phone()

# 引数付きの初期化メソッド

class Smart_phone:
    def __init__(self,os):
        self.os = os   # osはプロパティである
    def call(self):
        print('電話をかけています。')

sp = Smart_phone("iOS")

print(sp.os)