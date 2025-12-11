print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

y =[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        y.append(str(i))
print(','.join(y))
