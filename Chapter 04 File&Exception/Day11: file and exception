#                              文件和异常
# 内容：
# 1)学习处理文件，让程序能够快速地分析大量的数据；
# 2)学习错误处理，避免程序在面对意外情形时崩溃；
# 3)学习异常，它们是Python创建的特殊对象，用于管理程序运行时出现的错误；
# 4)学习模块json，它让你能够保存用户数据，以免在程序停止运行后丢失。

# 意义:
# １）学习处理文件和保存数据:可让你的程序使用起来更容易：用户将能够选择输入什么样的数据，
# 以及在什么时候输入；用户使用你的程序做一些工作后，可将程序关闭，以后再接着往下做。

# ２）学习处理异常:可帮助你应对文件不存在的情形，以及处理其他可能导致程序崩溃的问题。
# 这让你的程序在面对错误的数据时更健壮——不管这些错误数据源自无意的错误，还是源自破坏程序
# 的恶意企图。
#
# 你在本章学习的技能可提高程序的适用性、可用性和稳定性。

# 文件：读取（整个读取，单行读取），写入（单行写入，多行写入），追加。


# 一,读取文件内容:

# １--从文件中读取数据:
#   1)读取整个文件的全部内容. file_object.read() 返回一个包含所有文本内容的字符串。
#   2)每次读取一行.
#      （1）file_object.readline() 返回单行文本作为一个字符串。
#      （2）file_object.readlines()返回以单行文本作为字符串类型元素的列表。

# 1-1.读取整个文件的全部内容:

with open('pi_digits.txt') as file_object:  # as 后面的这个变量名随便起.
    contents = file_object.read()
    print(contents)

# (1)绝对路径:

file_fullname = 'D:\PycharmProjects\pythontestproject01\Files_Exception\pi_digits.txt'
with open(file_fullname) as file_object:
    contents = file_object.read()
    print(contents)

# (2)相对路径:
with open('file_test\pi_digits.txt') as file_object: #当前文件所在文件夹内的子文件夹 file_test
    contents = file_object.read()
    # print(contents)
    print(contents.rstrip())  #去空行

# 3.1415926535
# 8979323846
# 2643383279

# 函数open()接受一个参数：要打开的文件的名称。python在当前执行的文件所在的目录中查找指定
# 的文件,返回一个表示文件的对象.

# 在windows文件路径中使用反斜杠（\ ）而不是斜杠（/ ）.(但我尝试的结果是,两种斜杠都可以!!!)

# 关键字with会自动地将不再需要访问的文件关闭。你只管打开文件，并在需要时使用它，Python自
# 会在合适的时候自动将其关闭。

# 在这个程序中，注意到我们调用了open()，但没有调用close()；
# 你也可以调用close()来关闭文件，但这样做时:
# (1)如果程序存在bug，导致close()语句未执行，文件将不会关闭,未妥善地关闭文件可能会导致数
# 据丢失或受损。

# 如果在程序中过早地调用close()，你会发现需要使用文件时它已关闭（无法访问），这会导致更多
# 的错误。并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可让
# Python去确定.


# 有了表示pi_digits.txt的文件对象后，我们使用方法read()读取这个文件的全部内容，并将其作
# 为一个长长的字符串存储在变量contents中。 这样，通过打印contents的值，就可将这个文本
# 文件的全部内容显示出来.

# 相比于原始文件，该输出唯一不同的地方是末尾多了一个空行,因为read()到达文件末尾时返回一个
# 空字符串，而将这个空字符串显示出来时就是一个空行。要删除多出来的空行，可在print语句中使
# 用rstrip()：print(contents.rstrip())。


# 注意: Windows系统有时能够正确地解读文件路径中的斜杠( /)。如果你使用的是Windows系统，
# 且结果不符合预期，请确保在文件路径中使用的是反斜杠(\)。

# 1-2.按行读取文件：
# 在文件中查找特定的信息，或者要以某种方式修改文件中的文本时要用到按行读取文件。
# 例如:
# (1)你可能要遍历一个包含天气数据的文件，并使用天气描述中包含字样sunny的行。
# (2)在新闻报道中，你可能会查找包含标签<headline>的行，并按特定的格式设置它。

