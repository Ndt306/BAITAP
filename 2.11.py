print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

def benefit(t,n,k):
    A = n*(1+t/100)**k
    return A
t =float(input("Nhập lãi suất:"))
n =float(input("Nhập số vốn ban đầu:"))
k =float(input("Nhập số tháng gửi:"))
print("Số tiền nhận được sau",k,"tháng là:",benefit(t,n,k))
