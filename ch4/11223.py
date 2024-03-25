n = int(input("請輸入正數:"))
x = 0
for i in range(2,n):
    if n % i == 0:
        x += 1
        print("因數有:",i)
if x == 0:
    print(n,"是質數")