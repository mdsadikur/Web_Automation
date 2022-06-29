'''
Inheritance
'''


class Car():
    def __init__(self):
        print("Just Created car Instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car Stopped")


car_obj = Car()
car_obj.drive()
car_obj.stop()


class BMW(Car):
    def __init__(self):
        print("BMW car Instance just Created")

    def breaking(self):
        print("BMW break.")


bmw_obj = BMW()
bmw_obj.drive()
bmw_obj.breaking()
bmw_obj.stop()


class Toyota(Car):
    def __init__(self):
        print("Toyota car just created instance")


toyota_obj = Toyota()
toyota_obj.drive()
BMW.breaking("bmw")
toyota_obj.stop()
