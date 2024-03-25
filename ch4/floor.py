A = int(input("請輸入樓層:"))
for i in range(1,A+1):
    if i % 10 == 4:
        continue
    print(i,end=" ")