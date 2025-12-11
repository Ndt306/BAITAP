print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

n = int(input())
a,b = 0,1
fib = []
while a<n:
    fib.append(a)
    a,b=b,a+b
    print(fib)
