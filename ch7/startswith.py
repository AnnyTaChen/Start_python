web = input("請輸入網址:")
if web.startswith("http://")  or web.startswith("https://"):
    print("網址輸入正確!")
else:
    print("網址輸入錯誤!")