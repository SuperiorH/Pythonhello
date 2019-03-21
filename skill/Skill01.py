import uuid
from collections import OrderedDict, Counter
from emoji import emojize

# 1、ALL OR ANY
import requests
import pprint

import wikipedia as wikipedia

x = [True, True, False]
print(any(x))
print(all(x))
print(any(x) and not all(x))

# 2、控制台绘图
# $ pip install bashplotlib
# 现在 你的控制台就可以有图了

# 3、Collections
# Remembers the order the keys are added!(有序的字典)
x = OrderedDict(a=1, b=2, c=3)
print(x)
# Counts the frequency of each character(计数的字典)
y = Counter("JoeHH")
print(y)

# 4、DIR 面对一个Python对象，你是否曾想过可以直接看到其属性？你也许可以试试以下的代码:
a = dir("Hello World!")
print(a)

# 5、创建表情包
print(emojize(":thumbs_up:"))

# 6、GEOPHY
# place = "221b Baker Street, London"
# location = GoogleV3().geocode(place)
# print(location.address)
# print(location.location)

# 7、HOWDOI

# 8、INSPECT
# import inspect
# print(inspect.getsource(inspect.getsource))
# print(inspect.getmodule(inspect.getmodule))
# print(inspect.currentframe().f_lineno)

# 9、JEDI
# jedi库是一个代码自动补齐和静态分析的库。它可以使你更快更高效地书写代码。

# 10、**KWARGS
# 双星“**”放在字典的前面可以让你将字典的内容作为命名参数传递给函数。字典的键是参数的名字，键的值作为参数的值传递给函数。如下所示:
dictionary = {"a": 1, "b": 2}


def someFunction(a, b):
    print(a + b)
    return


# these do the same thing:
someFunction(**dictionary)
someFunction(a=1, b=2)

# 11、LIST COMPREHENSIONS 列表推导式
numbers = [1, 2, 3, 4, 5, 6, 7]
evens = [x for x in numbers if x % 2 is 0]
odds = [y for y in numbers if y not in evens]
cities = ['London', 'Dublin', 'Oslo']


def visit(city):
    print("Welcome to " + city)


for city in cities:
    visit(city)

# 12、MAP Python有许多非常有用的内置函数。其中一个就是map()——特别是和lambda函数相结合的时候。
x = [1, 2, 3]
y = map(lambda x: x + 1, x)
# prints out [2,3,4]
print(list(y))
# 在这个例子中，map()对x中的每一个元素都应用了一个简单的lambda函数。它会返回一个map对象，这个对象可以被转化成可迭代对象，如列表或者元组。

# 13、PPRINT
# Python的默认print函数可以满足日常的输出任务，但如果要打印更大的、嵌套式的对象，那么使用默认的print函数打印出来的内容会很丑陋。
url = "https://randomuser.me/api/?results=1"
users = requests.get(url).json()
pprint.pprint(users)

# 14、UUID
user_id = uuid.uuid4()
print(user_id)

# 15、WIKIPEDIA
# Wikipedia有一个很棒的API，它可以让用户通过编程访问到维基的词条内容。使用Python中的wikipedia模块可以让你以最便捷的方式访问该API。
# result = wikipedia.page("freeCodeCamp")
# print(result.summary)