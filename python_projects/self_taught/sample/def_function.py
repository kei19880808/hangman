# 自作関数の定義
def print_hello():
    print("こんにちわ！")                     # 処理を書く

print_hello()

# 引数のある関数

# 二つの数を加減乗除する関数、num1,num2には数値を、
# mode演算の種類を文字列型で指定する。
# modeの種類は加算（plus),減算（minus),乗算(multiply), 除算（division)。

def calc(num1,num2,mode):
    if(mode == "plus"):
        print(num1+num2)
    elif(mode == "minus"):
        print(num1-num2)
    elif(mode == "multiply"):
        print(num1*num2)
    elif((mode == "division") and (num2 !=0)):
        print(num1/num2)
    else:
        print("エラー：演算モードの指定が間違っているか、０で割っている可能性があります。")

calc(2,2,"plus")
calc(2,0,"division")
calc(2,8,"chopin")

# 本来はnum1 num2 が数値であるかを判定する必要がある。

# 戻り値

# 必ず整数型でユーザーからの入力を受け入れる関数

# input_messageはユーザーに入力を求めるときに表示するメッセージ。
# error_messageはユーザーが数値以外の値を入力した場合に表示するエラーメッセージ。

def num_input(input_message,error_message):

# 変数numberにユーザーからの入力を受け取る。

    number = input(input_message)

# ユーザーからの入力が数値かどうかを判定
    if(number.isdigit()):
        return int(number)
    else:
        return error_message

num = num_input("好きな数字を入力してください", 'Error:数値を入力してください。')

print(num)
print(type(num))   # ユーザーが入力した値のデータ型を表示
