import random

list = random.sample(range(0,10),4)
list.sort()
print("大獎為:",end="")
for i in range(4):
    print(str(list[i]))