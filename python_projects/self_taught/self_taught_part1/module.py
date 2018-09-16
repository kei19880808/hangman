# -----------------------------
# モジュール
# -----------------------------


# |||||||||組み込みモジュール||||||||||||

# math module

import math  # import はファイルの先頭に書き、誰でもファイルを開いたらすぐに分かるようにするべき。

print(math.pow(2, 3))  # 2^3

# random module

import random

print(random.randint(0, 100))  # 0～99の間で整数の乱数を生成する。

# statistics module

import statistics

nums = [1, 5, 33, 12, 46, 33, 2]

# mean

print(statistics.mean(nums))  # 平均値

# median

print(statistics.median(nums))  # 中央値

# mode

print(statistics.mode(nums))    # 最頻値

# keyword module → pythonのキーワードかどうかチェックする。

import keyword

print(keyword.iskeyword("for"))     # True
print(keyword.iskeyword("football"))  # False


# --------------------------------------------------
# 新しいモジュールを作る
# --------------------------------------------------

# def print_hello():
#         print("Hello")   # hello.pyに作成

import hello

hello.print_hello()

# モジュール内のコードで、実行されたくないコードには以下のコードを書き加える。
# module1.py を作成
# 中身↓
# if __name__ == "__main__":
#     print('Hello')

import module1  # print("Hello")は実行されない。
