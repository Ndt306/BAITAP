print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

import math

n = int(input("Nhập n: "))

for i in range(n):
    print(" " * (n - 1), end="")
    for j in range(i + 1):
        print(math.comb(i, j), end=" ")
    print()
