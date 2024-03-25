money = 0
list1 = []
while (money >= 0):
    money = int(input("請輸入支出:"))
    list1.append(money)
list1.pop()
print("總支出%d筆"%len(list1))
print("最高支出:%d"%max(list1))
print("最低支出:%d"%min(list1))
print("總支出%d"%sum(list1))
print("支出由小到大:{}".format(sorted(list1,reverse=False)))