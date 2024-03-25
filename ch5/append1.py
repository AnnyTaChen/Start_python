scores = []
total = inscore = 0
while (inscore >= 0):
    inscore = int(input("請輸入學生成績:"))
    if (inscore >= 0):
        scores.append(inscore)
print("共有%d位學生"% len(scores))
for i in scores:
    total += i
average = total / (len(scores))
print("本般總成績:%3d, 總平均為%5.2f"%(total,average))