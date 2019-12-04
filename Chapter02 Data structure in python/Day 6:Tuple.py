#                          元组
# 定义:不可变的列表称为元组.不可通过赋值改变元素值,
# 不支持以下会改变元组元素的操作:
# tuple.append(e),
# tuple.pop([index]),
# tuple.insert(index, element),
# del tuple[index]
# tuple.sort()
# tuple.reserve()
# 相比列表,元组是更简单的数据结构.

# 1--创建元组：
# (1)tuple = (1,2,3,...);
# (2)tuple = tuple(list).通过list创建元组
# (3)tuple = tuple(range([start,]stop[,step])).数字元组
# 2--访问元组:tuple[index]
dimensions=(200,50)
print(dimensions[0])  # 200
print(dimensions[1])  # 50

# 3--遍历元组
for d in dimensions:
    print(d)
        
# 4--修改列表变量(将元组引用指向新的元组对象):
dimensions=(200,50)
dimensions=(400,80)
print(dimensions)  # (400,80)

# 5--元组切片
tuple1 = (1,2,3,4,5,6,7)
tuple2 = tuple1[2:4]
print(tuple2)  # (3, 4)
tuple3 = tuple1[:]
print(tuple3)  # (1, 2, 3, 4, 5, 6, 7)

# 6--遍历元组切片
tuple4=(2,"heh",4,6,8,10,"hah")
for e in tuple4[:4]:
    print(e)
# 2
# heh
# 4
# 6


# 7--不支持永久排序tuple.sort() 因为元素不可改变.
tuple4 = (1,2,8,4,9,6,0)
# tuple4.sort()
# print(tuple4)  报错

# 8--支持临时排序函数sorted(tuple)
tuple5=sorted(tuple4)
print(tuple5)   # [0, 1, 2, 4, 6, 8, 9]

# 9--数字元组
tuple6 = tuple(range(1,10,2))
print(tuple6)  # (1, 3, 5, 7, 9)

# 10--元组解析 返回一个<genexpr>对象
tuple7=(x**2 for x in range(8))
print(tuple7)  #<generator object <genexpr> at 0x00000162A94124F8>

