g = input().split()
city =g[0].split(".")[1].split(",")[0]
street = g[1].split(".")[1].split(",")[0]
building = g[2].split(".")[1].split(",")[0]
print(city, "\n", street, "\n", building)