# 列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 访问列表元素
print(bicycles[0])
print(bicycles[1])
# 负值 倒索引
print(bicycles[-1])

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 修改元素
motorcycles[0] = 'ducati'
print(motorcycles)
# 添加元素
motorcycles.append("aaa")
print(motorcycles)

motorcycles = []
motorcycles.append("aaa")
motorcycles.append("bbb")
motorcycles.append("ccc")

print(motorcycles)
# 指定位置添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "aaa")
print(motorcycles)

# 列表中删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]  # 使用del的前提是得知道元素所在的索引位置
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# 使用pop弹出元素 还可以指定位置弹出元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# 根据值删除元素 remove()
motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.remove("aaa")
motorcycles.remove("honda")
# 方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
print(motorcycles)

# 组织列表 永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort();
print(cars);

# 临时性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# reverse永久性反向排序 cars.reverse()返回值为none 注意是有返回值的
cars.reverse()
print(cars)
cars.reverse()
print(cars)
# len返回长度
print(len(cars))
