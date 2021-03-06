# 类似于java map
# 字典中的键值的值对应任何python对象 字典是动态结构，可以添加键值对
alien = {'color': 'green', 'points': 5}
alien['x_position'] = 0
alien['y_position'] = 1
print(alien)

# 删除键值对 必须指明要删除的字典名以及对应的键的名字
del alien['x_position']
print(alien)
# 遍历字典
user = {
    "username": "efemi",
    'firstname': 'enrico',
    'last': 'fermi',
}
for key, value in user.items():
    print("\nKey:" + key)
    print("Value:" + value)

# 遍历所有键 以下两种形式
# 如果显式地使用方法 keys() 可让代码更容易理解，你可以选择这样做，但如果你愿意，也可省略它。
for key in user.keys():
    print(key)
for key in user:
    print(key)

# 键值按照指定顺序排列顺序 sorted返回已有键值列表的排序副本
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
# 字典所有值集合 values()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
# 针对重复项筛选保证不重复唯一 使用set（）函数
for language in set(favorite_languages.values()):
    print(language.title())

# 嵌套 字典嵌套列表 列表嵌套字典 字典嵌套字典
# 字典列表
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
    print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))
# 字典中存储列表
# 存储所点比萨的信息
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], }
# 概述所点的比萨
for topping in pizza['toppings']:
    print("\t" + topping)
# 双重循环字典中的列表值
favorite_languages = {'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby', 'go'],
                      'phil': ['python', 'haskell'], }
# 双重循环
for name,languages in favorite_languages.items():
    for language in languages:
        print("\t"+language)

# 字典中存储字典 略


