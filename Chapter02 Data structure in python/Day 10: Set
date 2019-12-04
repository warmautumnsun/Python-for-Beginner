# 集合

# 1-建立集合：1）-- {}，  2）-- set()函数
# 2-操作集合
# 3-使用集合的方法
# 4-使用集合的函数操作
# 5-冻结集合frozenset

# 1）--集合及元素的特点：
# 集合的内的元素无序且唯一，元素本身具有不可变性。
# 集合的内的元素类型可以多样。
# 集合本身可变：可增加和删除元素

# 可以作为集合元素的有：整形，浮点型，字符串，元组 （它们都是不可变的）
# 不可作为集合元素的有：列表，字典，集合 （它们都是可变的）

# 回顾：
# 列表：元素有序（有索引）不唯一，元素可变可不变，元素类型多样，列表本身可变。
# 元组：元素有序（有索引）不唯一，元素可变可不变，元素类型多样，元组本身不可变。
# 字典：元素无序，key值唯一，key为任意不可变类型，需要注意的是tuple元组作为键时，
#      其中不能以任何方式包含可变对象。value为任意类型。字典本身可变。

# 可以作为set()函数的参数的类型有：序列类型！
# 如，字符串，列表（不含可变元素），元组（不含可变元素）。
# 这与参数是可变不可变没有关系，因为集合的元素不是这些参数，而是组成这些参数的元素。

# 一，建立集合：
# 1--使用{}来建立集合：
# 举例：
languages = {"vba", "python", "java", "c", "c"}
print(languages)  # {'python', 'java', 'vba', 'c'}  无序且唯一，多余的“c”元素去掉了。
print(type(languages))  # <class 'set'>

# mixed_set = {1, "s", [1, 2, 3]}
# print(mixed_set)  # TypeError: unhashable type: 'list'
# unhashable 意味着是可变的，list 是 unhashable.

empty_dict = {}  # 这样定义的是空字典，而不是空集合。
print(type(empty_dict))  # <class 'dict'>

# 2--使用set()函数定义集合：

# 1)--空集合的建立方法：   set()表示空集合
empty_set = set()
print(type(empty_set))  # <class 'set'>

# 2)--将组成字符串，列表，元组的元素转为集合元素。
str = "aabcdeedfghikf"
str_set = set(str)
print(str_set)  # {'g', 'b', 'k', 'f', 'h', 'i', 'd', 'a', 'c', 'e'} 无序，唯一

list1 = [1, 2, 1, "s", "t", "r", "s"]
list_set = set(list1)
print(list_set)  # {1, 2, 't', 's', 'r'} 无序，唯一

tuple1 = (1, 2, 1, "s", "t", "r", "s")
tuple_set = set(tuple1)
print(tuple_set)  # {1, 2, 't', 's', 'r'} 无序，唯一

# 当list或tuple含有可变元素(列表，字典，集合)时：报错！
# list2 = [1, 2, ["s", 4, 2]]
# list2_set = set(list2)
# print(list2_set)  # TypeError: unhashable type: 'list'

# list3 = [1, 2, {"name":"tom","age": 29}]
# list3_set = set(list3)
# print(list3_set)  # TypeError: unhashable type: 'dict'

# list4 = [1, 2, {"collin","tom","jiera","taylor"}]
# list4_set = set(list4)
# print(list4_set)  # TypeError: unhashable type: 'set'


# 二，集合的操作

# 交集&，并集|，差集-，对称差集^
# 等于==, 不等于!=
# in, not in

# 1--交集（找两个集合的共同元素）:
# 语法： AB=A&B 或 AB=A.intersection(B) 或 AB=B.intersection(A)
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
AB = A & B
print(AB)  # {3, 4, 5}
AB = A.intersection(B)
print(AB)  # {3, 4, 5}
AB = B.intersection(A)
print(AB)  # {3, 4, 5}

