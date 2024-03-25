def  kgtolb(kg):
    b = kg *2.2
    return b 
inputkg = float(input("請輸入體重(公斤):"))
print("你的體重為:%5.1f磅"%kgtolb(inputkg))