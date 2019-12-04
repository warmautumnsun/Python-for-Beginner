#                               一  列表操作

# 1--创建列表:
# 1) 创建空列表:list1=[]
# 2) 创建非空列表 list2=[e0,e1,e2,e3...]
# 3) 创建特定长度的空列表 list3=[None]*10
# 4) 通过list4=list(range([start,]stop[,step]))函数创建 数字列表.
# 5) 通过列表解析生成 数字列表
# 6) 通过元组生成列表：list(tuple)
list0 = [None] * 5
for i in range(0, 5):
    list0[i] = "a" + str(i)
print(list0)  # ['a0', 'a1', 'a2', 'a3', 'a4']

tuple01=(1,3,5,7,9,2,4,6,8)
list02=list(tuple01)
print(list02)  # [1, 3, 5, 7, 9, 2, 4, 6, 8]




# 2--修改,添加和删除列表元素:
# 修改索引为index处的列表元素:list[index]=new_element 即可.
# 添加列表元素:
# 1)--末尾追加元素: list.append(new_element)
# 2)--列表中插入元素: list.insert(index, element),
# 如果index超出原列表长度,则只在列表末尾追加.
list01 = [0, 1, 2, 3, 4, 5]
list01.insert(2, "new")
print(list01)  # [0, 1, 'new', 2, 3, 4, 5]
list01.insert(8, "new2")
print(list01)  # [0, 1, 'new', 2, 3, 4, 5, 'new2']
list01.insert(15, "new3")
print(list01)  # [0, 1, 'new', 2, 3, 4, 5, 'new2', 'new3']

# 3)--从列表中删除元素:
# (1) del list[index]  del语句   语句操作不会有返回值.
# (2) del list[start:stop] 切片式删除. 不包含stop处元素，含左不含右。
# (3) list.pop([index]) 删除index处的元素,并返回此元素,index缺省时,删除并返回末尾元素.
# (4) 根据值删除元素 list.remove(e) 没有返回值.
list01 = ['a', 'b', 'c', 'd', 'e', 'f']
del list01[2]
print(list01)  # ['a', 'b', 'd', 'e', 'f'] 列表中不再存在'c'
list01 = ['a', 'b', 'c', 'd', 'e', 'f']
del list01[1:4]
print(list01)  # ['a', 'e', 'f']

list02 = [0, 1, 2, 3, 4, 5]
print(list02.pop())  # 5  返回5
print(list02)  # [0, 1, 2, 3, 4]   列表中不再存在5

list03 = ['a', 'b', 'c', 'd', 'e', 'f']
list03.remove("b")
print(list03)  # ['a', 'c', 'd', 'e', 'f']

#                                    二  组织列表

# 1--永久排序:
# list.sort([reserve=True/False])方法,无返回值，原列表就地排序：根据asc码排序.(小->大)
# (1)当列表元素中既有数字又有字符串时，排序会报错，字符串型数字可以与字符串比较，所有字符
#    串型的数字的asc码均小于字符串！
# (2)先按元素的第一个字符进行排序，第一个字符相同时，比较第二个，以此类推。

# list04=[3,1,"cb","a","ca"]
# list04.sort()
# print(list04) #TypeError: '<' not supported between instances of 'str' and 'int'
list04 = ["3", "1", "cb", "a", "ca"]
list04.sort()
print(list04)  # ['1', '3', 'a', 'ca', 'cb']

# 2--临时排序：
# (1)函数sorted(list，[reserve=True/False])函数，返回一个排序之后的新列表，原列表不变。
# (2)当reserve=True时，排序后顺序反转。
list05=["3", "1", "cb", "a", "ca"]
list06=sorted(list05)
print(list05)   # ['3', '1', 'cb', 'a', 'ca']
print(list06)   # ['1', '3', 'a', 'ca', 'cb']

# 3--列表元素反转: list.reserve()  无返回值。不排序，原列表反转元素顺序。
list07=["3", "1", "cb", "a", "ca"]
list07.reverse()
print(list07)  # ['ca', 'a', 'cb', '1', '3']

# 4--获取列表长度: 函数len(list)
print(len(list07))  # 5

# 5--遍历整个列表:
# 使用for in 循环遍历列表:
# for e in list:
#   print(e)

# 或者
# for i in range(len(list)-1):
#   print(list[i])

list08=["3", "1", "cb", "a", "ca"]
for i in range(len(list08)):
    print("第" + str(i)+ "个元素是:" + list08[i] + "\n")
    # 注意range(n) 表示的范围是[0,n),长度为n. "\n"为换行符.


#                                三  数字列表

# 6--Range()函数:
# 函数range([start,]stop[,step]),返回值是数字序列,不是列表.
# 含左不含右.当start缺省时,默认为0,当step缺省时,默认为1.

# 7--创建数字列表:
# 1)--使用range()创建数字列表:list(range([start,]stop[,step]))
list09 = list(range(1,10,2))
list10 = list(range(8))
print(list09)  # [1, 3, 5, 7, 9]
print(list10)  # [0, 1, 2, 3, 4, 5, 6, 7]

squares = []
for i in range(8):
    squares.append(i**2)

print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49]

# 8--数字列表的统计计算: min(list), max(list),sum(list)
list11=[1,3,5,7,9,11,-1]
print(min(list11))  # -1
print(max(list11))  # 11
print(sum(list11))  # 35

# 9--列表解析: 一种由range()快速生成数字列表的方法:
# list=[expressof_x for x in range([start,]stop[,step])]
list12=[x**2 for x in range(8)]
print(list12)  # [0, 1, 4, 9, 16, 25, 36, 49]


#                               四  列表切片
# 创建切片方式汇总:
# 1) list_new = list_old[start,stop] 含左不含右. start,stop可以是负值.
# 2) list_new = list_old[start:]     从start到最后. start可以是负值.
# 3) list_new = list_old[:stop]      含左不含右.
# 4) list_new = list_old[:]          复制完整列表.


# 1--创建切片:
# 1) list_new = list_old[start:stop]
# 含左不含右. start,stop可以是负值. 但start必须在stop左边才有意义,否则为空.
# 切片的返回结果类型和切片对象类型一致.

# 2) list_new = list_old[start:]
# 从start到最后. start可以是负值.

# 3) list_new = list_old[:stop]  含左不含右.
# 4) list_new = list_old[:]
# 复制完整列表.这种复制是安全的,对新列表的操作不影响原列表,反之亦然.

list12=[0,1,2,3,4,5,6,7,8,9]

list13=list12[2:5]
print(list13)    # [2, 3, 4] 含左不含右

list14=list12[-5:-2]
print(list14)    # [5, 6, 7] 含左不含右
list15=list12[-2:-5]
print(list15)    # 无意义 []

list16=list12[3:]
print(list16)  # [3, 4, 5, 6, 7, 8, 9]
list17=list12[-3:]
print(list17)  # [7, 8, 9]

# 2--遍历列表:
list20=[2,"heh",4,6,8,10,"hah"]
for e in list20[:4]:
    print(e)
# 2
# heh
# 4
# 6

