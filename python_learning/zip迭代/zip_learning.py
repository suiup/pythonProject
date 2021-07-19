name = ["a", "b", "c"]
score = [1,2,3]
d = {}
for i in range(3):
    d[name[i]] = score[i]
print(d)


e = {}
for n, s in zip(name, score):
    e[n] = s
print(e)


l = [1,2,3]
l.reverse()
print(l)

for i in reversed(l):
    print(i)