n = int(input("請輸入i :"))
for i in range(n,0,-1):
    print("第",i,"層外部迴圈，第",i,"層外部迴圈",end="")
    for j in range (i,0,-1):
        print("*",end="")
    print()