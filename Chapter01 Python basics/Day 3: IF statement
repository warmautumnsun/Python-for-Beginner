#                      条件测试及If 语句

# 1--常见的条件测试:
#   1)相等==
#   2)格式为大小写之后判断是否相等
#   3)检查是否不相等 !=
#   4)数字比较 < > == != >= <=
#   5)检查多个条件: and or    and优先级比or高.
#   6)检查特定值是不是存在于列表中.   in  not in

i=1.5
if 1<3 and i>-2 or i==1:
    print("符合条件"+str(i))  # 符合条件1.5

i=1
if 1<3 and i>-2 or i==1:
    print("符合条件"+str(i))  # 符合条件1

list01=["3", "1", "cb", "a", "ca"]
if 'cb' in list01:
    print('here')  # here

if 'cf' not in list01:
    print('not here')  # not here

# 2--If 语句:
#   1)if condition:
#         do something
#   2)if condition:
#         do something
#     else:
#         do something
#   3)if condition01:
#         do something
#     elif condition02:
#         do something
#       ....
#     [else:
#          do something]

# 用If语句处理列表：
# 可以高效地管理不断变化的情形。

# 检查元素是否在列表中（如果不存在就把它加进去）：
list01=["3", "1", "cb", "a", "ca"]
if 'ce' in list01:
    print('here')
else:
    print('not here')
    list01.append("ce")
print(list01)

# not here
# ['3', '1', 'cb', 'a', 'ca', 'ce']
