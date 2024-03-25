colors = ["紅色","黃色","藍色","綠色","橙色"]
while True:
    print("此串列有",colors)
    nocolor = input("請輸入要移除的顏色:")
    if (nocolor ==""):
        break
    n = colors.count(nocolor)
    if (n>0):
        colors.remove(nocolor)
    else:
        print("序列裡沒此顏色!")