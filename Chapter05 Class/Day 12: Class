#                            类Class
# 1--编写一个Dog类，包含name和age两个属性，sit和roll over两个行为：

# ❶Class Dog():
# ❷   """一次模拟小狗的简单尝试---这是文档字符串对该类进行描述"""
#
# ❸   """name和age两个属性"""
#     def __init__(self, name, age):
#       """初始化属性name和age"""
# ❹     self.name = name
#       self.age = age
#
# ❺   def sit(self):
#       """模拟小狗被命令时蹲下"""
#       print(self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#       """模拟小狗被命令时打滚"""
#       print(self.name.title() + " rolled over!")

# 解读：
# （1）在Python中，首字母大写的名称指的是类。❶
# （2）类中的函数称为方法，唯一与函数重要的差别是调用方法的方式。
# （3）__init__()是一个特殊的方法，当创建类的实例时Python都会运行它来根据类创建新实例.
#     （1.）开头和末尾各有两个下划线，旨在避免Python默认方法与普通方法发生名称冲突.
#     （2.）包含三个形参：self、name和age,形参self必不可少，必须位于其他形参的前面.
#     （3.）实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法.
#     （4.）Python调用__init__()创建类的实例时，将自动传入实参self，我们只需给最后两个
#          形参（name和age）提供值。
# （4）可通过实例访问的变量称为属性。
#     （1.）以self为前缀的变量可被类中的所有方法使用，还可以通过类的实例来访问这些变量。
#     （2.）self.name = name获取存储在形参name中的值，并将其存储到变量name中，然后该
#          变量被关联到当前创建的实例，可通过实例访问。
# （5）sit()和roll_over()方法：当前例子中，这两个方法只是打印一条消息，指出小狗的动作，
#     如果这个类包含在一个计算机游戏中，这些方法将包含创建小狗蹲下和打滚动画效果的代码。
#     如果这个类是用于控制机器狗的，这些方法将引导机器狗做出蹲下和打滚的动作。


# 2--根据类创建实例
class Dog():
    """一次模拟小狗的简单尝试---这是文档字符串对该类进行描述"""

    """name和age两个属性"""

    def __init__(self, name, a):  # 注：形参的名字可以随便起，一般和属性同名。
        """初始化属性name和age"""
        self.name = name
        self.age = a  # 初始化就是将 属性 和 形参 联系起来。

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


# 1)创建实例，并访问属性：
my_dog = Dog("tom", 3)  # 给类传实参时使用位置实参。
print("My dog is " + str(my_dog.age) + " years old.")
# My dog is 3 years old.

my_dog = Dog(age=3, name="tom")  # 给类传实参时使用关键字参数。
print("My dog's name is " + my_dog.name.title() + ".")
# My dog's name is Tom

# 2)调用方法：
my_dog.roll_over()  # Tom rolled over!
my_dog.sit()  # Tom is now sitting.


# 3--使用类和实例：
# 根据类建好实例之后,通常我们会修改实例的属性。
# (1)直接修改实例的属性.
# (2)编写方法以特定的方式进行修改.

# 3-1）Car类：编写一个存储了汽车各种信息（属性）和汇总这些信息的方法。
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())  # 2016 Audi A4


# 3-2）Car2类：给属性指定默认值。
# 类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。
# 在有些情况下，如设置默认值时，在方法__init__() 内指定这种初始值是可行的；
# 如果你对某个属性这样做了，就无需在_init_()的形参列表里为它提供初始值的形参。
# (也可以为其提供形参，但创建实例时，传入的实参的值不会改变默认值)。

