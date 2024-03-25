date1 = "2019-8-23"
date1 = "西元" + date1
date1 = date1.replace("-"," 年 ",1)
date1 = date1.replace("-"," 月 ",1)
date1 += "日"
print(date1)