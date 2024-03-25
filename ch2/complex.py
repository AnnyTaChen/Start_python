year = float(input("請輸入時間:"))
benefit = float(input("請輸入利率:"))
firstmoney = float(input("請輸入本金:"))
#firstmoney = firstmoney*((1+benefit)**year)
firstmoney *= (1+benefit)**year
print("六年後本金為:",firstmoney)