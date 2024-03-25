import random

while True:
    inkey = input("按任意鑑再按enter")
    if len(inkey)>0:
        num = random.randint(1,6)
        print("點數為"+str(num))
    else:
        print("結束!")
        break