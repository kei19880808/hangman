# 1

drama_list = ["ウォーキングデッド", "アントラージュ","ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]

for i in drama_list:
    print(i)

# 2

for i in range(25, 51):
    print(i)


# 3

n = 0
for i in drama_list:
    print(n)
    print(drama_list[n])
    n += 1

# もしくわ

for i, show in enumerate(drama_list):
    print(i)
    print(show)

# 4

correct_answer = [2,5,9]

while True:
    try:
        num = input("一桁の数字を予想して入力してください。終了するには q をタイプしてください。：")
        if num == "q":
            break
        else:
            input_num = int(num)
            for i,answer in enumerate(correct_answer):
                if input_num == answer:
                    print("正解です。")
                    break

                elif i <=1:
                    continue

                else:
                    print("不正解です。")

    except ValueError:
        print("数字を入力するか、qで終了します。")

# もっとスマート書ける。

while True:

    num = input("一桁の数字を予想して入力してください。終了するには q をタイプしてください。：")

    if num == "q":
        break

    try:
        input_num = int(num)

    except ValueError:

        print("数字を入力するか、qで終了します。")
        continue

    if input_num in correct_answer:
        print("正解です。")

    else:
        print("不正解です")

# 5

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for num1 in list1:
    for num2 in list2:
        list3.append(num1*num2)

print(list3)