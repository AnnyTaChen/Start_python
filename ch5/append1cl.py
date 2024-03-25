money = []
total = inmoney = 0
while (inmoney >= 0):
    inmoney = int(input("請輸入收入:"))
    if (inmoney >= 0):
        money.append(inmoney)
for j in money:
    total += j
print("總共存%5d元"%(total))