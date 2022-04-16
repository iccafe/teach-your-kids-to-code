print("我能知道你的年龄：")
print("把你的生日的月份乘以4")
print("把上面结果加9")
print("把上面结果乘以25")
print("把上面结果加上生日的日期")

n = int(input("你算出来的结果是多少？请输入:\n"))

month = (int(n)-225) // 100 #月份
date = (int(n) -225 - month * 100 ) #日期

if n < 326:
    print ("你应该算错了，数字太小了")
    exit()

if month in [1,3,5,7,8,10,12] and date > 31:
    print("您应该算错了，日期不能大于31.")
elif month == 2 and date > 29:
    print("有没有可能算错了，2月不可能大于29")
elif month in [4,6,9,11] and date >30:
    print("您应该算错了，这个月没有31日")

else:
    print("你的生日是",month,"月",date,"日")
