print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

import math

moves = []
print("Nhập các câu lệnh di chuyển :")
while True:
    line = input()
    if not line:
        break
    moves.append(line)
x = 0
y = 0

for move in moves:
    direction, steps = move.split()
    steps = int(steps)
    if direction.upper() == "UP":
        y += steps
    elif direction.upper() == "DOWN":
        y -= steps
    elif direction.upper() == "LEFT":
        x -= steps

distance = round(math.sqrt(x**2 + y**2))
print(distance)