# 2--并集（将两个集合的元素合并为新的集合）重复元素保留一个：
# 语法：A|B 或 A.union(B) 或 B.union(A)
A = {"A", "B", "C", "D"}
B = {"C", "D", "E", "F"}
print(len(A), "--", len(B))  # 4 -- 4
AorB = A | B
print(AorB)
AorB = B | A
print(AorB)
AorB = A.union(B)
print(AorB)
AorB = B.union(A)
print(AorB, len(AorB))
# {'E', 'B', 'D', 'F', 'C', 'A'} 6

# 3--差集：
# 语法：属于A但不属于B: A-B; 属于B但不属于A：B-A
A = {"A", "B", "C", "D"}
B = {"C", "D", "E", "F"}
A_only = A - B
print(A_only)  # {'A', 'B'}
A_only = A.difference(B)
print(A_only)  # {'A', 'B'}

B_only = B - A
print(B_only)  # {'E', 'F'}
B_only = B.difference(A)
print(B_only)  # {'E', 'F'}

# 4--对称差集：A|B-AB A，B两个集合排除共有的剩下的其他所有部分
# 语法：A^B  A.symmetric_difference(B)
A = {"A", "B", "C", "D"}
B = {"C", "D", "E", "F"}

A_syid_B = A ^ B
print(A_syid_B)  # {'B', 'F', 'A', 'E'}

A_syid_B = B.symmetric_difference(A)
print(A_syid_B)  # {'B', 'F', 'A', 'E'}  无序，每次打印都可能不一样。

# 5--等于：bo = A == B 返回True或False
A1 = {"A", "B", "C", "D"}
B = {"C", "D", "E", "F"}
A2 = {"B", "A", "D", "C"}

print(A1 == B)  # False
print(A1 == A2)  # True

# 6--不等于 !=
# 语法：A != B  如果A不等于B，返回True，否则False
A = {"A", "B", "C", "D"}
B = {"C", "D", "E", "F"}
print(A != B)  # True

# 7--成员操作符 in  not in
A = {"A", "B", "C", "D"}
print("A" in A)  # True
print("M" in A)  # False

# 三，集合的类方法
# A.add(e)                   给集合增加一个元素。
# A.clear()                  空集合的所有元素。
# B=A.copy()                 以浅复制（shallow copy）方式复制集合。
#                            对新集合的操作不会影响到旧集合
# B=A                        深复制 deep copy
# A.difference_update(B)     删除与另一个集合重复的元素，更新A使其不含有与B重复的元素。
# A.discard(e)               删除元素，无论此元素存不存在都不报错.返回None
# A.pop(e)                   返回所随机删除的元素，如果是空集合则返回False
# A.remove(e)                删除指定元素，此元素不存在则返回KeyError 'e'
# A.intersection_update(*B)  更新A使其等于AB （*B表示参数可以是多个集合，以逗号分开)。
# A.isdisjoint(B)            如果A与B没有交集，相互独立，则返回True。
# A.issubset(B)              如果A集合是B集合的子集，则返回True.
# A.issuperset(B)            如果A集合是B集合的父集，则返回True.
# A.update(B)                使用A|B来更新集合内容

# 方法举例：
A = {"A", "B", "C", "D"}

# 新增元素
A.add("E")
print(A)  # {'D', 'A', 'B', 'C', 'E'}

# 清空元素
A.clear()
print(A)  # set() 空集合

# 移除集合中的元素
# 方法1：A.discard(e)
A = {"A", "B", "C", "D"}
A.discard("D")
print(A)  # {'C', 'B', 'A'}
A.discard("F")
print(A)  # {'B', 'C', 'A'}
# 方法2：A.pop() 随机删除某元素，并返回此元素
SETB = {"A", "B", "C", "D"}
e = SETB.pop()
print(e)  # D
print(SETB)  # {'A', 'C', 'B'}
SETC = set()
# e=SETC.pop()  # KeyError: 'pop from an empty set'
# print(e)  #
# print(SETC)  #
# 方法3：A.remove(e)
A = {"A", "B", "C", "D"}
A.remove("D")
print(A)  # {'B', 'A', 'C'}
# A.remove("F")
# print(A)  # KeyError: 'F'

