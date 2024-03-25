dict1 = {"金牌":26,"銀牌":34,"銅牌":30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("%2s有%2d面"%(listkey[i],listvalue[i]))