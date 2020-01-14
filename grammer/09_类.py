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

my_new_car = Car('audi', 'a4', 2016)
my_new_car.read_odometer()

# 修改属性值

