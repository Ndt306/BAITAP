print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

Words = input().split()
Max_len = max(len(w)for w in Words)
print(*[w for w in Words if len(w)== Max_len],sep="\n")
