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