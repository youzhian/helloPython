# -*- coding: utf-8 -*-
# dict和set的使用
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {"Dave":89,"HengLi":75,"LiLi":66}
print("d['Dave'] is",d["Dave"])
# 字典赋值可以用户 d[xxx] = 00
d["adam"] = 100
print("when add adam is",d)
# 如果key不存在，dict就会报错，为避免报错，可以使用in
print("'DSD' in d","DSD" in d)
# 或者使用get()，如果key不存在，可以返回None，或者自己指定的value：
print("d.get('adam') is", d.get("adam"))
print("d.get('xxx') is", d.get("xxx"))
print("d.get('xxx',-1) is", d.get("xxx", -1))
# 注意：返回None的时候Python的交互环境不显示结果。

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除，删除一个不存在的key会报错
print("删除前d为：", d)
print("d.pop('adam')", d.pop("adam"))
print("删除后d为：", d)
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的，key应为不可变类型，如字符串，和整数
print("\n=============set的使用===============\n")
# set的使用
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# set也是无序的
s = set([1, 2, 3])
print("set s is", s)
# 自动过滤重复的值
s = set([1, 2, 4, 3, 5, 2, 3, 4])
print("过滤重复值的s", s)
# 通过add(key)的方式为set增加元素，可以增加重复元素，但是实际上不会增加
s.add(7)
s.add(2)
print("执行add后的s ", s)
# 通过remove(key)可以删除元素
s.remove(1)
print("执行remove(1)后的s", s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 3, 5, 7])
s2 = set([2, 4, 7, 8, 3])
print("s1为", s1, "s2为", s2)
# 求交集
print("s1 & s2 is", s1 & s2)
# 求合集
print("s1 | s2 is", s1 | s2)
# 求差集
print("s1 ^ s2 is", s1 ^ s2)
