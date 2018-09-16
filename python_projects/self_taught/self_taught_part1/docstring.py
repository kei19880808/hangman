#ドキュメンテーション文字列
#関数を呼びだす人に、エラーが起きないように引数のエータ型を伝える方法

def add(x,y):
    """
    returns x + y.
    : param x: int.
    : param y: int.
    :return int sum of x and y
    """
    return x + y

#他のプログラマーがこの関数を利用するときに使う
#関数の機能をコードを読むより早く理解できる。