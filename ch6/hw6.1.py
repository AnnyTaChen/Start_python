dicts = {1:"JAN",2:"FEB",3:"MAR",4:"APR",5:"MAY",6:"JUN",7:"JUL",8:"AUG",9:"SEP",10:"OCT",11:"NOV",12:"DEC"}
n = input("請輸入月份:")
if n in dicts:
    print("%d:%s"%((n),dicts[n]))