#条件分岐　条件がTrueの時

if(10>=1):
    print('10は1以上の数')

# 条件がTrueでなくFalseでも処理を実行

budget = 20000
cpu_price = 24000

if(budget >= cpu_price):
    print('CPU買いました！')

else:
    print('CPU高けええええええええ')

# より複雑な条件分岐
# テストの点数により異なるメッセージを表示するプログラム
test_score =100

if(test_score == 100):
    print("満点！すげえ")
elif(test_score >= 50):
    print('合格じゃ')

else:
    print("不合格")

test_score = 90

if(test_score >= 80):
    print("あなたは80点以上ですので成績はAです。")
elif((test_score >= 70) and (test_score <=80)):
    print('あなたは70点以上80点未満ですので成績はBです。')
elif((test_score >= 60) and (test_score <=70)):
    print('あなたは60点以上70点未満ですので成績はCです。')
else:
    print("落第です。")