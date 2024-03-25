fruits =["香蕉","蘋果","橘子","鳳梨","西瓜"]
while True:
    print("串列元素有:",fruits)
    i = input("請輸入要刪除的水果:")
    if (i==""):
        break
    n = fruits.count(i)
    if (n>0):
        fruits.remove(i)
    else:
        print(i,"不再串列中")