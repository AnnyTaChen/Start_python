innum=0
list1 = []
while (innum != -1):
    innum = int(input("請輸入電費:"))
    list1.append(innum)
list1.pop()
print("總共有%d筆電費"%len(list1))
print("最高電費為%4d元"%max(list1))
print("最低電費為%4d元"%min(list1))
print("電費由大到小為:{}".format(sorted(list1,reverse=True)))