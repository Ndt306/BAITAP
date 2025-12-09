print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))
py = py_solution()
print(py.reverse_words("hello .py"))
