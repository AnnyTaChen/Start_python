A = int(input("請輸入A:"))
B = int(input("請輸入B:"))
maxx = A*B
for i in range(1,maxx+1):
    if i%A == 0 and i%B == 0:
        break
print(i)