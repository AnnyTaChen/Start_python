animals = ["鼠","牛","虎","兔","龍","蛇","馬","羊","猴","雞","狗","豬"]
while True:
    i = int(input("請輸入出生年分:"))
    if (i==""):
        break
    p =  i % 12
    if (p>0):
        print("%4d年出生數%s"%(i,animals[p-1]))
    else:
        print("%4d年出生數%s"%(i,animals[11]))