# 以每次一行的方式检查文件，可对文件对象使用for 循环：

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:  # line 也可以是其他的变量名字,随便起
        print(line)

# 3.1415926535
#
# 8979323846
#
# 2643383279
#

# 每行的末尾都有一个看不见的换行符，而print语句也会加上一个换行符，因此每行末尾都有两个
# 换行符：一个来自文件，另一个来自print语句。要消除这些多余的空白行，可在print语句中使用
# rstrip().

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:  # line 也可以是其他的变量名字,随便起
        print(line.rstrip())

# 2--创建一个包含文件各行内容的列表: (以每行内容作为一个列表元素)
# 因为使用关键字with时，open()返回的文件对象只在with代码块内可用。如果要在with代码块外
# 访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，这样就既可在with代码块内
# 使用该列表,也可以在with代码块外面使用它。

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    # print(line)
    print(line.rstrip())

# 方法readlines()从文件中读取每一行，并将其存储在一个列表中；
# 接下来，该列表被存储到变量lines中；在with代码块外，我们依然可以使用这个变量。

# 3--使用文件的内容:

# 将文件读取到内存中后，就可以以任何方式使用这些数据了。
# 下面以简单的方式使用圆周率的值。
# 首先，我们将创建一个字符串，它包含文件中存储的所有数字，且没有任何空格：

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_str = ""
for line in lines:
    pi_str += line.strip()  # line.rstrip()

print(pi_str)  # # 3.141592653589793238462643383279
print(len(pi_str))  # 32

if "5897" in pi_str:
    print("5897 is in " + pi_str)
# 5897 is in 3.141592653589793238462643383279

# 知识链接:
# Python中有三个去除头尾【字符】或【空白符】的函数，它们依次为:
# str.strip： 用来去除头尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# str.lstrip：用来去除开头字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# str.rstrip：用来去除结尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
#
# 注意：这些函数都只会删除头和尾的字符，中间的不会删除。
#
# 用法分别为：
# str.strip([chars])  # []表示可选,不是列表符号.
# str.lstrip([chars])
# str.rstrip([chars])
#
# 参数chars是可选的，当chars为空，默认删除string头尾的空白符(包括\n、\r、\t、' ')
# 当chars不为空时，函数会被chars解成一个个的字符，然后将这些字符去掉。
#
# 它返回的是去除头尾字符(或空白符)的string副本，string本身不会发生改变。

# str="asdfghjk"
# print(str.rstrip("jk"))  # asdfgh
# print(str.rstrip("zk"))  # asdfghj  去掉了K
# print(str)  # asdfghjk


# 二,将内容写入文件:

# 往文本内写内容：
# 1）单行写入：
# 2）多行写入:每行末尾添加换行符\n


# 1--以单行的形式写入文件:
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    new_number = 123456789
    file_object.write(str(new_number))

# filename = 'programming.txt'
# with open(filename, 'w+') as file_object:
#     file_object.write("I love programming222.")
#     print(file_object.read())  # 只会显示一个空行.因为此时光标位置位于最后。


filename = 'programming.txt'
with open(filename, 'w+') as file_object:
    file_object.write("I love programming222.")
    file_object.seek(0, 0)  # 将当前打开的文件的光标移到文件开头.
    contents = file_object.read().strip()
    print(contents)

# 补充一下open(filename[,"r/w/a/r+"])知识点:
# 第一个实参也是要打开的文件的名称；
# 第二个实参为模式实参: 读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或
# 能够读取和写入文件的模式（'r+'）。
# Python只能将字符串写入文本文件:要将数值数据存储到文本文件中，必须先使用函数str()将其
# 转换为字符串格式。
# 更详细的介绍请参考: https://www.runoob.com/python/python-files-io.html

# 如果你省略了模式实参，Python将以默认的只读模式打开文件。

