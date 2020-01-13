# 类基本语法
class Dog():
    # __init__() 是一个特殊的方法，每当你根 据Dog 类创建新实例时，Python都会自动运行它
    # 在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting")
    def roll_over(self):
        print(self.name.title()+" rolled over")