class Car2():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car2('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# 2016 Audi A4
# This car has 0 miles on it.

class Car2():
    def __init__(self, make, model, year, odometer_reading):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car2('audi', 'a4', 2016, 10)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# 2016 Audi A4
# This car has 0 miles on it.   通过传入参数的方式不能改变带默认值的属性。


# 3-3）Car3类：修改属性的值：
#   （1）：直接修改属性的值。通过实例直接访问属性并赋值。
#   （2）：通过方法修改属性的值。
#   （3）：通过方法对属性的值进行递增。

class Car3():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 10  # 设初始里程为10

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


# 3-3-1）：直接修改属性的值。通过实例直接访问属性并赋值。
my_new_car = Car3('audi', 'a4', 2016)
my_new_car.odometer_reading = 15
my_new_car.read_odometer()  # This car has 15 miles on it.

# 3-3-2）：通过方法修改属性的值。
my_new_car = Car3('audi', 'a4', 2016)
my_new_car.read_odometer()  # This car has 10 miles on it.

my_new_car.update_odometer(5)  # You can't roll back an odometer!
my_new_car.read_odometer()  # This car has 10 miles on it.

my_new_car.update_odometer(20)
my_new_car.read_odometer()  # This car has 20 miles on it.


# 3-3-3）：通过方法对属性的值进行递增.

class Car4():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值禁止将里程表读数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_new_car = Car4('audi', 'a4', 2016)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()  # This car has 100 miles on it.


# 4--继承：B(A) B类继承A类
# 子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。

# 4-1)子类继承其父类的所有属性和方法:
class Car5():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car5):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)  # 注意参数里没有self!!


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.odometer_reading)
print(my_tesla.get_descriptive_name())


# 0
# 2016 Tesla Model S

# 我们创建的这个子类没有属于自己的属性和方法，仅测试其是否能够具备父类的属性和方法。
# (1)创建子类时，父类必须包含在当前文件中，且位于子类前面.
# (2)方法__init__() 接受创建Car 实例所需的信息.
# (3)super()是一个特殊函数，将父类和子类关联起来。让Python调用ElectricCar的父类的
#    __init__()方法，让ElectricCar实例包含父类的所有属性。

# 4-2)给子类定义独有的属性和方法:

# 4-2-1)给子类定义一个给定默认值的特有的属性（电瓶），以及一个描述该属性的方法：
class ElectricCar2(Car5):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """电动汽车的独特之处初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar2('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# 2016 Tesla Model S
# This car has a 70-kWh battery.

# 4-2-2)给子类定义一个特有的属性（车牌颜色），以及一个描述该属性的方法：：
class ElectricCar3(Car5):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, charge_times):
        """电动汽车的独特之处初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.charge_times = charge_times

    def chargetimesadd(self):
        print("charge times: " + str(self.charge_times))


my_tesla = ElectricCar3('tesla', 'model s', 2016, 10)
print(my_tesla.get_descriptive_name())
my_tesla.chargetimesadd()


# 2016 Tesla Model S
# charge times: 10

# 如果一个属性或方法是任何汽车都有的，而不是电动汽车特有的，就应将其加入到Car类，而不是
# ElectricCar 类中。这样，使用Car 类的人将获得相应的功能，而ElectricCar类只包含处理
# 电动汽车特有属性和行为的代码。


# 5--重写父类的方法:
# 对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。
# 为此，可在子类中定义一个父类方法同名的方法(重写)。
# 这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法.

class Car6():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def fill_gas_tank(self):
        print("加油成功!")


class ElectricCar4(Car6):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def fill_gas_tank(self):
        """实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法."""
        print("电动车不需要加油!")


my_el = ElectricCar4('tesla', 'model s', 2016)
my_el.fill_gas_tank()  # 电动车不需要加油!


# 6--将实例用作属性:
# 使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来
# 越长。在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。可以将大型类拆分成多个
# 协同工作的小类。

class Car7():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def fill_gas_tank(self):
        print("加油成功!")


class Battery():
    """将有关电池的信息单独放在一个类中"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    # def _int_(self):  # 与上面等效,但上面的是可以通过传参改变battery_size的值。
    #     self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar5(Car7):
    """此类的特有属性的值为Battery类的实例"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)
        """初始化此类的特有属性，并给其赋予初始值，因此参数列表里不用包含此属性的形参"""
        self.battery = Battery()
        # self.battery = Battery(100)

    def fill_gas_tank(self):
        """实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法."""
        print("电动车不需要加油!")


