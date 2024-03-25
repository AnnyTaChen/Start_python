dict1 = {"A":"內向穩重","B":"外向樂觀","O":"堅強自信","AB":"聰明自然"}
name = input("請輸入血型:")
blood = dict1.get(name)
if blood == None:
    print("沒有["+ name +"]此血型!")
else:
    print(name + "血型個性為" + str(dict1[name]))