# 列表遍历操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 复杂点的循环操作
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
# 在for 循环后面，没有缩进的代码都只执行一次，而不会重复执行。
print("Thank you, everyone. That was a great magic show!")

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 使用列表的一部分 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# 如果没有指定开头
print(players[:4])
# 没有指定结尾索引
print(players[1:])
# 输出最后三个
print(players[-3:])
# 遍历前三名 使用切片
for val in players[:3]:
    print(val)

# 使用切片进行列表复制
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)

# 使用切片可以完整复制一份列表，并分别对列表进行操作
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

