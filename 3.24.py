print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

s = input("Nhập câu:")

upper_count = 0
lower_count = 0

for ch in s:
    if ch.isupper():
        upper_count +=1
    elif ch.islower():
        lower_count +=1

print("Chữ hoa:", upper_count)
print("Chữ thường:", lower_count)

