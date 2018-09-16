# ================================================
# is キーワード
# ================================================

# 前後のオブジェクトが同一のオブジェクトなら True を返す。


class Person:
    def __init__(self):
        self.name = "Bob"


bob = Person()
same_bob = bob
print(bob is same_bob)  # True

another_bob = Person()
print( another_bob is bob)   # False

# ==========================================================

x = 10
if x is None:
    print("x はNone :(")

else:
    print("x はNoneじゃない")

x = None

if x is None:
    print("x はNone")

else:
    print("x はNoneじゃない :(")