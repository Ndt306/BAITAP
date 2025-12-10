print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

S = input("Nhập các số nhị phân:")

binaries = S.split(",")

valid = []
for b in binaries:
    num = int(b, 2)
    if num % 5 == 0:
        valid.append(b)

print(",".join(valid))
