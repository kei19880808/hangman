#1

my_favorite_musicans = ["Chemistry","Kenshi Yonezu","Kinki Kids"]

print(my_favorite_musicans)

#2

hakata_station = (33.590045,130.420611)
ueno_zoo = (35.716454,139.771318)
kaikyokan = (33.954592,130.942467)

#3

my_personality = {"Eye_color":"Black","Height":'165cm',"Weight":'55kg'}

#4

n = input('人間の特徴を表す言葉を英語で入力してください。:')
if n in my_personality:
    personality = my_personality[n]
    print(personality)
else:
    print("その特徴は登録されていません。もう一度別の特徴を入力してください。")

#5

my_favorite_songs = {"Chemistry":["two","meaning of tears"],
                     "Kenshi Yonezu":['Lemon',"Uchiage Hanabi"],
                     "Kinki Kids":["薄荷キャンディー","ガラスの少年"]}

print(my_favorite_songs)

