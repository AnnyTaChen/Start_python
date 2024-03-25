a = int(input("請輸入年收入:"))
if (a >= 300000):
    if (a < 600000):
        print("付稅金額:",a*0.06,end="元/n")
    elif(a >= 600000 and  a< 1000000):
        print("付稅金額:",a*0.21,end="元/n")
    elif(a >= 2000000):
        print("付稅金額:",a*0.30,end="元/n")
else:
    print("免稅!")