a = int(input("請輸入年分:"))
b = a % 100
c = a % 4
if (b == 0):
    if (c == 0):
        print("今年是閨年!")
    else:
        print("今年是平年!")
else:
    if (c == 0):
        print("今年是閨年!")