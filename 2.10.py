print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

import math
def Tinh(R):
    if R<=0:
        return("Bán kính phải là số dương!")
    P = 2*math.pi*R
    S = math.pi*R**2
    return P,S
try:
    R = float(input("Nhập R"))
    KQ = Tinh(R)
    if isinstance( KQ, str):
        print(KQ)
    else:
        P, S = KQ
        print(f"Chu vi hình tròn: {P}")
        print(f"Diện tích hình tròn: {S}")
except ValueError:
    print("Giá trị nhập không hợp lệ!")
