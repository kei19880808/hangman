# tuple (組）と辞書について

tpl1 = (1,2,3,4,5,6) # ()は省略可能　リストとの違いは変更不可な点

print(tpl1)

#　一行で複数の変数に値を代入できる

a,b,c,d,e,f = tpl1

print(c)

# 辞書

# 辞書はタプルと違いミュータブル（変更可能）

number = {'one':1,'twe':2,'three':3}

print(number['one'])

kakaku_list = [['CPU','i5-8400'],['RAM','16GB_DDR4'],['M/B','H370-I']]

kakaku_dict = dict(kakaku_list)

print(kakaku_dict)

print(kakaku_dict['RAM'])      # RAMの量を表示

# 重要！　リストは順序が決まっているが、辞書は決まっていない