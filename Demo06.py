"""
函数
"""
def add(x, y):
    return x + y


print(add(1, 2))
print(add(y=7, x=8))


def varAggs(*args):
    init = 0
    for i in args:
        init += i
    return init

print(varAggs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def keyword_args(**kwargs):
#     return kwargs

v = (lambda x: x > 2)(3)
print(v)
li = filter(lambda x: x > 5, [3, 4, 5, 6, 7])
print(list(li))