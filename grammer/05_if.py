# if基本语法
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    # lower和upper函数不会改变原有值
    if car == 'toyota':
        print(car.upper())
    else:
        print(car.lower())
# python中的短路与和短路或 and or
age0 = 22
age1 = 18
print(age0 >= 21 and age1 >= 21)
print(age0 >= 21 or age1 >= 21)
# in 检查特定值是否在列表中 反向 not in
# if结构
# if:
# else:
# if elif else
# if:
# elif:
# else:
# Python并不要求if-elif 结构后面必须有else 代码块。在有些情况下，else 代码块很有用；而在其他一些情况下，使用一条elif 语句来处理特定的情形更清晰
# 5.4