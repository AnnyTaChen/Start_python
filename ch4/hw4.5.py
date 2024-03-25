n = int(input("請輸入正數:"))
for i in range(2,n-1):
    if n % i == 0:
        print("因數有:",i)
        
    