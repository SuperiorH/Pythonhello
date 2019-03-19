"""
字典类似Java中的Map和Set
"""
# 字典类似Java中的Map
# 用字典表达映射关系
empty_dict = {}
# 初始化的字典
filled_dict = {"one": 1, "two": 2, "three": 3}
filled_dict.update({"six": 6})
print(filled_dict)

# 用[]取值
print(filled_dict["three"])

# 用 keys 获得所有的键。
# 因为 keys 返回一个可迭代对象，所以在这里把结果包在 list 里。我们下面会详细介绍可迭代。
# 注意：字典键的顺序是不定的，你得到的结果可能和以下不同。
list(filled_dict.keys())
print(filled_dict.keys())

# 用values获得所有的值。跟keys一样，要用list包起来，顺序也可能不同。
print(filled_dict.values())

# 用in测试一个字典是否包含一个键
print("one" in filled_dict)  # => True
print(1 in filled_dict)  # => False

# 访问不存在的键会导致KeyError
# filled_dict["four"]   # KeyError

# 用get来避免KeyError
print(filled_dict.get("one"))  # => 1
print(filled_dict.get("four"))  # => None

# 当键不存在的时候get方法可以返回默认值
print(filled_dict.get("one", 4))  # => 1
print(filled_dict.get("five", 5))  # => 4

# setdefault方法只有当键不存在的时候插入新值
filled_dict.setdefault("five", 5)  # filled_dict["five"]设为5
filled_dict.setdefault("five", 6)  # filled_dict["five"]还是5

print(filled_dict)

# 字典赋值
filled_dict.update({"four": 4})
filled_dict["four"] = 44  # 另一种赋值方法
print(filled_dict)

# 用del删除
del filled_dict["one"]  # 从filled_dict中把one删除
print(filled_dict)

# 用set表达集合
empty_set = set()
# 初始化一个集合，语法跟字典相似。
some_set = {1, 1, 2, 2, 3, 4}  # some_set现在是{1, 2, 3, 4}
print(some_set)

# 可以把集合赋值于变量
filled_set = some_set

# 为集合添加元素
filled_set.add(5)  # filled_set现在是{1, 2, 3, 4, 5}
print(filled_set)

# & 取交集
other_set = {3, 4, 5, 6}
print(filled_set & other_set)  # => {3, 4, 5}

# | 取并集
print(filled_set | other_set)  # => {1, 2, 3, 4, 5, 6}

# - 取补集
print({1, 2, 3, 4} - {2, 3, 5})  # => {1, 4}
print({1, 2, 3, 4} - {2, 3, 4, 5})  # => {1}

# in 测试集合是否包含元素
print(2 in filled_set)  # => True
print(10 in filled_set)  # => False
