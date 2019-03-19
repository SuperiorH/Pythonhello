from collections import OrderedDict, Counter

# 1、ALL OR ANY
from emoji import emojize

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