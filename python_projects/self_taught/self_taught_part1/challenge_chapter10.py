# 英単語当てクイズ →答えの単語をリストからランダムに選ぶバージョン。

import random

def hangman():

    answer_words = ["cat", "dog", "snake", "bird"]

    rand_word = random.randint(0, 3)

    word = answer_words[rand_word]

    wrong = 0                         # プレイヤーの予想が何回はずれたかを表す変数。初期値を0に設定。
    stages = ["",
              "___________        ",
              "|                  ",
              "|          |       ",
              "|          0       ",
              "|         /|\      ",
              "|         / \      ",
              "|                  "
              ]
    rletter = list(word)  # 英単語を一文字に区切ったリストを作成。
    board = ["_"]*len(word) # 英単語の文字の数だけアンダーラインを要素に持つリストを作成。
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) -1 : # ステージが完成するまでの間繰り返す処理。
        print("\n")
        msg = "アルファベット一文字を予想してね。"
        char = input(msg)
        if char in rletter:
            index_number = rletter.index(char)  # rletter内に char が複数あっても、最初のインデックスを返す。
            board[index_number] = char
            rletter[index_number] = "$"  # 上のコメントの事情を避けるため、すでに答えられた文字は＄に置き換える。
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1                 # 終了インデックスはスライスに含まれないので1を足す。
        print("\n".join(stages[0:e]))  # ハングマンの絵の途中経過を表示。
        if "_" not in board:   # board の中にアンダーラインがない＝プレイヤーの勝ち。
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:   # winが偽であれば真。
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け！正解は{}".format(word))


hangman()





