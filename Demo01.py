""" 多行字符串用三个引号
    包裹，也常被用来做多
    行注释
"""
"""
基本数据类型运算
"""
# 但是除法例外，会自动转换成浮点数
print(35 / 5)
print(5 / 3)

# 整数除法的结果都是向下取整
# 5 // 3     # => 1
# 5.0 // 3.0 # => 1.0 # 浮点数也可以
print(5 // 3)
print(5.0 // 3)

# 浮点数的运算结果也是浮点数
print(3 * 2.0)

# 模除
print(7 % 4)

# x的y次方
print(2**5)

# 用括号决定优先级
print((1 + 3) * 2)

# 布尔值 用not取非
print(True)
print(False)
print(not True)
print(not False)
print(True and False)
print(False or True)

# 整数也可以当作布尔值
print(0 and 2) # => 0
print(-5 or 0) # => -5
print(0 == False) # => True
print(10 == True) # => False
print(1 == True) # => True

# 用==判断相等 用!=判断不等
print(1==1)
print(1==2)
print(1!=1)
print(1!=2)

# 比较大小
print(1 < 10)  # => True
print(1 > 10)  # => False
print(2 <= 2)  # => True
print(2 >= 2)  # => True

print("***分隔符***")
# 大小比较可以连起来！
print(1 < 2 < 3)  # => True
print(2 < 3 < 2)  # => False