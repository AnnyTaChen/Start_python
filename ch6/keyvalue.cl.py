stars = {"摩羯座":"刻苦耐勞","水瓶座":"古靈精怪","雙魚座":"天真爛漫","獅子座":"死要面子"}
char = input("請輸入星座:")
starkey = list(stars.keys())
starvalue = list(stars.values())
if char in stars:
    print(char+":"+str(stars[char]))
else:
    score = input("請輸入個性:")
    stars[char] = score
    print(char+":"+stars[char])