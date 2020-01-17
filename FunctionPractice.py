# -*- coding: utf-8 -*-
# 函数
print("=============函数=============")
r1 = 3.4
r2 = 4
r3 = 5.7
PI = 3.1415
s1 = PI * r1**2
print("半径为：", r1," 的圆的面积为：", s1)
# 可以在交互式命令窗口中输入 help(abs)查看，也可以到官网查看：http://docs.python.org/3/library/functions.html#abs
print("abs(100) is", abs(100), ",abs(-20) is", abs(-20), ",abs(2.41) is", abs(2.41))
# 而max函数max()可以接收任意多个参数，并返回最大的那个,参数个数不能小于1
print("max(1, 2, 3) is", max(1, 2, 3))
print("max(1, 2) is", max(1, 2))
# 有多个内置函数 int()、float()、str()、bool()
print("int(2.3) is", int(2.3))
print("float(3) is", float(3),"float(2.5) is", float(2.5))
print("str(12.3) is", str(12.3))
print("bool(1) is", bool(1), ",bool('') is", bool(''), ",bool(2) is", bool(2), ",bool(0) is", bool(0), ",bool('a') is"
      , bool('a'), ",bool(-1) is", bool(-1), ",bool(True) is", bool(True))
# 还可以把函数赋值给变量，相当于是给函数取别名
a = abs
print("取别名后的a(-30.3) is", a(-30.3))
# hex() 将数值转为十六进制字符串
print("hex(255) is", hex(255))
print("hex(1000) is", hex(1000))

# 自定义函数
print("\n=========自定义函数=========\n")
print("自定义函数 myAbs(x)")
def myAbs(x):
    if x < 0:
        return -x
    else:
        return x

print("调用自定义的绝对值函数，myAbs(-394) is", myAbs(-394))
# 若没有return,函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return

# 空函数,如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass
print("执行nop()",nop())
# pass可以作为占位符，若还没想好某分支该做什么，可以使用pass 例如
# if a < 18:
#     pass
# 完善myAbs()函数
def myAbs2(x):
    if not isinstance(x,(int,float)):
        raise TypeError("参数类型只能为int或float类型")
    if x < 0:
        return -x
    else:
        return x

print("执行完善后的myAbs2(x)，myAbs2('a') is",myAbs2('a'))

# 函数返回多个值
import math
def mevo(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 是用mevo(x,y,step,angle)函数
print()
