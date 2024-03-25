fruits = ["香蕉","蘋果","橘子","鳳梨","西瓜"]
while True:
    i = input("請輸入水果:")
    if (i==""):
        break
    n = fruits.count(i)
    if(n>0):
        print("水果是第%d項"%fruits.index(i))
    else:
        print("沒有!")