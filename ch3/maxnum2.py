a = int(input("請輸入a:"))
b = int(input("請輸入b:"))
c = int(input("請輸入c:"))
if (a >= b):
    if (b >= c):
        print("最大為",a)
    elif(a <= c):
        print("最大為",c)
elif(a >= c):
    if (a <= b) :
        print("最大為",b)
    elif(c >= b):
        print("最大為",a)
elif(b>=c):
    if (a <= c):
        print("最大為",b)
else:
    print("最大為",c)
