print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

a,b = 0,1
total = 0
print(a,end=" ")
while (a<=4000000-1):
    if a % 2 == 0:
        total +=a
    a, b =b, a+b
    print(a,end=" ")
print("\n sum of prime number term in fibonacci series:", total)
