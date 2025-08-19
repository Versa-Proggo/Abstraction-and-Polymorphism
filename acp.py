class BMW:
    def fuel_type(self):
        print("BMW uses Petrol 0r Diesel engine")
    def max_speed(self):
        print("BMW's top speed is 250 km/h")
    def type(self):
        print("BMW is a luxury car")
class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol engine")
    def max_speed(self):
        print("Ferrari's top speed is 350 km/h")
    def type(self):
        print("Ferrari is a sports car")
class Toyota:
    def fuel_type(self):
        print("Toyota uses Petrol, Diesel or Hybrid engine")
    def max_speed(self):
        print("Toyota's top speed is 180 km/h")
    def type(self):
        print("Toyota is a reliable family car")
class Mercedes:
    def fuel_type(self):
        print("Mercedes uses Petrol, Diesel or Electric engine")
    def max_speed(self):
        print("Mercedes's top speed is 240 km/h")
    def type(self):
        print("Mercedes is a premium luxury car")
class Honda:
    def fuel_type(self):
        print("Honda uses Petrol or Hybrid engine")
    def max_speed(self):
        print("Honda's top speed is 200 km/h")
    def type(self):
        print("Honda is an affordable and practical car")
class Tesla:
    def fuel_type(self):
        print("Tesla uses Electric engine")
    def max_speed(self):
        print("Tesla's top speed is 260 km/h")
    def type(self):
        print("Tesla is a futuristic electric car")
b=BMW()
f=Ferrari()
t=Toyota()
m=Mercedes()
h=Honda()
t=Tesla()
for car in (b,f,t,m,h,t):
    car.fuel_type()
    car.max_speed()
    car.type()
