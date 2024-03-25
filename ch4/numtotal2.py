sum = 0
a = int(input("請輸入數字:"))
for i in range(1,a+1):
    sum += i
print("1到%d總合為%d"% (a,sum))