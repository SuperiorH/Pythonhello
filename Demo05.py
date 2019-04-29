"""
流程控制和迭代器
"""
some_var = 10
if some_var < 10:
    print("{}小于10".format(some_var))
elif some_var > 10:
    print("{}大于10".format(some_var))
else:
    print("{}等于10".format(some_var))

# 用for循环语句遍历列表
my_list = ["dog", "cat", "pig"]
for i in my_list:
    print("{} is one kind of animal".format(i))

# while 循环
a = 0
while a < 4:
    print(a)
    a += 1

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # => dict_keys(['one', 'two', 'three'])，是一个实现可迭代接口的对象
for i in our_iterable:
    print(i)  # 打印 one, two, three

# 但是不可以随机访问
# our_iterable[1]  # 抛出TypeError

# 可迭代对象知道怎么生成迭代器
our_iterator = iter(our_iterable)

# 迭代器是一个可以记住遍历的位置的对象
# 用__next__可以取得下一个元素
our_iterator.__next__()  # => "one"

# 再一次调取__next__时会记得位置
our_iterator.__next__()  # => "two"
our_iterator.__next__()  # => "three"

# 当迭代器所有元素都取出后，会抛出StopIteration
# our_iterator.__next__() # 抛出StopIteration

# 可以用list一次取出迭代器所有的元素
print(list(filled_dict.keys()))  # => Returns ["one", "two", "three"]

# x = [True,True,False]
# print(any(x))
# print(all(x))
# print(any(x) and not all(x))