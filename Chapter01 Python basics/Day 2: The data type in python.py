# python里数据类型是强类型，动态类型。
# type(数据或变量) 可以查看数据类型。
# 变量：第一次赋值的时候声明，变量类型可变（动态）。

# type(None)  返回 'Nonetype'

# 内存：对象和变量表
# id(数据或变量):返回内存地址
# 对于整型数据，当值小于256时，不同的变量指向同一个int对象时，id（变量）返回的内存地址相同。
# 对于一些较短的字符串，也是这样。（放在了缓存中）
# ==比较的是值的大小，is比较的是内存地址。内存地址相同则认为是同一个对象。

# eg:

# a=10
# b=10
# id(a)
# 140711898821744
# id(b)
# 140711898821744
# a is b
# True

# e=256
# f=256
# e is f
# True


# z=2000
# y=2000
# id(z)
# 1537659823952
# id(y)
# 1537659823920
# id(z)==id(y)
# False
# y is z
# False
# y==z
# True

# 核心数据类型
# 1-数值类型：int  float  Decimal
# 2-字符串： str
# 3-序列：str list tuple
# 4-映射：dict
# 5-文件：
# 6-集合：set
# 7-布尔：bool
# 8-其他：None
# 9-程序单元：模块，函数，类

# list的元素是可以改变的，tuple的元素是不可以改变的。

# eg:
# 列表元素可变：
# li=[2,3,4,5]
# li
# [2, 3, 4, 5]
# li[0]=9
# li
# [9, 3, 4, 5]

# 元组元素不可变：
# tu=(2,3,4,5)
# tu
# (2, 3, 4, 5)
# tu[0]
# 2
# tu[0]=9
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

# 字典元素可变：
# d={'id':1,"name":"tom","score":"99"}
# d["name"]
# 'tom'
# d["name"]="Taylor"
# print(d["name"])

# in 在序列中使用：
# 7 in li
# False

# 3 in tu
# True

# "c" in "ascd"
# True

# in 在映射中使用：用来检查key或value的存在。
# "name" in d
# True
#
# "tom" in d.values()
# True


# -------------数值类型-------------
# int float Decimal

# 以二进制方式声明一个整型变量
# a=0b1001
# a
# 9

# 以八进制方式声明一个整型变量
# a=0o341437
# a
# 115487

# 以十六进制方式声明一个整型变量
# a=0x132AEF
# a
# 1256175

# Float 精度问题：
# 1.1-0.2
# # 0.9000000000000001

# Decimal
# import decimal
# decimal.Decimal("1.1")-decimal.Decimal("0.2")
# Decimal('0.9')
# 或者：
# from decimal import Decimal
# Decimal('1.1')-Decimal('0.9')
# Decimal('0.2')

# 注意，Decimal()接收的参数一定得是字符串型的，否则计算结果不准确,如果是数值型变量，
# 先用str()转一下。
# a=1.1
# b=0.2
# decimal.Decimal(a)-decimal.Decimal(b)
# Decimal('0.9000000000000000777156117238')

# decimal.Decimal(str(a))-decimal.Decimal(str(b))
# # Decimal('0.9')


# f=.14
# f
# 0.14

# 类型转换
# a="20"
# a*2
# '2020'

# a+"2"
# '202'
