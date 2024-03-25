str1 = 'hello world'
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mind the stop
arr2 = arr1[0:5]
# -1 represent the last element
arr3 = arr1[0:-1:2]
# you can ignore the args...
arr4 = arr1[:]

print(arr2)
print(arr3)
print(arr4)
print(arr4 is arr1)
print(str1[5:])