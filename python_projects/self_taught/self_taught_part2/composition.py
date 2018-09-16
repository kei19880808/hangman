# -------------------------------------------
# コンポジション
# -------------------------------------------

# 別クラスのオブジェクトを変数として持たせる。

# 犬とその飼い主の関係

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


mick = Person("Mick Jagger")
stan = Dog("stanley", "Bulldog", mick)
print(stan.owner.name)  # Mick Jagger

# stan オブジェクトは”Mick Jagger" という名前のPerson オブジェクトをインスタンス変数に持つ。