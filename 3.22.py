print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

result = []
for num in range(1000,3001):
    s = str(num)
    if all(int(d) % 2 == 0 for d in s):
        result.append(s)
print(",".join(result))
