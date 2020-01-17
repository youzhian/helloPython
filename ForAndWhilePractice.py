# -*- coding:utf-8 -*-
print("1 + 2 + 3 =", 1 + 2 + 3)

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ["Dave", "Lisa", "Jhone", "Ilis"]
for name in names:
    print("name is",name)
# 求和
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print("1到10的和为：",sum)

# 可以通过range()函数创造数组，如range(5)会得到[0,5)的整数序列，即0,1,2,3,4 list()函数可以将其转为数组
# 计算1到100的和,用range()生成序列
sum = 0
for x in range(101):
    sum = sum + x
print("1到100的和：",sum)

# 第二种循环 while循环
# 计算100以内的奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print("100以内奇数之和：",sum)

# 练习 ，遍历名称，打印出 Hello ,xxx
# for循环方式实现
print("for循环方式实现：")
for name in names:
    print("Hello,", name)
# while 循环方式
print("while循环方式实现：")
index = 0
while index < len(names):
    print("Hello,", names[index])
    index = index + 1

# break
n = 1
while n <= 100:
    print(n)
    n = n + 1
print("End")

# 使用break
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print("End")

# continue的使用,打印10以内的奇数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
print("End")