n = int(input("請輸入i :"))
for i in range(1,n+1):
    print("第",i,"層外部迴圈，第",i,"層外部迴圈",end="")
    for j in range (1,i+1,2):
        print("*",end="")
    print()