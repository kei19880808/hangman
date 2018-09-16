x =2
if x == 2:
    print('数値は2です。')
if x % 2 == 0 :
    print("数値は偶数です。")
if x % 2 != 0 :
    print("数値は奇数です。")


x = 10
y = 12

if x == 10:
    if y == 12:
        print('OK')

x = 100

if x == 10:
    print("10!")
elif x == 20:
    print('20!')
else:
    print('わかりません！')

str1 = 'america'
str2 = 'japan'
str3 = 'china'

print(str1)
print(str2)
print(str3)

x = 23

if x >= 10:
    print("１０以上の数です。")
else:
    print("10より小さい数です。")

s = 22

if s <= 10:
    print('10以下の数です。')
elif 10 < s <= 25:
    print("10より大きく25以下の数です。")
else:
    print('25より大きな数です')

x = 21
y = 5

print(x % y)
print(x // y)

age = 21

if age < 18:
    print('結婚も喫煙も飲酒も全部だめ！')
elif 18 <= age < 20:
    print('結婚はしていいけど、飲酒喫煙はだめ！')
else:
    print('結婚も飲酒喫煙も問題ナッシング！')

def increment(a):
    return a + 1

print(increment(2))