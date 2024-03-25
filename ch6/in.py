dict1 = {"林小明":85,"曾山水":93,"黃明士":81}
name = input("請輸入姓名:")
if name in dict1:
    print(name + "的成績是" + str(dict1[name]))
else:
    score = input("請輸入成績:")
    dict1[name]=score
    print("字典內容" + str(dict1))