# 读文件
# 函数open() 返回一个表示文件的对象。在这里，open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象
# Python将这个对象存储在file_object
with open('D:\pdf\pi_digits.txt') as file_object:
    # read()方法将读取的字符串返回变量中，并打印
    contents = file_object.read()
    print(contents)
    # read()会返回最后有一个空行 read()到达文件末尾时会返回一个空字符串 显示出来就是一个空行
    print(contents.rstrip())
    # 关键字with在不再需要访问文件后将其关闭
    # 注意到我们调用了open()，但没有调用close()；你也可以调用open()和close()来打开和关闭文件，但这样做时，
    # 如果程序存在bug，导致close()语句未执行，文件将不会关闭
    # 并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可 让Python去确定：你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。

# 妥善处理文件中的每一行
filename = "D:\pdf\pi_digits.txt"
with open(filename) as file_object:
    for line in file_object:
        # print(line)
        print(line.rstrip())  # 去掉空白行

with open(filename) as file_object:
    # 方法readlines() 从文件中读取每一行，并将其存储在一个列表中；在with 代码块外，我们依然可以使用这个变量
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # print(line.rstrip())
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

# 读文本文件时python默认读取为字符串 如果需要数值转化 用int()或者float()
# 对于你可处理的数据量，Python没有任何限制；只要系统的内存足够多，你想处理多少数据都可以

# python写入文件
filename = "D:\eee.txt"
# 可指定读读取取模模式式 （'r' ）、写写入入模模式式 （'w' ）、附附加加模模式式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）。
with open(filename, 'w') as file_object:
    # Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str() 将其转换为字符串格式。
    file_object.write("I love programme.\n")
    # 还可以包含换行符
    file_object.write("I love programme.")

# 附加模式
with open(filename, 'a') as file_object:
    file_object.write("\nshe is very good")

# 处理异常
try:
    print(5 / 0)
except ZeroDivisionError:
    print("you can't divide by zero!")

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_num = input("\nFirst num:")
#     if first_num == 'q':
#         break
#     second_num = input("\nsecond_num:")
#     if second_num == 'q':
#         break
#     try:
#         answer = print(int(first_num) / int(second_num))
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     print(answer)

# FileNotFoundError 异常
# try 对应的else模块仅当try 代码块成功执行时才执行它们
# 失败时跳过
#     except ZeroDivisionError:
#         pass

# 存储数据 json形式
import json
numbers = [2,3,5,6,8,9]
filename = 'D:\\numbers.json'
with open(filename,'w') as f_object:
    json.dump(numbers,f_object)# json api

with open(filename) as f_object:
    numbers = json.load(f_object)# json api
    print(numbers)