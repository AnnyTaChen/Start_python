dict2 = {"春":"陽光明媚","夏":"炎熱","秋":"涼爽","冬天":"寒冷"}
weather = input("請輸入季節:")
feel = dict2.get(weather)
if ( feel == None ):
    print("錯誤!")
else:
    print(feel+":"+str(dict2[feel]))