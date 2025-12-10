print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

nums = input("Nhập danh sách số:").split()

odd_numbers = [int(n) for n in nums if int(n) % 2 !=0]

print("Các số lẻ là:", odd_numbers)