# 以写入（'w'）模式打开文件时:
# (1)如果要写入的文件不存在，函数open()将自动创建它。
# (2)如果指定的文件已经存在，Python将在返回文件对象前清空该文件。

# 以写入（'w+'）模式打开文件时:
# (1)如果要写入的文件不存在，函数open()将自动创建它。
# (2)如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
# (3)虽然支持读的操作,但光标位置需要重新定位到文件开头才可以:
#    1)没有with时,读文件时也可以先file.close()之后,再file.open(filename,"r")读取,
#      就不用重置光标位置了.
#    2)有with时,with会自动将文件关闭,光标重置,重新使用with file.open(filename,"r")即可.

# 2--以多行的形式写入文件:末尾添加换行符\n.

filename = 'programming.txt'
with open(filename, 'w+') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    file_object.write("I love creating new games2.\ngames3")
    file_object.seek(0, 0)  # 将当前打开的文件的光标移到文件开头.
    contents = file_object.read().strip()
    print(contents)

# I love programming.
# I love creating new games.
# I love creating new games2.
# games3


# 三, 将内容追加到文件:

# 如果要给文件添加内容，而不是覆盖原有的内容，可以附加模式打开文件,Python不会在返回
# 文件对象前清空文件，而将写入到文件的行都将添加到文件末尾。
# 如果指定的文件不存在，Python将为你创建一个空文件。

filename = 'programming.txt'
# step01：先创建文件，并写入内容：
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love programming222.\n")
    file_object.write("I love programming333.")
# step02:在上面的文件中追加内容：
with open(filename, 'a') as file_object:
    file_object.write("\nI love programming444.")  #追加内容时，要加换行符才可以换行。
# step03:读取上述写入和追加的内容：
with open(filename, 'r') as file_object:
    print(file_object.read())

# I love programming.
# I love programming222.
# I love programming333.I love programming444.

# 追加模式并不会在原来内容前面加换行符,可以下方式改进:

with open(filename, 'a') as file_object:
    file_object.write("\nI love programming444.")

# 四, 异常处理:

# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。每当发生让Python不知所措
# 的错误时，它都会创建一个异常对象。

# 如果你编写了处理该异常的代码，程序将继续运行；
# 如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。

# 1--处理ZeroDivisionError异常
# 下面来看一种导致Python引发异常的简单错误: 除数为0的情况:

print(5 / 0)

# Traceback (most recent call last):
#   File "D:.......", line 1, in <module>
#     print(5/0)
# ZeroDivisionError: division by zero


# 在上述traceback中，python指出的错误ZeroDivisionError是一个异常对象。
# Python无法按你的要求做时，就会创建这种对象。在这种情况下，Python将停止运行程序，并指出
# 引发了哪种异常，而我们可根据这些信息对程序进行修改。

# 2--使用try-except代码块来处理异常:
# 语法:
# try:
#     可能会出异常的程序代码
# except 想捕获的异常类型:
#     自定义的异常处理代码
# [else:]
#     [没有异常时的处理代码]

divisor = int(input("请输入一个除数(正整数):"))
dividend = int(input("请输入一个被除数(正整数):"))

try:
    print(divisor / dividend)
except ZeroDivisionError:
    print("you can't divide by zero!")

# 请输入一个除数(正整数):5
# 请输入一个被除数(正整数):0
# you can't divide by zero!

# 如果try-except 代码块后面还有其他代码，程序将接着运行，因为已经告诉了Python如何处理
# 这种错误。下面来看一个捕获错误后程序将继续运行的示例。


# 3--不使用异常时,程序崩溃,且暴露你的代码:
# 未使用异常处理时,不但会报错,还会通过traceback暴露你的代码,训练有素的攻击者会通过
# 此种方式获取相关信息判断对你的程序发动什么样的攻击.
# (例如，他将知道你的程序文件的名称，还将看到部分不能正确运行的代码.)
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
# 当用户把除数输入为0时:

