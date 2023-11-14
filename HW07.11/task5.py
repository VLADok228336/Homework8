n = int(input())
item = []
price = []
d = {}
for i in range(n):
    f = input().split()
    item.append(f[0])
    price.append(f[1])
item_item = item.copy()
price_price = price.copy()
price_price.sort()

print(price_price)
i = 0