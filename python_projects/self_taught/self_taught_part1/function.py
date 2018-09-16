#関数の定義

def f(x):
    return x*2

result = f(2)
print(result)

#引数を持たない関数

def f():
    return 1 + 1

result = f()
print(result)

#複数の引数を持つ関数

def f(x,y,z):
    return x + y + z

result = f(1,2,3)
print(result)

#return文がない関数はNoneを返す

def f():
    z = 1 + 1

result = f()
print(result)

#組み込み関数→初めからパイソンに用意されてる関数

#文字列の長さを返す関数

len('Python')  #6

#オブジェクトを引数として受けとり、文字列型のオブジェクトに変換する関数

str(100) #"100"

#オブジェクトを受け取り、整数オブジェクトを返す関数

int("1")  #1
int(2.2)  #2

#浮動小数点数オブジェクトを返す関数

float(100) #100.0
float("23") #23.0

#プログラムを動作させている人から、情報を集める組み込み関数

age = input("Enter your age")
int_age = int(age) # input関数はユーザーの入力を文字列データ型で受け取る
if int_age <21:
    print("you are young!")
else:
    print("wow, you are old!")

