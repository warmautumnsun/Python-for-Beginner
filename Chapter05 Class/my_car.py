from car import Car

my_new_car = Car("audi", "a6", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 2019 Audi A6
# This car has 23 miles on it.

