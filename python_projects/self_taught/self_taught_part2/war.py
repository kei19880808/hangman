# ==============================================
# Card
# ==============================================


class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]    # マーク、弱い順。

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#  A→K→Q→J→10→・・・→3→2の順に強い、インデックスと数値を一致させるために None を入れた。

    def __init__(self, v, s):
        """スートも値も整数値です。"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True

        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " " + "of" + " " \
            + self.suits[self.suit]
        return v


# card1 = Card(10, 2)
# card2 = Card(11, 3)
# print(card1 < card2)    # True

# card = Card(2, 3)
# print(card)  # 2 of clubs


# ==================================================================
# Deck
# ==================================================================
import random


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))

        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

# リストオブジェクト.pop(インデックス)
# 指定のインデックスの要素を削除し、その要素を返します。インデックスが省略された場合はリストの末尾の要素が削除されます。

# deck = Deck()    # デッキオブジェクトを作り、すべてのカードをプリント出力。
# for card in deck.cards:
#   print(card)

# ====================================================================
# Player
# ====================================================================

# プレイヤーの名前、持っているカード、ゲームで何回勝ったか。


class Player:
    def __init__(self, name,):
        self.wins = 0
        self.name = name
        self.card = None


# ===============================================================
# Game
# ===============================================================

class Game:
    def __init__(self):
        name1 = input("プレイヤー１の名前:")
        name2 = input("プレイヤー２の名前:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは {} が勝ちました。"
        w = w.format(winner)
        print(w)

    def draw(self, p1, p2):
        d = "{} は {}, {} は {} を引きました。"
        d = d.format(p1.name, p1.card, p2.name, p2.card)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます！")
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでPlay:"
            response = input(m)
            if response == "q":
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.print_winner(self.p1, self.p2)
        print("ゲーム終了、{} の勝利です！".format(win))

    def print_winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return " 引き分け！"


game = Game()
game.play_game()
