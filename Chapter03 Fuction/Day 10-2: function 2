作补充：

# 参数类型：位置参数，关键字参数，默认值参数。
# 默认值参数放最后，不影响位置参数的使用。

# 使用默认值的场合：
# 1）一些参数是必须的，不指定时使用默认值。
# 2）一些参数在某些情况下是不必须的，将定义函数时将默认值设为空，只有当使用到这个参数时
# 才给这个参数赋值，比如middle name，不是所有人都有middle name。

# 函数返回值：
# 1--返回None：不设计返回值时实际上默认 return None。
# 2--简单返回数值数据。
# 3--返回多个数据的应用：返回数据之间用逗号分隔。
# 4--返回字典或列表：

def addToVipDict(id, name):
    if id not in dict_vip:
        dict_vip[id] = name


dict_vip = {}
addToVipDict(1,"rex")
addToVipDict(2,"tom")
addToVipDict(3,"taylor")

print(dict_vip)  # {1: 'rex', 2: 'tom', 3: 'taylor'}
