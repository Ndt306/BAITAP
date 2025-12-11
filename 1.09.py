print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

str = input("enter a string:")
dict = {}
for i in str:
    dict[i] = str.count(i)
print(dict)
