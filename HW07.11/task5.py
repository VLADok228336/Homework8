n = int(input())
item = []
price = []
d = {}
for i in range(n):
    f = input().split()
    item.append(f[0])
    price.append(f[1])
    d[i] = {f[0]:f[1]}
print(d)
g= price.sort()
k = item.sort()
i = 0