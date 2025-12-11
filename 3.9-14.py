print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

ds = input("Nhập chuoi:").split()
x = ds[1:-1]
for c in x:
    print(c)
print("##########")
ds.append("love")
for ch in ds:
    print(ch)
print("##########")
ds.remove("love")
for ch in ds:
    print(ch)
print("##########")
ds.sort()
for ch in ds:
    print(ch)
print("##########")
print("Vị trí của chuỗi one là", ds.index("one"))

