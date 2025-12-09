print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return 3.141592653589793 * (self.radius ** 2)
    def circumference(self):
        return 2 * 3.141592653589793 * self.radius

r = input("Nhập bán kính: ")
c = Circle(r)

print("Diện tích:", c.area())
print("Chu vi:", c.circumference())