# 集合复制
# 1--集合浅复制  对新集合操作不影响原集合
A = {"A", "B", "C", "D"}
B = A.copy()
B.add("E")
print(B)  # {'B', 'E', 'C', 'D', 'A'}
print(A)  # {'A', 'C', 'B', 'D'}
# 2--深复制     对新集合操作影响原集合
B = A
B.add("F")
print(B)  # {'A', 'C', 'B', 'F', 'D'}
print(A)  # {'A', 'C', 'B', 'F', 'D'}

# 判断是否相互独立没有交集：是True,否False
A = {"A", "B", "C", "D"}
B = {"C", "F", "M"}
print(A.isdisjoint(B))  # False

# 判断是否为子集或父集
A = {"A", "B", "C", "D"}
B = {"B", "C"}
print(B.issubset(A))  # True
print(A.issuperset(B))  # True

# 用交集更新集合：
A = {"A", "B", "C", "D"}
B = {"B", "C", "E", "F"}
A.intersection_update(B)  # 返回值为None
print(A)  # {'B', 'C'}

A = {"A", "B", "C", "D"}
B = {"B", "C", "E", "F"}
C = {"A", "C", "E"}
A.intersection_update(B, C)  # 返回值为None
print(A)  # {"C"}

# 将集合B的元素全部添加到集合A里： 等效于A=A|B
A = {"A", "B", "C", "D"}
B = {"B", "C", "E", "F"}
A.update(B)
print(A)  # {'B', 'D', 'E', 'A', 'F', 'C'}
print(A | B)  # {'C', 'B', 'E', 'D', 'A', 'F'}

# 删除与另一集合重复的元素
# A.difference_update(B) 等效于： A=A-B  A=A.difference(B)
A = {"A", "B", "C", "D"}
B = {"B", "C", "E", "F"}
A.difference_update(B)
print(A)  # {'A', 'D'}

A = {"A", "B", "C", "D"}
B = {"B", "C", "E", "F"}
A = A - B
print(A)  # {'A', 'D'}

# 使用对称差集来更新调用此方法的集合
# A.symmetric_difference_update(B) 等效于A = A.symmetric_difference(B)
A = {"A", "B", "C", "D"}
B = {"B", "C", "E", "F"}
A.symmetric_difference_update(B)  # 返回值None
print(A)  # {'F', 'E', 'A', 'D'}

A = {"A", "B", "C", "D"}
B = {"B", "C", "E", "F"}
A = A.symmetric_difference(B)
print(A)  # {'F', 'E', 'A', 'D'}

# 四，操作集合的函数：
# enumerate(A)                      # 传回连续整数配对的enumerate对象
# len(A)                            # 返回元素数量
# max(A)                            # 返回最大值
# min(A)                            # 返回最小值
# sum(A)                            # 求和
# sorted()                          # 返回已经排序的列表，集合本身不变

# 函数举例：
# max(A),min(A),sum(A):
# 1) 若集合的元素是数值，则分别是求最大值，最小值，和
# 2）若集合元素是字符串或字符，则是对元素的unicode找最大最小值，sum()不可用于字符或字符串。
# 举例：略

# len(A) 返回集合元素数量
# 举例：略

# sorted(A[,reverse=False]) 临时排序，不改变原集合，返回列表！！
# 当reverse=True时，逆向排序。
# 既含有数值，又含有字符或字符串的集合不能使用此方法。

A = {"b", "B", "A", "D", "f"}
list01 = sorted(A)
list02 = sorted(A, reverse=True)
print(list01)  # ['A', 'B', 'D', 'b', 'f']
print(list02)  # ['f', 'b', 'D', 'B', 'A']
A = {3, 5, 1, 2, 6, 9, 0}
list03 = sorted(A)
print(list03)  # [0, 1, 2, 3, 5, 6, 9]

