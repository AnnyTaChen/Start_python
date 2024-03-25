person = int(input("請輸入人數:"))
apple = int(input("請輸入蘋果數:"))
left = divmod(apple,person)
print("%d人可以拿到%d蘋果，剩下%d顆蘋果"%(person,left[0],left[1]))