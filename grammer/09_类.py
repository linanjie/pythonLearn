# 类基本语法
class Dog():
    # __init__() 是一个特殊的方法，每当你根 据Dog 类创建新实例时，Python都会自动运行它
    # 在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突
    # 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
    # 创建Dog实例时，Python将调用Dog类的方法__init__()。我们将通过实参向Dog()传递名字和年龄；self会自动传递，
    # 因此我们不需要传递它。每当我们根据Dog类创建实例时，都只需给最后两个形参（name和age）提供值。
    def __init__(self, name, age):
        # 两个变量都有前缀self。以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over")


# 根据类创建实例
# 虽然__init__并未显式地包含return语句 python会自动返回一个对应的Dog实例
# 命名规则 大写创建类 小写是变量实例名
my_dog = Dog("aaa", "7")
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


#
class Car():
    """一次模拟汽车的简单尝试"""
    """初始化描述汽车的属性"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        """返回整洁的描述性信息"""

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


# 给属性设置默认值
class Car():
    def __init__(self, name, model, year):
        """初始化描述汽车的属性"""
        self.name = name
        self.model = model
        self.year = year
        #
        self.odometer_reading = 0

    # def get_descriptive_name(self):
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', 2016)
my_new_car.read_odometer()

# 修改属性值 通过实例 通过方法 通过方法递增
my_new_car.odometer_reading = 1
my_new_car.read_odometer()
# 通过方法修改
my_new_car.update_odometer(2)
my_new_car.read_odometer()

# 继承类
# 子类首先要初始化赋值父类的属性值
# 语法：def __init__(self, make, model, year):
# class ElectronicCar(Car):

# """初始化父类的属性"""
# super().__init__(make, model, year) 先初始化父类的属性 再给子类特有的属性赋值

# 9.3.4 重写父类方法 需要和原有的父类方法同名 这样python自动忽略子类方法
# 一个模块中导入多个类 / 导入整个模块 使用句点法使用函数 / 导入模块中的所有类 from module_name import *

# 子类和父类分开放置时，需要子类中引入父类的模块或者父类
# from car import Car
# class Battery(): --snip - -
# class ElectricCar(Car): --snip - -

# 使用python标准库
from collections import OrderedDict
favorite_language = OrderedDict()
favorite_language['1'] = 'a'
favorite_language['2'] = 'b'
favorite_language['3'] = 'c'
print(favorite_language)

# 类名 驼峰命名 模块和实例名 小写 下划线
# 对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文 档字符串，对其中的类可用于做什么进行描述
# 可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类
# 导入模块 先导入标准库 再导入三方和自用库

