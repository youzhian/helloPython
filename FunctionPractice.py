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



# 函数返回多个值
import math
def mevo(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 是用mevo(x,y,step,angle)函数
print("执行mevo(100,100,60,math.pi/6) is ",mevo(100,100,60,math.pi/6))

#自定义函数，求 ax^2+bx+c=0的两个解
def quadratic(a,b,c):
    q = math.sqrt((b*b - 4*a*c))
    x1 = (-b + q)/(2*a)
    x2 = (-b - q)/(2*a)
    return x1,x2
print("执行quadratic(4,30,-3) is ",quadratic(4,30,-3))
print(quadratic(2,3,1))
print(quadratic(1,3,-4))

def power(x,n=2):
    s = 1
    i = 1
    if(n < 1):
        raise TypeError("参数n必须大于等于1")
    if(n == 1):
        return s
    while i <= n :
        i = i+1
        s = s*x
    return s

print("执行power(4) = ",power(4))
print("执行power(4,3) = ",power(4,3))
print("执行power(4,1) = ",power(4,1))
#print("执行power(4,-3) = ",power(4,-3))

def enroll(name,grander,age=6,city="海口"):
    print("name:",name)
    print("grander:",grander)
    print("age:",age)
    print("city:",city)

print("执行enroll('张三','三年级') = ",enroll("张三","三年级"))
print("执行enroll('张三','三年级',city='北京') = ",enroll("张三","三年级",city="北京"))
print("执行enroll('张三','三年级',7) = ",enroll("张三","三年级",7))
print("执行enroll('张三','三年级',7，,'深圳') = ",enroll("张三","三年级",7,"深圳"))
print()
#print("执行完善后的myAbs2(x)，myAbs2('a') is",myAbs2('a'))

# 函数的参数

def add_end(L=[]):
    L.append("end")
    return L

print("执行add_end([1,3,5]) = ",add_end([1,3,5]))
print("执行add_end([1,3,7]) = ",add_end([1,3,7]))
print("执行add_end() = ",add_end())
print("执行add_end() = ",add_end())
print()

#设置参数为不可变参数
def add_end2(L=None):
    if L is None:
        L = []
    L.append("end")
    return L

print("执行add_end2([1,3,5]) = ",add_end2([1,3,5]))
print("执行add_end2([1,3,7]) = ",add_end2([1,3,7]))
print("执行add_end2() = ",add_end2())
print("执行add_end2() = ",add_end2())
print()

# 不定长参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print("执行calc(1,2,3) = ",calc(1,2,3))
print("执行calc(1) = ",calc(1))
print("执行calc(4,4) =",calc(4,4))
print("执行calc() =",calc())
nums = [1,2,3]
nums2 = (1,2,3)
print("将list作为不定参数传入 =",calc(*nums))
print("将tuple作为不定参数传入 =",calc(*nums2))
print()

# 传入关键字，可以已输入0或任意个参数
def person(name,age,**kw):
    print("name:",name,"age:",age,"other:",kw)

print("person('Jhone','30') = ",person("Jhone",30))
print("person('Bob',23,city='BeiJin') = ",person("Bob",23,city="BeiJin"))
print("person('Adam', 45, gender='M', job='Engineer') =",person('Adam', 45, gender='M', job='Engineer'))
print()

def person2(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print("name:", name, "age:", age, "other:", kw)

print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

# 关键字参数
def person3(name,age,*,city,job):
    print(name,age,city,job)

print(person3("HA",23,city="BeiJin",job="IT"))

def person4(name,age,*args,city,job):
    print(name,age,args,city,job)

print(person4("AM",34,2,"test",city="BeiJin",job="IT"))

def person5(name,age,*,city="BeiJin",job):
    print(name,age,city,job)

print(person5("TY",44,job="IT"))

def f1(a,b,c=0,*args,**kw):
    print("a=",a," b=",b," c=",c," args=",args," kw=",kw)

def f2(a,b,c=0,*,d,**kw):
    print("a=", a, " b=", b, " c=", c, " d=",d, " kw=", kw)

print()
print(f1(1,2))
print(f1(1, 2, c=3))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99))
print(f2(1, 2, d=99, ext=None))
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))
print()

print("=============递归函数==============")
# 阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print("执行fact(10) = ",fact(10))
print("执行fact(1) = ",fact(1))
print("执行fact(5) = ",fact(5))
# 栈溢出
#print("执行fact(1000) = ",fact(1000))