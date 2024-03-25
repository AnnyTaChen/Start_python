age = int(input("請輸入年齡:"))
if age>=18:
    print("全部可看")
elif age <= 18 and age >= 12:
    print("除了限制級其他都可看")
elif age <=12 and age >= 6:
    print("可看普遍級保護級")
else:
    print("只能看普遍級")