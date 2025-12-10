print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

balance = 0
print("Nhập nhật kí giao dịch:")

while True:
    line = input()
    if not line:
        break
    try:
        action, amount = line.split()
        amount = int(amount)
    except ValueError:
        print("Định dạng sai.Nhập lại.")
        continue

    if action == "D":
        balance += amount
    elif action == "W":
        balance -= amount
    else:
        print("Hành động không hợp lệ (D hoặc W).")
        continue

print("Số dư cuối cùng là:", balance)
