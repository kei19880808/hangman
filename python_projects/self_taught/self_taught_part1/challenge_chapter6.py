# 1

name = "カミュ"
for i in range(3):
    print(name[i])

# 2

str1 = input("昨日何を書いた？:")
str2 = input("それを誰に送った？:")

str3 = "私は昨日{}を書いて、{}に送った！".format(str1,str2)
print(str3)

# 3

string = "aldous Huxley was born in 1894.".capitalize()
print(string)

# 4

string = "どこで？ だれが？ いつ？"
string = string.split(" ")
print(string)

# 5

string_list = ["The","fox","jumped","over","the","fence","."]
string = " ".join(string_list)
string = string[0:-2] + "."
print(string)

# 6

string = "A screaming comes across the sky."
string = string.replace("s","$")
print(string)

# 7

string = "Hemingway"
num = string.index("m")
print(num)

# 8

string = "Kenshiro said, \"You are already dead.\""
print(string)

# 9

string = "three " + "three " + "three"
print(string)
string = "three "*3
print(string)

#10

string = "四月のは晴れた寒い日で、時計がどっれも十三時を打っていた。"
string = string[0:11]
print(string)