#                                  函数
# 函数是带名字的代码块,用来完成具体的工作.
# 函数可以没有返回值,也可以返回任何类型的值，包括列表,字典等较复杂的数据结构。
# 也可以有多个返回值。

# 本章内容：
# 1)编写函数，以及如何传递实参，让函数能够访问完成其工作所需的信息；
# 2)使用位置实参和关键字实参，以及任意数量的实参；
# 3)显示输出的函数和返回值的函数；
# 4)如何将函数同列表、字典、if语句和while循环结合起来使用。
# 5)如何将函数存储在被称为模块的独立文件中，让程序文件更简单、更易于理解。
# 6)学习函数编写指南。

# 1--函数示例:
def hello():
    print("Hello")


hello()


# 2--带参数的函数:
def hello(name):
    print("Hello " + name.title())


hello("tom")


# 3--实参和形参: 定义就不解释了
# 3-1)传递实参:
#   1)位置实参，实参的顺序与形参的顺序相同；
#   2)关键字实参，每个实参都由变量名和值组成；
#   3)形参使用默认值,默认值的形参必须放在最后面,这样在调用时不妨碍其他实参使用位置参数.
#   3)列表和字典。

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 3-1-1)位置实参
describe_pet('Cat', 'Tom')

# 3-1-2)关键字实参
describe_pet(animal_type='Cat', pet_name='Tom')


# 3-1-3)形参默认值
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')  # 关键字参数指定剩下的参数值,
describe_pet('willie')  # 位置参数,这个实参将关联到函数定义中的第一个形参.


# I have a dog.
# My dog's name is Willie.

# 3-1-4)混合使用实参,关键字参数和形参默认值:

# def describe_pet(pet_name, animal_type='dog'):
# # 一条名为Willie的小狗
# describe_pet('willie')
# describe_pet(pet_name='willie')
# # 一只名为Harry的仓鼠
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# 4--函数的返回值:
# 1)函数可以没有返回值.
# 2)可使用return语句将值返回到调用函数的代码行。

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 5--让实参可选: 使用默认值来让实参变成可选的。
# 有时候,可以让某些参数在必要时才提供给函数,其他时候使用默认值。

# 比如:并不是所有的人的名字都有middle name,可以默认middle name为空,需要时再赋值.
def get_formatted_name(first_name, last_name, middle_name=''):
    # 根据middle_name是否为默认值,给定不同的返回值.
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Jimi Hendrix
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)  # John Lee Hooker


# 6--函数返回字典。
# 函数可返回任何类型的值， 包括列表和字典等较复杂的数据结构。
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


# {'first': 'jimi', 'last': 'hendrix'}


# 7--结合使用函数和while 循环:
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'quit' at any time to quit)")
    f_name = input("First name: ")

    if f_name == 'quit':
        break

    l_name = input("Last name: ")
    if l_name == 'quit':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


# 8--传递列表:
# 你经常会发现，向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象
# （如字典）。将列表传递给函数后，函数就能直接访问其内容。
# 8-0 简单示例.
# 8-1 对传入的列表进行操作,会影响此列表.
# 8-2 对传入的列表切片进行操作,不会影响此列表.
#

# 8-0 将列表传入函数:
# eg:
# 下面的示例将一个名字列表传递给一个名为greet_users()的函数，这个函数问候列表中的每个人：

def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 8-1 在函数中修改列表:即,给函数传入列表,在函数体内对该列表进行列表的各种操作.
# eg:
# 1)不使用函数时:
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:  # 当第一个列表不为空时,进入循环.
    current_design = unprinted_designs.pop()

    print("Printing model: " + current_design)
    completed_models.append(current_design)

# 显示打印好的所有模型:
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# 2):使用函数时:
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8-2 在函数中修改列表切片:即,给函数传入列表切片,在函数体内对该切片进行列表的各种操作.
# eg:

list_name = ["tom", "ivan", "taylor"]
greet_users(list_name[:])  # 传入的是列表的切片

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)  # 传入的是列表的切片


# 练习:列表反转函数,不改变原列表:
def reverse(ListInput):
    RevList = []
    for i in range(len(ListInput)):  # i 从0开始
        RevList.append(ListInput[-i - 1])
    return RevList


def reverse02(ListInput):
    Rlist = ListInput[:]
    Rlist.reverse()
    return Rlist


list01 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse(list01))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(list01)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list02 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse02(list02))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(list02)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 9--传入任何数量的实参: 形参:*vars.

# 9-1)收集任意数量的实参:

# 有时候，预先不知道函数需要接受多少个实参，Python允许函数从调用语句中收集任意数量的实参。
# 形参名*vars 中的星号让Python创建一个名为vars的空元组,将收到的参数封装其中.

# eg:

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 形参名*toppings 中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都
# 封装到这个元组中。

