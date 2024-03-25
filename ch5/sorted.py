scores = []
while True:
    inscore = input("請輸入學生成績:")
    if (inscore ==""):
        break
    scores.append(inscore)
scores2 = sorted(scores,reverse=True)
print(scores2)