# enumerate()对象
# enumerate() 方法可以将iterable类数值的元素用计数值与元素配对的方式传回，返回的数据
# 称之为enumerate对象。其中iterable类数值可以是列表（list）,元组（tuple）,集合（set）
# 语法：obj=enumerate(iterable[,start=0])  # 如果省掉start=设定，默认值为0
# 我们可以使用list()将enumerate对象转化为列表，使用tuple()将enumerate对象转成元组。

# enumerate对象被转为list或tuple之后,就变为空了。

# 1）当iterable类数值为list时：

# ---------------------将列表对象转为enumerate对象---------------------：
drinks01 = ["tea", "coffee", "wine"]
enumerate_drinks01 = enumerate(drinks01)  # 数值初始为0
print(enumerate_drinks01)  # <enumerate object at 0x0000015B937D50D8>
print(type(enumerate_drinks01))  # <class 'enumerate'>

# ---------------------将enumerate对象转为列表------------------------：
drinks01 = ["tea", "coffee", "wine"]
enumerate_drinks01 = enumerate(drinks01)  # 数值初始为0
print(enumerate_drinks01)  # <enumerate object at 0x000001BCB1E15120>
print(list(enumerate_drinks01))
# [(0, 'tea'), (1, 'coffee'), (2, 'wine')]
print(enumerate_drinks01)  # <enumerate object at 0x000001BCB1E15120>

enumerate_drinks01 = enumerate(drinks01, start=10)  # 数值初始为10
print(list(enumerate_drinks01))
# [(10, 'tea'), (11, 'coffee'), (12, 'wine')]


# ---------------------将enumerate对象转为元组------------------------：
enumerate_drinks01 = enumerate(drinks01)  # 数值初始为0
print(tuple(enumerate_drinks01))
# ((0, 'tea'), (1, 'coffee'), (2, 'wine'))

enumerate_drinks01 = enumerate(drinks01, start=10)  # 数值初始为10
print(tuple(enumerate_drinks01))
# ((10, 'tea'), (11, 'coffee'), (12, 'wine'))


# 2）当iterable类数值为tuple时：

# -----------将元组对象转为enumerate对象----------：
drinks02 = ("tea", "coffee", "wine")
enumerate_drinks02 = enumerate(drinks02)  # 数值初始为0
print(enumerate_drinks02)  # <enumerate object at 0x0000015B937D50D8>
print(type(enumerate_drinks01))  # <class 'enumerate'>

# -----------将enumerate对象转为列表或元组---------：
drinks02 = ("tea", "coffee", "wine")

enumerate_drinks02 = enumerate(drinks02)  # 数值初始为0
# 将enumerate对象转为列表：
print(list(enumerate_drinks02))
# [(0, 'tea'), (1, 'coffee'), (2, 'wine')]

# 将enumerate对象转为元组：
enumerate_drinks02 = enumerate(drinks02)  # 数值初始为0
print(tuple(enumerate_drinks02))
# ((0, 'tea'), (1, 'coffee'), (2, 'wine'))

enumerate_drinks02 = enumerate(drinks01, start=10)  # 数值初始为10
# 将enumerate对象转为列表：
print(list(enumerate_drinks02))
# [(10, 'tea'), (11, 'coffee'), (12, 'wine')]
enumerate_drinks02 = enumerate(drinks01, start=10)  # 数值初始为10
# 将enumerate对象转为元组：
enumerate_drinks01 = enumerate(drinks02)
print(tuple(enumerate_drinks02))

print("---------------------------")
# 3）使用for in 循环解析enumerate对象：
drinks = ["tea", "coffee", "wine"]

enumerate_drinks = enumerate(drinks)  # 数值初始为0
for drink in enumerate_drinks:
    print(drink)

# (0, 'tea')
# (1, 'coffee')
# (2, 'wine')

enumerate_drinks = enumerate(drinks)  # 数值初始为0
for count, drink in enumerate_drinks:  #
    print(count, drink)

# 0 tea
# 1 coffee
# 2 wine
print("---------------------------")

# 3）当iterable类数值为set时：
drinks03 = {"tea", "coffee", "wine"}
enumerate_drinks03 = enumerate(drinks03)  # 数值初始为0
print(enumerate_drinks03)  # <enumerate object at 0x0000023C7E455438>
print(type(enumerate_drinks03))  # <class 'enumerate'>

