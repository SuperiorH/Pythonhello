""" 多行字符串用三个引号
    包裹，也常被用来做多
    行注释
"""
"""
字符串和None
"""
# 字符串用单引双引都可以
print("这是个字符串")
print('这也是个字符串')

# 用加号连接字符串
print("Hello" + " World!")

# 字符串可以被当作字符列表
a = "JoeH"
print(a[0])

# 用.format来格式化字符串 用{}
b = "{} can be {}".format("String", "interpolated")
print(b)

# 可以重复参数以节省时间
c = "{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")
print(c)

# 如果不想数参数，可以用关键字
d = "{name} wants to eat {food}".format(name="Bob", food="lasagna")
print(d)

# None 是一个对象
e = None
print(e)

# 当与None进行比较时不要用 ==，要用is。is是用来比较两个变量是否指向同一个对象。
print(e is None)

# None，0，空字符串，空列表，空字典都算是False
# 所有其他值都是True
print(bool(0))  # => False
print(bool(""))  # => False
print(bool([]))  # => False
print(bool({}))  # => False
