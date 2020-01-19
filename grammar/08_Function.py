# 函数定义格式
def greet_user():
    # 三引号是文档字符串引用
    """ 显示简单的问候语 """
    print("Hello!")

greet_user()

# 传参方式 位置实参 参数顺序要一致 关键字实参，键值对的形式，直接指定参数值
def describe_pet(animal_type, pet_name):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 位置实参调用方法
describe_pet(animal_type="aaa",pet_name="hahaha")
# 设定默认值形式 如果显式地提供了实参，Python将忽略这个形参的默认值
# 注意 　使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让 Python 依然能够正确地解读位置实参。
def describe_pet(pet_name, animal_type='dog'):
    """ 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
# 传递列表副本 使用切片法   listed[:]
# 传递任意数量的形参
def make_pizza(*toppings):
    """ 打印顾客点的所有配料 """
    print(toppings)
make_pizza("pepperoni")
make_pizza("mushroom","green peppers","extra cheese")
# 带*的形参其实是一个空元组
# 接收任意数量的形参放在最后 位置实参和关键字实参放在前面

# 接收任意数量的关键字键值对
def build_profile(first,last,**user_info):
    """ 创建一个字典，其中包含我们知道的有关用户的一切 """
    user = {}
    user['first_name'] = first
    user['last_name'] = last
    for key,val in user_info.items():
        user[key] = val
    return user

# 导入文件模块py import pizza
# import pizza
# pizza.make_pizza(16, 'pepperoni') 模块名.函数名
# 导入模块中特定的函数 这种方式函数调用时无需使用句点调用
# 1. from 模块名 import 函数名
# 2. from 模块名 import 函数名1，函数名2，函数名3

# 使用别名as的函数  也可以给模块起别名
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# from module_name import function_name as fn

# 使用星号（ * ）运算符可让 Python 导入模块中的所有函数：from pizza import *
# 尽量使用 模块.函数名() 这样即使函数名有重复的也不会导致覆盖影响使用
# 如果形参很多，导致函数定义的长度超过了
#    79 字符，可在函数定义中输入左括号后按回车键，并在下一行按两次 Tab 键，从而将形参列表和只缩进一层的函数体区分开来。
