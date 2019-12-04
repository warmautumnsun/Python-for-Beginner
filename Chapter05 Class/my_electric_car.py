
"""从含右多个类的模块中导入需要的类"""
from car import ElectricCar

my_tesla=ElectricCar("tesla","model s",2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# 2019 Tesla Model S
# This car has a 70-kWh battery.
# This car can go approximately 240 miles on a full charge.

"""从含有多个类的模块中一次导入多个类"""
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# 2016 Volkswagen Beetle
# 2016 Tesla Roadster

"""导入整个模块"""
# 你还可以导入整个模块，再使用句点表示法访问需要的类。这种导入方法很简单，代码也易于阅读。
# 由于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。（推荐）

import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla=car.ElectricCar("tesla","model s",2019)
print(my_tesla.get_descriptive_name())

# 2016 Volkswagen Beetle
# 2019 Tesla Model S

"""导入模块的所有类"""
# 要导入模块中的每个类，可使用下面的语法：
# from module_name import *
# 极不推荐使用：
#   1）这种导入方式没有明确地指出你使用了模块中的哪些类。
#   2）这种导入方式还可能引发名称方面的困惑。如果导入了一个与程序文件中其他东西同名的类，
#   将引发难以诊断的错误。