# Making a pizza with the following toppings:
# - pepperoni
#
# Making a pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese


# 9-2)混合使用位置实参和任意数量实参:
# 函数同时接受位置实参,关键字实参，以及任意数量的实参时,任意数量实参的形参必须放在最后。
# Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

# eg:如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参*toppings的前面：

def make_pizza(size, *toppings):
    print(
        "\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Making a 16-inch pizza with the following toppings:
# - pepperoni
#
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese


# 9-3)混合使用关键字实参和任意数量实参:

# 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，
# 可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
# (也可理解成传入字典的方式是解包字典)
# Notes: Key必须为变量才行.


# eg:创建用户简介：你知道你将收到有关用户的信息，但不确定会是什么样的信息。
# 函数build_profile()接受名和姓，同时还接受任意数量的关键字实参：

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field=
'physics')

print(user_profile)


# {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton',
# 'field': 'physics'}


# 10--传递字典: 字典不能直接传入函数,先要解包才可.
# **dic  表示已经解包的一个字典类型的参数(即传入的参数是key=value的形式),Key 必须为变量.
def dealwithdictionary(**d):
    message = ""
    for k, v in d.items():
        message = message + k + ":" + v + ","
    return message


# favorite_languages = {"tom": "java", "ivan": "python", "alex": "vba"}

msg = dealwithdictionary(tom="java", ivan="python", alex="vba")
print(msg)  # tom:java,ivan:python,alex:vba,

# 11--将函数存储在模块中
# 将函数存储在称为模块的独立文件中，再将模块import到主程序中。
# 将函数存储在称为模块的独立文件中的好处：
# （1）可隐藏程序代码的细节，将重点放在程序的高层逻辑上。
# （2）能够在其他程序中重用函数。
# （3）与其他人共享这些文件而不是整个程序。
# （4）使用其他程序员编写的函数库。
# Python读取这个文件时，代码行import pizza让Python打开文件pizza.py，并将其中的所有函数
# 都复制到这个程序中。你看不到复制的代码，因为这个程序运行时，Python在幕后复制这些代码。

# 1）:创建模块，模块是扩展名为.py的文件，包含要导入到程序中的代码。
# pizza.py
# def make_pizza(size, *toppings):
#     print("\nMaking a " + str(size) +"-inch pizza with following toppings:")
#
#     for topping in toppings:
#         print("- " + topping)

import pizza

help(pizza)
# Help on module pizza:
# NAME
#     pizza
# FUNCTIONS
#     make_pizza(size, *toppings)
# FILE
# c:\users\xuyunpeng\pycharmprojects\pythontestproject001\function_method\pizza.py

# 2）:导入模块并调用模块里的函数。
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Making a 16-inch pizza with following toppings:
# - pepperoni
#
# Making a 12-inch pizza with following toppings:
# - mushrooms
# - green peppers
# - extra cheese

# 3）：使用as给导入的模块指定别名：
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 4）：导入模块中特定的函数：
# 语法：from module_name import function_name
# 语法：from module_name import function_0, function_1, function_2
# 由于我们在import 语句中显式地导入了函数make_pizza()，因此调用它时只需指定其名称。
# eg：
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 5）：使用as给导入的函数指定别名：
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# 将函数make_pizza()重命名为mp()，即避免与此程序可能包含的函数make_pizza()混淆。
# 也可简化代码长度。


# 6）：导入模块中所有的函数：
# 使用星号（*）运算符可让Python导入模块中的所有函数：
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# import 语句中的星号让Python将模块pizza中的每个函数都复制到这个程序文件中。
# 由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。
# 然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法，因为：
#   如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：
#       Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。
# 最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。

# 这能让代码更清晰，更容易阅读和理解。这里之所以介绍这种导入方法，只是想让你在阅
# 读别人编写的代码时，如果遇到类似于下面的import 语句，能够理解它们：
# from module_name import *


# 12--函数编写指南：

# （1）应给函数指定描述性名称，且只在其中使用小写字母和下划线。
# （2）模块命名时也应遵循上述约定。
# （3）每个函数都应包含简要地阐述其功能的注释（功能，实参及返回值类型），该注释应紧跟在
# 函数定义后面，并采用文档字符串格式。
# （4）给形参指定默认值时，等号两边不要有空格：
# def function_name(parameter_0, parameter_1='default value')
# （5）对于函数调用中的关键字实参时，等号两边也不要有空格：
# function_name(value_0, parameter_1='value')
# （6）如果形参很多，导致函数定义的长度超过了79字符，可在函数定义中输入左括号后按回车键，
# 并在下一行按两次Tab键，从而将形参列表和只缩进一层的函数体区分开来：
# def function_name(
#       parameter_0, parameter_1, parameter_2,
#       parameter_3, parameter_4, parameter_5):
# function body...