# 将enumerate转为列表：
print(list(enumerate_drinks03))
# [(0, 'coffee'), (1, 'tea'), (2, 'wine')]

# 将enumerate转为元组：
enumerate_drinks03 = enumerate(drinks03, 20)  # 数值初始为20
print(tuple(enumerate_drinks03))
# ((20, 'wine'), (21, 'coffee'), (22, 'tea'))

# 遍历enumerate：
enumerate_drinks03 = enumerate(drinks03)  # 数值初始为0
for drink in enumerate_drinks03:
    print(drink)

# (0, 'wine')
# (1, 'tea')
# (2, 'coffee')

for count, drink in enumerate_drinks03:
    print(count, drink)

# (0, 'coffee')
# (1, 'wine')
# (2, 'tea')


# 五，冻结集合：
# 元组可看作不可变列表，冻结集合frozenset可看作是不可变集合。
# frozenset的好处：1）可作为集合的元素；2）可作为字典的key
# 使用frozenset()函数建立frozenset.
# 不可使用add(),remove(),pop()，update()等改变集合内容的方法，但可以使用：
# A&B A|B A-B A^B A.copy() issubset() issuperset() isdisjoint()等方法。


frozensetA = frozenset(["A", "B", "C", "D"])
frozensetB = frozenset(["E", "F", "C", "D"])
print(frozensetA)  # frozenset({'A', 'B', 'D', 'C'})
print(frozensetB)  # frozenset({'C', 'F', 'D', 'E'})
print(frozensetA & frozensetB)  # frozenset({'D', 'C'})
print(frozensetA | frozensetB)  # frozenset({'D', 'C', 'F', 'B', 'E', 'A'})

# 六，补充知识：tuple元组的zip()方法：
# 这是一个内置函数，参数内容主要是可迭代（iterable）的对象，如列表,元组等。
# 然后将相对应的元素打包成元组（tuple），最后传给zip对象object, 我们可以使用list()函数
# 将zip对象转成列表，或使用tuple()函数将zip对象转为元组。

fields = ['name', 'age', 'hometown']
info = ['tom', '25', 'xuzhou']
zipdata = zip(fields, info)
print(zipdata)  # <zip object at 0x000002297CD18848> 是object

# 把zip对象转为list：
print(list(zipdata))
# [('name', 'tom'), ('age', '25'), ('hometown', 'xuzhou')]

# 把zip对象转为tuple：
zipdata = zip(fields, info)
print(tuple(zipdata))
# (('name', 'tom'), ('age', '25'), ('hometown', 'xuzhou'))

# 如果zip()函数的列表参数的长度不相等，由于多出的元素无法匹配，转成列表对象之后zip对象元素
# 数量将是较短的数量。
fields = ['name', 'age', 'hometown','job']
info = ['tom', '25', 'xuzhou']
zipdata = zip(fields, info)
print(zipdata)  # <zip object at 0x000002297CD18848>

# 把zip对象转为list：
print(list(zipdata))
# [('name', 'tom'), ('age', '25'), ('hometown', 'xuzhou')]


# 如果将上述通过zip()函数得到的新的list放在zip()函数内，并在此列表前增加"*"符号，
# 表示unzip()此列表，得到最初的那连个列表：
fields = ['name', 'age', 'hometown']
info = ['tom', '25', 'xuzhou']
zipdata = zip(fields, info)
new_list=list(zipdata)
f,i=zip(*new_list)
print(f)  # ('name', 'age', 'hometown')
print(i)  # ('tom', '25', 'xuzhou')

fields = ['name', 'age', 'hometown','job']
info = ['tom', '25', 'xuzhou']
zipdata = zip(fields, info)
new_list=list(zipdata)
f,i=zip(*new_list)
print(f)  # ('name', 'age', 'hometown')  注 没有 'job'这个元素了。
print(i)  # ('tom', '25', 'xuzhou')
