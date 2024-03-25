import random
list=[]
for i in range(3):
    num = random.randint(1,6)
    list.append(num)
print(list)
print(sum(list))