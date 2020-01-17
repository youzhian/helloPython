# -*- coding: utf-8 -*-

age = 20
if age >= 18:
    print("your age is",age)
    print("adult")
# elif是 else if的缩写
age = 3
print("your age is",age)
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")

# 使用input()与int()
s = input("你的出生年份：")
brith = int(s)
if brith < 2000:
    print("00前")
else:
    print("00后")

# 练习题，小明身高1.75m，体重80kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数得到结果
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
xmHeigth = 1.75
xmWeigth = 80
xmBMI = xmWeigth/xmHeigth**2
# 判断结果
if xmBMI < 18.5:
    result = "过轻"
elif xmBMI <= 25:
    result = "正常"
elif xmBMI <= 28:
    result = "过重"
elif xmBMI <= 32:
    result = "肥胖"
elif xmBMI > 32:
    result = "严重肥胖"
print("小明身高为：", xmHeigth, "，体重为：", xmWeigth, "，其BMI值为：", xmBMI, "评判结果为：", result)
