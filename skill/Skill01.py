from collections import OrderedDict, Counter
from emoji import emojize

# 1、ALL OR ANY

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