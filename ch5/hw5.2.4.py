import numbers


numbers = [1,2,3,4,2,7,3,2,3]
numbers2 = sorted(numbers,reverse=False)
del numbers2[2:6]
print(numbers2)