# Give me two numbers, and I'll divide them.
# Enter 'q' to quit.
# First number: 5
# Second number: 0
# Traceback (most recent call last):
# File "D:........py", line 9, in <module>     此处暴露文件路径及名称
# answer = int(first_number) / int(second_number)  此处暴露你的代码
# ZeroDivisionError: division by zero


# 4--使用try-except-else代码块:
# 依赖于try代码块成功执行的代码都放在else代码块中:

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:  # 用它只包围可能出错的地方
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero!")
    else:
        print(answer)

# try-except-else使用要点:
# 1)只有可能引发异常的代码才需要放在try语句中。
# 2)仅在try代码块成功执行时才需要运行的代码放在else代码块中。
# 3)except代码块用来存放自定义的异常处理代码块。

# 5--处理FileNotFoundError异常:
# 使用文件时， 一种常见的问题是找不到文件：
#   1)提供的文件路径不对;
#   2)文件名不正确;
#   3)文件根本就不存在。
# 对于所有这些情形，都可使用try-except代码块以直观的方式进行处理。

# 例如:
filename = 'alice.txt'
with open(filename) as f_obj:
    contents = f_obj.read()

# Traceback (most recent call last):
#     File "alice.py", line 3, in <module>
#         with open(filename) as f_obj:
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

# 使用try-except改进上面程序:
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("sorry, the file: " + filename + " does not exist.")

# 如果文件不存在，这个程序什么都不做，因此错误处理代码的意义不大。
# 下面来扩展这个示例，看看在你使用多个文件时，异常处理可提供什么样的帮助。


# 5--分析文本:
# str.split([指定的字符或符号]) 方法:参数缺省时,默认以" "为参数.将文本按参数分割成列表.

title = "Alice in Wonderlan"
list01 = title.split()
print(title)
print(list01)
# Alice in Wonderlan
# ['Alice', 'in', 'Wonderland']

title = "Alice-in-Wonderlan"
list02 = title.split("-")
print(list02)

title = "AliceOinOWonderlan"
list03 = title.split("O")
print(list03)

# 回到我们的例子来: 分析文本:统计文本文件中大致含有多少文字:
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 分析文本:计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


# 6--使用多个文件:
# 下面多分析几本书。这样做之前，我们先将这个程序的大部分代码移到一个名为count_words()的
# 函数中，这样对多本书进行分析时将更容易：

def count_words(filename):
    """计算文本文件中含有多少个word"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "sorry, the file:" + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)


filename = "alice.txt"
count_words(filename)

# 当有多个文件需要分析时(需要统计字数时),使用列表,for循环加上述函数:
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# 文件siddhartha.txt不存在，但这丝毫不影响这个程序处理其他文件：
# The file alice.txt has about 29461 words.
# Sorry, the file siddhartha.txt does not exist.
# The file moby_dick.txt has about 215136 words.
# The file little_women.txt has about 189079 words.


# 7--失败时一声不吭:
def count_words(filename):
    """计算文本文件中含有多少个word"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass  # 如果文件找不到,直接越过,不报任何错.
    else:
        words = contents.split()
        num_words = len(words)


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# pass 语句还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些
# 什么。例如，在这个程序中，我们可能决定将找不到的文件的名称写入到文件missing_files.txt
# 中。用户看不到这个文件，但我们可以读取这个文件，进而处理所有文件找不到的问题。


# 8--决定报告哪些错误:
# 在什么情况下该向用户报告错误？在什么情况下又应该在失败时一声不吭呢？
# 1)如果用户知道要分析哪些文件，他们可能希望在有文件没有分析时出现提示消息时,报告给他们。
# 2)如果用户只想看到结果，而并不知道要分析哪些文件，可能就无需在有些文件不存在时告知他们。
# 3)向用户显示他不想看到的信息可能会降低程序的可用性。
# Python的错误处理结构让你能够细致地控制与用户分享错误信息的程度，要分享多少信息由你决定。

# 编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，但只要程序依赖于外
# 部因素，如用户输入、存在指定的文件、有网络链接，就有可能出现异常,此时按照上述3条来决定
# 要不要报告给用户.

