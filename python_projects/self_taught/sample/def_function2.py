# 戻り値が辞書型の場合

def fruits_price(apple_price,lemon_price,orange_price,banana_price):
    fruits_price_dictionary = {"apple":apple_price,'lemon':lemon_price,'orange':orange_price,'banana':banana_price}
    return fruits_price_dictionary


fruits_price_dictionary = fruits_price(banana_price=100,lemon_price=50,apple_price=200,orange_price=100)
# キーワード引数を用いると、引数の順序に関係なく、関数に値を渡すことができる。

print(fruits_price_dictionary)

# デフォルト引数

def print_message(message1 = '今日は',message2 = '晴れです。'):
    print(message1)
    print(message2)

print_message()

# デフォルト引数を指定したうえで、関数呼び出しの際にも引数を指定した場合
# 円の面積を求める

def area_of_circle(radius,pi = 3.14):
    return (radius**2)*pi

print(area_of_circle(10))   #小学生が円を求めるとき

print(area_of_circle(10,3.141592))   #　デフォルト引数よりも指定した引数が優先され、より精度の高い円の面積を求めることができる。

# 何個の引数を与えていいかわからない場合の引数の定義
# プログラム言語の一覧を表示する関数

def programing_language_list(*language):
    for programing_language in language:
        print(programing_language)

# 好きな数だけ引数を渡してよい

programing_language_list("Python3",'PHP','C#',"Ruby",'C+')

# このlanguageはタプル型の変数！
# 関数を定義するときに、引数に*引数名を指定することで、任意の数の引数を渡すことができるというわけです！

#  好きな数のキーワード引数を受け取って辞書化する関数

def generate_dic(**element):
    for key in element:
        print(key + "といえば" + element[key])

generate_dic(Apple = "Iphone",Microsoft = "windows",Sony = "walkman")
