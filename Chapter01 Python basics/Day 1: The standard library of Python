了解几个常用的标准库


# 标准库的导入方式:
# from datetime import datetime
# from os import getcwd
# import sys
# import os
# import datetime
# import time

# Example 1--使用datetime父包获取分钟，判断其是否在奇数数组内：
import datetime
odds = [1, 3, 5, 7, 9, 1, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37,
        39, 41, 43, 45, 47, 49, 51, 53, 57, 59]
current_minute = datetime.datetime.today().minute
# 第一个datetime是主模块(包),第二个datetime是子模块,today()是方法,minute是属性.

if current_minute in odds:
    # 超级操作符in 检查一个对象是否是另一个对象的元素,用于判断, 和if配合使用.
    # if 操作符会返回一个布尔类型的返回值.
    # python用缩进区分代码组
    # :的作用是用来引入与python控制语句(if, else, for等)关联的代码块
    print("this minute is a odd", current_minute)  # 第一个块
else:
    print("this minute is not a odd", current_minute)  # 第二个块

## this minute is not a odd 34

# Example 2--使用datetime包，获取当前系统的年月日：
# 天以内的time要用datetime的子包datetime的方法.
import datetime
print(datetime.datetime.today().minute)
print(datetime.date.today())
print(datetime.date.today().month)
print(datetime.date.today().day)
print(datetime.date.today().year)

# Example 3--使用datetime子包获取分钟，判断其是否在奇数数组内：
from datetime import datetime
current_minute = datetime.today().minute

if current_minute in odds:
    print("this minute is a odd", current_minute)
else:
    print("this minute is not a odd", current_minute)

## this minute is a odd 39

# Example 4--使用time包，获取当前系统的时间：
import time
print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))  ## Friday PM
print(time.strftime("%a %p"))  ## Fri PM

# Example 5--使用time包的sleep()方法：
for i in range(5):
    time.sleep(2)
    print("hello" + str(i))

# Example 6--使用os包，获取当前工作目录：
import os
print(os.getcwd())  # 会打印当前py 文件所在的路径
print(os.environ)  # 会打印当前系统的所有环境变量的 name:value

# Example 6--使用sys包，获取当前系统的平台和版本：
import sys
print(sys.platform)
## win32

print(sys.version)
## 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)]

# Example 7--使用randint包，获取上下限范围内的随机整数：
# randint(s,e) 随机结果包含上下限
import random
print(random.randint(1, 10))




# 使用dir方法获取库的方法列表：

# import datetime
# dir(datetime)
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__',
#  '__file__', '__loader__', '__name__', '__package__', '__spec__',
#  'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta',
#  'timezone', 'tzinfo']


# print(dir(random))
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
# 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence',
# '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '_
# _loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect',
# '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os',
# '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',
# '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate',
# 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate',
# 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange',
# 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform',
# 'vonmisesvariate', 'weibullvariate']



