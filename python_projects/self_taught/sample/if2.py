# if文の中にif

gakusei_syou = True
test_score = 98

if(gakusei_syou == True):
    if(test_score >50):
        if(test_score >= 70):
            print("学生証は確認できました。70点以上なのであなたの成績はAです。")

# and と　or

gakusei_syou = True
test_score = 80

if((gakusei_syou ==True) and (test_score >=70)):
    print('学生証を確認しました。テストの成績は70点以上なので合格です！')


test_score_english = 33
test_score_math = 92

if((test_score_english >=70) or (test_score_math >=70)):
    print("英語か数学のどちらか一方で70点以上なので合格！")

test_score_math =10
test_score_japanese =88
test_score_english= 32

if((test_score_japanese >= 70) and ((test_score_english >= 80) or (test_score_math >= 80))):
    print("合格です")
else:
    print("不合格です")