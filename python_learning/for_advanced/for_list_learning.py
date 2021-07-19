l = []
for i in range(10):
    l.append(i * 2)
print(l)

m = [i * 2 for i in range(10)]
print(m)

# 字典 key: value
d = {"index" + str(i): i * 2 for i in range(10)}
print(d)