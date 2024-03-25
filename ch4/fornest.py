for i in range(1,6):
    print("第",i,"圈內向迴圈，第",i,"圈外向迴圈")
    for j in range(1,i+1):
        print("#",end="")
    print()