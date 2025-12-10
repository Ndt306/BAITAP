print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

s = input("Nhập câu")

letters = 0
digits = 0

for ch in s:
    if ch.isalpha():
        letters +=1
    elif ch.isdigit():
        digits +=1
print("Số chữ cái:", letters)
print("Số chữ số:", digits)
