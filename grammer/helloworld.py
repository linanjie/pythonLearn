message="aaa";
print(message)

name = "This is a string"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name+" "+last_name
print(full_name)
print("Hello, "+full_name.title()+"!")

print("Python")
print("\tPython")

print("Languages:\n\tPython\n\tC\n\tJavaScript")
# 要确保字符串末尾没有空白，可使用方法rstrip() lstrip() 和strip()
favourite = "Python "
print(favourite.rstrip())
favourite = favourite.rstrip()
print(favourite)

message = "One of Python's strengths is its diverse community."
print(message)

# message = 'One of Python's strengths is its diverse community.'
# print(message)

# 函数str()字符串化
age = 23 #针对整形需要额外进行字符串处理
message = "Happy " + str(age) + "rd Birthday!"
print(message)