my_tesla = ElectricCar5('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()


# 2016 Tesla Model S
# This car has a 70-kwh battery.
# This car can go approximately 240 miles on a full charge.
# 电动车不需要加油!


# 7--模拟实物:
# 模拟较复杂的物件（如电动汽车）时，需要解决一些有趣的问题:
# 1)续航里程是电瓶的属性还是汽车的属性呢？
# 如果我们只需描述一辆汽车，那么将方法get_range()放在Battery 类中也许是合适的；
# 但要描述一家汽车制造商的整个产品线，也许应该将方法get_range()移到ElectricCar类中。
# 在这种情况下，get_range()依然根据电瓶容量来确定续航里程，但报告的是一款汽车的续航里程。
# 我们也可以这样做：将方法get_range()还留在Battery类中，但向它传递一个参数，如car_model；
# 在这种情况下，方法get_range()将根据电瓶容量和汽车型号报告续航里程。

# 这让你进入了程序员的另一个境界：解决上述问题时，你从较高的逻辑层面（而不是语法层面）考虑；
# 你考虑的不是Python，而是如何使用代码来表示实物。到达这种境界后，你经常会发现，现实世界的
# 建模方法并没有对错之分。有些方法的效率更高，但要找出效率最高的表示法，需要经过一定的实践。
# 只要代码像你希望的那样运行，就说明你做得很好！即便你发现自己不得不多次尝试使用不同的方法
# 来重写类，也不必气馁；要编写出高效、准确的代码，都得经过这样的过程.

# 练习题：

# 创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和
# cuisine_type。创建一个名为describe_restaurant()的方法和一个名为open_restaurant()
# 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。

class Restaurant():
    def __init__(self, re_name, cu_type):
        self.restaurant_name = re_name
        self.cuisine_type = cu_type

    def describe_restaurant(self):
        print("the cuisine in " + self.restaurant_name + "is " + self.cuisine)

    def open_restaurant(self):
        print("the restaurant is open")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ["ice", "spics", "hot", "sweet", "salty"]

    def describe_flavors(self):
        print(self.flavors)


iceshop = IceCreamStand("Collin's iceshop", "icecream")
iceshop.describe_flavors()


# ['ice', 'spics', 'hot', 'sweet', 'salty']

# 在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()
# 的方法。这个方法检查电瓶容量，如果它不是85，就将它设置为85。
# 创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级，并再次调用
# get_range()。你会看到这辆汽车的续航里程增加了.


class Car8():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def fill_gas_tank(self):
        print("加油成功!")


class Battery2():
    """将有关电池的信息单独放在一个类中"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    # def _int_(self):  # 与上面等效,但上面的是可以通过传参改变battery_size的值。
    #     self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar6(Car8):
    """此类的特有属性的值为Battery类的实例"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)
        """初始化此类的特有属性，并给其赋予初始值，因此参数列表里不用包含此属性的形参"""
        self.battery = Battery2()
        # self.battery = Battery(100)

    def fill_gas_tank(self):
        """实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法."""
        print("电动车不需要加油!")


my_elcar = ElectricCar6("tesla", "model s", 2016)
my_elcar.battery.get_range()
my_elcar.battery.upgrade_battery()
my_elcar.battery.get_range()

# This car can go approximately 240 miles on a full charge.
# This car can go approximately 270 miles on a full charge.

# 7--导入模块中的类:
# 随着你不断地给类添加功能，文件可能变得很长，即便你妥善地使用了继承亦如此。
# 为遵循Python的总体理念，应让文件尽可能整洁。为在这方面提供帮助，Python允许你将类存储在
# 模块中，然后在主程序中导入所需的模块。

# 单独建三个文件：car.py  和 my_car.py，my_electric_car.py


# 8--python标准库
# Python标准库是一组模块，安装的Python都包含它。可使用标准库中的任何函数和类，为此只需在
# 程序开头包含一条简单的import语句。下面来看模块collections中的一个类——OrderedDict。

# 1）字典让你能够将信息关联起来，但它们不记录你添加键—值对的顺序。
# 2）要（1）创建字典（2）并记录其中的键—值对的添加顺序，可使用模块collections中的
# OrderedDict类。OrderedDict 实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。

# 回忆一下之前学习Dictionary时的例子：

favorite_languages = {}

favorite_languages["tom"] = "java"
favorite_languages["ivan"] = "vba"
favorite_languages["alex"] = "automation"
favorite_languages["taylor"] = "python"

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

# 注,在python3.6之后,原生的字典也记录键—值对的添加顺序:
# Tom's favorite language is Java
# Ivan's favorite language is Vba
# Alex's favorite language is Automation
# Taylor's favorite language is Python


# 使用collections模块中的OrderedDict类:

from collections import OrderedDict

favorite_languages = OrderedDict()  # 创建一个OrerDict()的实例,空字典.

favorite_languages["tom"] = "java"
favorite_languages["ivan"] = "vba"
favorite_languages["alex"] = "automation"
favorite_languages["taylor"] = "python"

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

# 无论运行多少遍，结果都是：
# Tom's favorite language is Java
# Ivan's favorite language is Vba
# Alex's favorite language is Automation
# Taylor's favorite language is Python


# 练习题:
# 骰子：模块random包含以各种方式生成随机数的函数，其中的randint()返回一个位于指定
# 范围内的整数.
# 例如，下面的代码返回一个1~6内的整数：
# from random import randint
# x = randint(1, 6)
# 请创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。编写一个名为roll_die()
# 的方法，它打印位于1和骰子面数之间的随机数。创建一个6的骰子，再掷10次。创建一个10面的骰子
# 和一个20面的骰子，并将它们都掷10次。

from random import randint


class Die():
    """骰子类"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


my_die = Die()
print(my_die.roll_die())

# 看看上面的骰子在特定次数下,各个面出现的几率是多少(当次数多时,各个面的几率应该接近).

# step1:创建一个和骰子面数相同长度的列表,用来记录各面出现的次数,各面次数先初始化为0.
sidenumbercounts = [None] * my_die.sides
for i in range(0, sides):
    sidenumbercounts[i] = 0

# step2: 设定尝试次数,并开始摇骰子,用列表记录各面出现的次数.
try_times = 100000

for i in range(try_times):
    n = my_die.roll_die()
    for j in range(0, my_die.sides):
        if n == j + 1:
            sidenumbercounts[j] += 1

# step3:打印列表的各元素与尝试次数的比值(即显示各面出现的几率).
for i in range(0, my_die.sides):
    print(str(i) + "出现的几率是: " + str(sidenumbercounts[i] / try_times))


# 也可以写成函数:
def probability_of_eachside_of_sides(sides, try_times):
    my_die = Die(sides)  # 函数内部可以实例化类

    sidenumbercounts = [None] * sides  # 别忘了创建特定长度的空列表的方法:

    for i in range(0, sides):
        sidenumbercounts[i] = 0

    for i in range(try_times):
        n = my_die.roll_die()
        for j in range(0, sides):
            if n == j + 1:
                sidenumbercounts[j] += 1

    for i in range(0, sides):
        print(str(i) + "出现的几率是: " + str(sidenumbercounts[i] / try_times))


probability_of_eachside_of_sides(6, 100000)


# 上述function可以用来测试randint的随机程度,伪随机数.

def probability_of_eachside(sides, try_times):
    sidenumbercounts = [None] * sides  # 别忘了创建特定长度的空列表的方法:

    for i in range(0, sides):
        sidenumbercounts[i] = 0

    for i in range(try_times):
        n = randint(1, sides)  # 改成如此,直接使用randint
        for j in range(0, sides):
            if n == j + 1:
                sidenumbercounts[j] += 1

    for i in range(0, sides):
        print(str(i) + "出现的几率是: " + str(sidenumbercounts[i] / try_times))


probability_of_eachside(10, 100000)

# 0出现的几率是: 0.10077
# 1出现的几率是: 0.10061
# 2出现的几率是: 0.09981
# 3出现的几率是: 0.10023
# 4出现的几率是: 0.09979
# 5出现的几率是: 0.10207
# 6出现的几率是: 0.09839
# 7出现的几率是: 0.09997
# 8出现的几率是: 0.09856
# 9出现的几率是: 0.0998

# 当然,每次运行,上面的结果都不一样.


# 9--类的编码风格:
# 1)类的名称命名:驼峰命名法--类名中的每个单词的首字母大写, if 不使用下划线:
# 2)在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的
#   文档字符串时采用的格式约定。
# 3)每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
# 4)在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类.
# 5)需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再添加
#   一个空行，然后编写导入你自己编写的模块的import语句。
