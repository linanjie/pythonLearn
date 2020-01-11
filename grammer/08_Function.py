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
