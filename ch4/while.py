
from re import I

total = i = 1
n = int(input("請輸入n:"))
while i <= n:
     total *= i
     i += 1
print("%d!=%d"%(n,total))#n!