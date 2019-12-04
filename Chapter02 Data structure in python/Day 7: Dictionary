#                           Dictionary 字典
# 1--创建字典：
# (1)dic={key1:value1,key2:value2...}
# (2)函数dict创建字典。
# 没有空字典，最简单的字典只有一个键值对（项Iterm）。无序，没有索引。
# 字典即可以用来存储同一个对象的多种信息（如一个学生的姓名，年龄，体重等）。
# 也可以用来存储多种相似对象（如key为name，value为score）。
# 键不可重复，值可以重复。
# 字典是python中唯一的内置映射类型，其中的值不按顺序排列，而是储存在键下。
# 键可以是数字，字符串或元组！

# 2--修改字典值：
# dic[key]=new_value

# 3--删除键值对：del dic[key]
favorite_languages = {"tom": "java", "ivan": "java", "alex": "vba",
                      "taylor": "python"}
print(favorite_languages)
del favorite_languages["alex"]
print(favorite_languages)
# {'tom': 'java', 'ivan': 'java', 'alex': 'vba', 'taylor': 'python'}
# {'tom': 'java', 'ivan': 'java', 'taylor': 'python'}
print("tom's favorite language is " +
      favorite_languages["tom"].title() + ".")
# tom's favorite language is Java.

# 4--遍历字典：
# (1)遍历键-值对 for k,v in dic.items():
# (2)遍历键 for k in dic.keys():      其中.keys() 可省略，dic.keys()是视图
# (3)按顺序遍历所有的键。
# (4)遍历值：
#   1）for v in dic.values():    dic.values()是视图
#   2）通过遍历键来遍历值：
#       for k in dic.keys():
#           print(k + "对应的值为：" + dic[k])

# 遍历键-值对:
favorite_languages = {"tom": "java", "ivan": "java", "alex": "vba",
                      "taylor": "python"}
for k, v in favorite_languages.items():
    print("\nkey:" + k)
    print("value:" + v)
# key:tom
# value:java
#
# key:ivan
# value:java
#
# key:alex
# value:vba
#
# key:taylor
# value:python

# 遍历键:
for k in favorite_languages.keys():
    print("\nkey:" + k)
# key:tom
#
# key:ivan
#
# key:alex
#
# key:taylor

# 遍历值--通过键得到值：
for k in favorite_languages.keys():
    print("\nvalue:" + favorite_languages[k])
# value:java
#
# value:java
#
# value:vba
#
# value:python

# # 遍历值：
for v in favorite_languages.values():
    print("\nvalue:" + v)
# value:java
#
# value:java
#
# value:vba
#
# value:python

# 按顺序遍历所有的键：对键进行临时排序：
for k in sorted(favorite_languages.keys()):
    print("sorted_key:" + k.title())
# sorted_key:Alex
# sorted_key:Ivan
# sorted_key:Taylor
# sorted_key:Tom

# 按顺序遍历所有的值：对值进行临时排序：
for v in sorted(favorite_languages.values()):
    print("sorted_value:" + v.title())
# sorted_value:Java
# sorted_value:Java
# sorted_value:Python
# sorted_value:Vba

print(type(favorite_languages.values()))  # <class 'dict_values'>

# 5--函数dict:可以从其他字典或键值对序列创建字典：
# (1)items=[(key0,value0),(key1,value1),(key2,value2)...]
#    dic=dict(item)
# (2)


# 6--数据结构的嵌套：

# (1)字典列表(列表元素为字典)：[dic1,dic2,dic3...]

# 创建10个特征一样的外星人
aliens = []
for alien_no in range(10):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# 打印前3个外星人：
for alien in aliens[:3]:
    print(alien)
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}

# 修改某些外星人特征：
for alien in aliens[:3]:
    alien["color"] = "yellow"
    alien["speed"] = "medium"
    print(alien)
# {'color': 'yellow', 'points': 5, 'speed': 'medium'}
# {'color': 'yellow', 'points': 5, 'speed': 'medium'}
# {'color': 'yellow', 'points': 5, 'speed': 'medium'}

for alien in aliens[:2]:
    alien["points"] = 6
    print(alien)
# {'color': 'yellow', 'points': 6, 'speed': 'medium'}
# {'color': 'yellow', 'points': 6, 'speed': 'medium'}

for alien in aliens[:5]:
    if alien["points"] == 6:
        alien["speed"] = "fast"
    print(alien)
# {'color': 'yellow', 'points': 6, 'speed': 'fast'}
# {'color': 'yellow', 'points': 6, 'speed': 'fast'}
# {'color': 'yellow', 'points': 5, 'speed': 'medium'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}

# (2)字典中存储列表(字典的值为列表)：
favorite_languages = {"tom": ["java", "vba"], "ivan": ["vba", "java", "python"],
                      "taylor"
                      : "python"}
print(favorite_languages["ivan"])  # ['vba', 'java', 'python']

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# Tom's favorite languages are:
# 	Java
# 	Vba
#
# Ivan's favorite languages are:
# 	Vba
# 	Java
# 	Python
#
# Taylor's favorite languages are:
# 	P
# 	Y
# 	T
# 	H
# 	O
# 	N

# 可见,字符串也可被for in遍历.
# 注意：列表和字典的嵌套层级不应太多.

# (3)字典嵌套字典：
# 直接举例:
users = {"aeinstein": {"firstname": "albert", "lastname": "einstein",
                       "location": "beijing"},
         "mcuries": {"firstname": "marie", "lastname": "curie",
                     "location": "paris"}}

for username,user_info in users.items():
    print("\nUsername:"+username)
    fullname=user_info["firstname"]+" "+user_info["lastname"]
    location = user_info["location"]

    print("Fullname:"+fullname.title())
    print("Location:" + location.title())

# Username:aeinstein
# Fullname:Albert Einstein
# Location:Beijing
#
# Username:mcuries
# Fullname:Marie Curie
# Location:Paris
