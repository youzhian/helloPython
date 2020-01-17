#!/usr/bin/env python3
# 用于告诉系统文件所使用的编码
# -*- coding: utf-8 -*-
a = 'ABC'
b = a
a = "XYZ"
print('a =',a,' b =',b)

# 转换函数
# ord()是获取字符的整数表示的函数
print('ord(\'A\') is ',ord('A'))
print('ord("中") is',ord("中"))
# chr()是将编码转为对应字符的函数
print('chr(65) is',chr(65))
print("chr(20013) is",chr(20013))
# 字符串整数编码的十六进制
print('\u4e2d\u6587')
# 编码
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
print(x)
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
# 转为ascii码
print('"ABC.encode(\'ascii\')" is','ABC'.encode('ascii'))
# 转为utf-8
print('"ABC.encode(\'utf-8\')" is','ABC'.encode('utf-8'))
print("'中文'.encode('utf-8') is","中文".encode("UTF-8"))
# "中文".encode('ascii') 会报错，因为中文超出了ascii编码范围
# decode() 将bytes转为字符
print("b'ABC'.decode('ascii') is",b"ABC".decode("ASCII"))
print("b'ABC'.decode('utf-8') is",b"ABC".decode("utf-8"))
print("b'\\xe4\\xb8\\xad\\xe6\\x96\\x87'.decode('utf-8') is",b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))
# 如果bytes中包含无法解码的字节，decode()方法会报错 如 b'\xe4\xb8\xad\xff'.decode('utf-8')
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print("b'\\xe4\\xb8\\xad\\xff'.decode('utf-8',errors='ignore') is",b'\xe4\xb8\xad\xff'.decode("utf-8",errors="ignore"))

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print("len('ABC') is",len("ABC"))
print("len('中文') is",len("中文"))
print("len(b'ABC') is",len(b"ABC"))
print("len(\"b'\\xe4\\xb8\\xad\\xe6\\x96\\x87') is",len(b'\xe4\xb8\xad\xe6\x96\x87'))
print("len('中文'.encode('utf-8')) is",len("中文".encode("utf-8")))

# 格式化
# %d 表示 整数
# %f 表示 浮点数
# %s 表示 字符串
# %x 表示 十六进制整数
print("Hello ,%s" % "world")
print("Hi, %s you have $%d. or $%f" %("Jhone",1000,1000))
print("%2d-%02d" % (3,1))
print("%.2f" % 3.1415926)
print("%03d" % ord("A"))
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print("age: %s. Gender:%s" % (20,True))
# 通过% 转译%
print("growth rate: %d %%" % 7)
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
print("Hello,{0},成绩提升了{1:.1f}".format("小明",17.2312))
s1 = 72
s2 = 85
r = (s2-s1)/s1 * 100
print("小明成绩由 72分提升到了85分，成绩提升了%.1f%%" % r)