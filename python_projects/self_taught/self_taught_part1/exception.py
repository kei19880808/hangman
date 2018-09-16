#例外処理

#0除算を回避するプログラム　　try-except

a = input("type a number")
b = input('type a number')
a = int(a)
b = int(b)

try:
    print(a/b)         #bに0以外が入力された場合はこちら

except ZeroDivisionError:
    print("b cannot be zero.")

#ユーザーが数値以外を入力した場合の対処

try:
    c = input("type a number")
    d = input('type a number')
    c = int(c)
    d = int(d)
    print(c/d)

except (ZeroDivisionError,ValueError):  #かっこでくくることで、二つの例外を捕らえられる。
    print('Invalid input.')

#トライ節で定義された変数をexcept内で使用するな！　トライ節で変数が定義される前に、例外が発生し、
#exceptに飛ばされる可能性があるからだ。

try:
    10/0
    e = "I will never get defined"
except ZeroDivisionError:
    print(e)