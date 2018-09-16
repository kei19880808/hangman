# 乱数を発生させるプログラム

# ファイル名をrandom.pyにするとエラーがでるので注意！


# randomモジュールの読み込み

import random

print(random.randint(1,10))  # randint(1, 10)とすることで1から10までの範囲で整数の乱数を取得できる

# 乱数を利用した簡易占いプログラム

import random

#  入力された文字を整数にする関数、入力が整数でなければ0を返す

def num_input(num1):
    result = input(num1)
    if(result.isdigit()):
        result = int(result)
        return result
    else:
        return 0

#占い結果を判断し、占い結果メッセージを表示する関数

def judgement(omikuji):

    rand = random.randint(1,9)
    if(omikuji == rand):
     print('素晴らしい！超大吉です！なんでも願いが叶うよ！')
    elif(omikuji > rand):
     print("まぁまぁかな。ラッキーアイテムは任天堂3DS!!")
    elif(omikuji < rand):
     print('運悪すぎ、すぐにラッキーアイテムの車を買ったほうがいいよ。')

#  何回でも繰り返せるように無限ループを生成

while(True):
        omikuji = num_input('1 から 9 の中で好きな数字を入力してください\n\n')

        if((omikuji != 0) and (omikuji > 0 ) and (omikuji < 10)):
            print('あなたの好きな数字は' + str(omikuji) + "ですね！\n\n")
            print('それではその数字からあなたの命運を占って差し上げましょう。\n\n')
    # 占い結果を判断し、占い結果メッセージを表示する関数を呼び出し
            judgement(omikuji)
# 正常に占いが終わったのでwhile文を抜け出しプログラムを終了。
            break

# omikujiの値が1から9のどれにも該当しない場合

        else:
            print("1から9の数字を入力してください。\n\n")