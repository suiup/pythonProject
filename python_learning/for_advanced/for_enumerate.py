count = 0
l = [11,22,33,44]
for data in l:
    if count == 2:
        data += 11
    l[count] = data
    count += 1
print(l)

m = [11,22,33,44]
for index, num in enumerate(m):
    if index == 2:
        num += 11
    m[index] = num

print(m)

n = [11,22,33,44]
d = {}
for index, num in enumerate(n, start=5):
    d[index] = num
print(d)
