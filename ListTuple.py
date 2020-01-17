# -*- coding: utf-8 -*-
# list
classmates = ['a','3','23']
print("classmates is",classmates)
print("len(classmates) is",len(classmates))
print("classmates[0] is",classmates[0])
# 获取最后一个元素的两种方式，len()可以计算list的长度
print("classmates last item is",classmates[len(classmates)-1])
# -1表示倒数第一个，-2表示倒数第二个，以此类推
print("classmates last item is",classmates[-1])
# list添加元素
classmates.append("Adam")
print("add Adam in classmates",classmates)
# 使用insert将元素插入到指定位置,若指定位置大于当前长度，则插入末尾
classmates.insert(5,"Tony")
print("befor insert",classmates)
# 使用-1会导致元素插入倒数第二的位置
classmates.insert(-1,"Devi")
print("insert index is -1",classmates)
# pop可以将元素删除
print("when classmates.pop()",classmates.pop(),classmates)
print("when classmates.pop(1)",classmates.pop(1),classmates)
print("when classmates.pop(1)",classmates.pop(0),classmates)
# list的值替换
classmates[1] = "Jhone"
print("when classmates[1] = 'Jhone'",classmates)

# list 的值可以是多种数据类型
L = ["Heny",123,30.1,True]
print("L is",L)
# 元素也可以为list
s = ['Monkey',"java",["asp","php"],"python"]
print("s is",s,"len(s) is",len(s))
# 想获取php元素可以写成s[2][1]，若元素不是数组而是字符串，则也会获取相应位置的字符
print("s[2][1] is",s[2][1],"s[1][1]",s[1][1])
p=["asp","php"]
s2 = ["12",34,p,"AS",True]
print("p is",p,"s2 is",s2)
# 若此时改变p的元素，s2也会跟着变化
p[1] = "JSP"
print("when change the p to",p,"s2 is",s2)
# 空list的长度为0，L = [] ,len(L) = 0

# tuple应用
# tuple为另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates2 = ("Devy","Jhone","Hony","Lisa")
print("classmates2 is",classmates2)
print("classmates2[1] is",classmates2[1])
# 定义空元组可以写成
t = ()
print(t)
# 若字定义一个元素的元组时，为避免歧义，应在后加","
t = (1,)
print(t)
t = ("ad",)
print(t)
classmates2 = ("Devy",)
print("classmates2 is",classmates2)