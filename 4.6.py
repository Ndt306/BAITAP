print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

class IOString:
    def __init__(self):
        self.strl = ""
    def get_String(self):
        self.strl = input()
    def print_String(self):
        print(self.strl.upper())

strl = IOString()
strl.get_String()
strl.print_String()
