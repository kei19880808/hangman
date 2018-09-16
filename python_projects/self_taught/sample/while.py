# 条件式を満たす間、処理を繰り返す

cont = 0

while (cont <10):
    print("繰り返しています！")
    print(cont +1)
    cont = cont + 1

# ユーザーの好きな回数だけ繰り返す

end = 0
while(end ==0):
    print('ユーザーから入力があるまでぐるぐる回ります')
    end = input("ループを終了するには0以外の好きな値を入力してください")
    end = int(end)

# Python3では関数inputは文字列で値を返すので、数値型に変換する必要がある

# breakを使ってwhileから抜け出す

cont = 0

while(True):
    print(cont)
    cont = cont + 1

    if(cont ==5):
        print('contの値が5になったのでループを抜けます')
        break

# 条件式にTrueを指定すると、評価も何もなく、永遠に繰り返し処理をし続けます。

#continue

cont = 0

while(cont <5):

    print(cont)
    cont = cont + 1

    if(cont ==3):
        print("contが3のときは最後のメッセージを飛ばします")
        continue

    print('繰り返しております！')


list = ['Apple','Microsoft','IBM']

for company in list:

    if(company =="IBM"):
        print(company + "は戦前から日本にある老舗ですね！")
        continue
    print(company + "はIT企業の花形ですね！")