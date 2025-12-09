print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(6)
print (aCircle.area())
    
