l = []
for i in range(10):
    if i % 2 == 0:
        l.append(i*2)
print(l)

m = [i * 2 for i in range(10) if i % 2 == 0]
print(m)

d = {"index"+str(i): i*2 for i in range(10) if i % 2 == 0}
print(d)