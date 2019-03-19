"""
变量和集合(列表、元组)
"""
# 在给变量赋值前不用提前声明
# 传统的变量命名是小写，用下划线分隔单词
some_var = 5

# 访问未赋值的变量会抛出异常
# 参考流程控制一段来学习异常处理
# print(some_unknown_var)  # 抛出NameError

# 用列表(list)储存序列
li = []
# 创建列表时也可以同时赋给元素
other_li = [4, 5, 6]
print(li)
print(other_li)

# 用append在列表最后追加元素
li.append(1)  # li现在是[1]
li.append(2)  # li现在是[1, 2]
li.append(4)  # li现在是[1, 2, 4]
li.append(3)  # li现在是[1, 2, 4, 3]
print(li)
# 用pop从列表尾部删除
li.pop()  # => 3 且li现在是[1, 2, 4]
print(li)
# 把3再放回去
li.append(3)  # li变回[1, 2, 4, 3]
print(li)

print(li[0])  # 第一个元素
print(li[-1])  # 最后一个元素
# print(li[4])  # 越界了 IndexError: list index out of range

# 列表有切割语法
print(li[1:3])  # => [2, 4]
# 取尾
print(li[2:])  # => [4, 3]
# 取头
print(li[:3])  # => [1, 2, 4]
# 隔一个取一个
print(li[::2])  # =>[1, 4]
# 倒排列表
print(li[::-1])  # => [3, 4, 2, 1]
# 可以用三个参数的任何组合来构建切割
# li[始:终:步伐]

# 用del删除任何一个元素
del li[0]  # li is now [1, 2, 3]
print(li)

# 列表可以相加
# 注意：li和other_li的值都不变
li1 = li + other_li  # => [2, 4, 3, 4, 5, 6]
print(li1)

# 用extend拼接列表
li.extend(other_li)  # li现在是[2, 4, 3, 4, 5, 6]
print(li)

# 用in测试列表是否包含值
print(4 in li)  # => True

# 用len取列表长度
print(len(li))  # => 6

# 元组是不可改变的序列
tup = (-1, -2, -3)
tup[0]  # => 1
print(tup[0])
print(len(tup))
print(tup + (4, 5, 6))
print(tup[:2])
print(-1 in tup)

# 可以把元组合列表解包，赋值给变量
a, b, c = (1, 2, 3)  # 现在a是1，b是2，c是3
# 元组周围的括号是可以省略的
d, e, f = 4, 5, 6
# 交换两个变量的值就这么简单
e, d = d, e  # 现在d是5，e是4
print(d)
print(e)
