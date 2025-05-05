j = input()
s = input()
n = len(j)
k = 0
for i in range(n):
    k += s.count(j[i])
print(k)
