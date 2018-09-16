# 例外処理

def triple(number):
    try:
        result = int(number)
        # 数字以外を引数に指定した場合、整数型に変換できない。その時この行は無視される。
        return result*3
    except:
        # 数値以外の文字列をtripleの引数に指定した場合この行に直行
        # 例外が発生したときの戻り値を0に指定
        result = 0
        return result

num = triple("uhoho")
print(num) #  文字列を引数に指定したため、例外処理がなされ0と表示される。
if(num == 0):
    print('不正な値がdouble関数に入力されました！！')
else:
    print('triple関数は正常に実行されました！！')

# 例外の場合、戻り値0を返すのでではなく、エラーメッセージを表示させるには

def triple(number):
    try:
        result = int(number)
        # 数字以外を引数に指定した場合、整数型に変換できない。その時この行は無視される。
        return result*3
    except Exception as e:
        # 数値以外の文字列をtripleの引数に指定した場合この行に直行
        # 例外が発生したときの戻り値をエラーメッセージにする
        result = e.args
        return result

num = triple('uhoho')
print(num)