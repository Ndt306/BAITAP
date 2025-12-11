print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

n = int(input())

for x in range(1, n):
    if sum(i for i in range(1, x) if x % i == 0) > x:
        print(x, end=" ")
